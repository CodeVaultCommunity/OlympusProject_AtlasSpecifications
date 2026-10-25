"""Atlas LaTeX adapter (controlled profile)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from ..errors import AtlasError, AtlasParseError, AtlasVersionError, Diagnostic
from ..slots import externalize, restore
from ..util import (
    decode_text_exact,
    split_lines_keepends,
    strict_json_loads,
    strip_line_ending,
    write_text_exact,
)
from .base import Adapter, DecodeOptions, EncodeOptions
from .markdown_adapter import _derived_content
from ..graph_render import render_tikz

PROFILE = "atlas-latex"
VERSION = "Alpha-v0.1.0"
TRANSLATOR = "0.1.0"

HEADER_RE = re.compile(
    r"^% atlas:latex profile=atlas-latex representation=(?P<version>\S+) "
    r"translator=(?P<translator>\S+)$"
)
ENV_NAMES = (
    "atlastitle",
    "atlasheading",
    "atlastext",
    "atlasparagraph",
    "atlasitem",
    "atlasquote",
    "atlasnote",
    "atlascode",
    "atlasformula",
    "atlasderived",
)
BEGIN_RE = re.compile(
    r"^\\begin\{(?P<env>" + "|".join(ENV_NAMES) + r")\}(?P<args>(?:\{[^{}]*\})*)$"
)
END_RE = re.compile(r"^\\end\{(?P<env>" + "|".join(ENV_NAMES) + r")\}$")
STRUCTURE_BEGIN = "% atlas:structure:begin"
STRUCTURE_END = "% atlas:structure:end"
TIKZ_BEGIN_RE = re.compile(r"^% atlas:tikz:begin id=(?P<id>TIKZ-[A-Z0-9-]+)$")
TIKZ_END_RE = re.compile(r"^% atlas:tikz:end id=(?P<id>TIKZ-[A-Z0-9-]+)$")
CELL_RE = re.compile(r"\\AtlasCell\{(?P<id>T[0-9]{6})\}\{")

ESCAPES: list[tuple[str, str]] = [
    ("\\", r"\AtlasCharBackslash{}"),
    ("{", r"\AtlasCharLBrace{}"),
    ("}", r"\AtlasCharRBrace{}"),
    ("%", r"\AtlasCharPercent{}"),
    ("#", r"\AtlasCharHash{}"),
    ("&", r"\AtlasCharAmp{}"),
    ("_", r"\AtlasCharUnderscore{}"),
    ("$", r"\AtlasCharDollar{}"),
    ("^", r"\AtlasCharCaret{}"),
    ("~", r"\AtlasCharTilde{}"),
]
INLINE_ESCAPES: list[tuple[str, str]] = [
    ("\r\n", r"\AtlasCharNewline{}"),
    ("\n", r"\AtlasCharNewline{}"),
    ("\r", r"\AtlasCharNewline{}"),
    ("\t", r"\AtlasCharTab{}"),
]
UNESCAPES = {encoded: char for char, encoded in ESCAPES}
UNESCAPES.update(
    {
        r"\AtlasCharNewline{}": "\n",
        r"\AtlasCharTab{}": "\t",
    }
)
UNESCAPE_RE = re.compile(
    "|".join(re.escape(key) for key in sorted(UNESCAPES, key=len, reverse=True))
)


class LatexAdapter(Adapter):
    format_name = "latex"

    def decode(self, source: str | bytes | Path, options: DecodeOptions) -> dict:
        text, source_path = self._read_source(source)
        return decode_latex(text, source_path=source_path, options=options)

    def encode(self, document: dict, options: EncodeOptions) -> str:
        return encode_latex(document, options=options)

    def _read_source(self, source: str | bytes | Path) -> tuple[str, Path | None]:
        if isinstance(source, Path):
            return decode_text_exact(source.read_bytes(), location=str(source)), source
        if isinstance(source, bytes):
            return decode_text_exact(source, location="<bytes>"), None
        return source, None


def decode_latex(
    text: str, *, source_path: Path | None = None, options: DecodeOptions | None = None
) -> dict:
    options = options or DecodeOptions()
    lines = split_lines_keepends(text)
    records: dict[str, str] = {}
    derived: dict[str, str] = {}
    tikz: dict[str, str] = {}
    tikz_id: str | None = None
    tikz_lines: list[str] = []
    structure_lines: list[str] | None = None
    header_seen = False
    state = "normal"
    env_name: str | None = None
    env_args: list[str] = []
    content_lines: list[str] = []
    structure_state = "outside"
    line_number = 0

    def malformed(message: str) -> AtlasParseError:
        return AtlasParseError(
            Diagnostic(
                "ATL-E-LATEX",
                message,
                f"{source_path or '<latex>'}:{line_number}",
            )
        )

    def finish_env() -> None:
        nonlocal content_lines, env_name, env_args
        assert env_name is not None
        raw = "".join(content_lines)
        if raw:
            _, eol = strip_line_ending(content_lines[-1])
            if eol:
                raw = raw[: -len(eol)]
        decoded = unescape_latex(raw)
        if env_name == "atlasderived":
            derived_id = env_args[0]
            if derived_id in derived:
                raise malformed(f"duplicate derived region {derived_id}")
            derived[derived_id] = decoded
        else:
            if not env_args:
                raise malformed(f"{env_name} has no text record id")
            slot_id = env_args[0]
            if slot_id in records:
                raise malformed(f"duplicate text record {slot_id}")
            if not re.fullmatch(r"T[0-9]{6}", slot_id):
                raise malformed(f"invalid text record id {slot_id!r}")
            records[slot_id] = decoded
        content_lines = []
        env_name = None
        env_args = []

    for line in lines:
        line_number += 1
        body, _eol = strip_line_ending(line)
        if state == "env":
            end_match = END_RE.match(body)
            if end_match:
                if end_match.group("env") != env_name:
                    raise malformed(
                        f"environment {env_name} closed by {end_match.group('env')}"
                    )
                finish_env()
                state = "normal"
                continue
            if BEGIN_RE.match(body):
                raise malformed(f"nested Atlas environment inside {env_name}")
            content_lines.append(line)
            continue
        if state == "tikz":
            end_match = TIKZ_END_RE.match(body)
            if end_match:
                if end_match.group("id") != tikz_id:
                    raise malformed(
                        f"TikZ region {tikz_id} closed by {end_match.group('id')}"
                    )
                raw = "".join(tikz_lines)
                if raw:
                    _, eol = strip_line_ending(tikz_lines[-1])
                    if eol:
                        raw = raw[: -len(eol)]
                assert tikz_id is not None
                tikz[tikz_id] = raw
                tikz_id = None
                tikz_lines = []
                state = "normal"
                continue
            tikz_lines.append(line)
            continue
        if structure_state == "inside":
            if body == STRUCTURE_END:
                structure_state = "done"
                continue
            stripped = body[2:] if body.startswith("% ") else body[1:] if body.startswith("%") else None
            if stripped is None:
                raise malformed("structure appendix lines must be LaTeX comments")
            assert structure_lines is not None
            structure_lines.append(stripped + _eol)
            continue
        if structure_state == "done":
            if not body.strip() or body.strip() == r"\end{document}":
                continue
            raise malformed("content after the Atlas structure appendix")
        if body == STRUCTURE_BEGIN:
            if structure_lines is not None:
                raise malformed("structure appendix appears more than once")
            structure_lines = []
            structure_state = "inside"
            continue
        tikz_match = TIKZ_BEGIN_RE.match(body)
        if tikz_match:
            tikz_id = tikz_match.group("id")
            if tikz_id in tikz:
                raise malformed(f"duplicate TikZ region {tikz_id}")
            tikz_lines = []
            state = "tikz"
            continue

        begin_match = BEGIN_RE.match(body)
        if begin_match:
            env_name = begin_match.group("env")
            env_args = re.findall(r"\{([^{}]*)\}", begin_match.group("args"))
            if env_name == "atlasheading" and len(env_args) != 2:
                raise malformed("atlasheading requires a text id and a level")
            if env_name != "atlasheading" and len(env_args) != 1:
                raise malformed(f"{env_name} requires exactly one argument")
            content_lines = []
            state = "env"
            continue
        header_match = HEADER_RE.match(body)
        if header_match:
            if header_seen:
                raise malformed("duplicate Atlas LaTeX header")
            header_seen = True
            if header_match.group("version") != VERSION:
                raise AtlasVersionError(
                    Diagnostic(
                        "ATL-E-VERSION",
                        f"Atlas LaTeX version {header_match.group('version')!r} is not "
                        f"supported; this translator implements {VERSION!r}",
                        f"{source_path or '<latex>'}:{line_number}",
                    )
                )
            continue
        if body.startswith("\\begin{atlas") or body.startswith("\\end{atlas"):
            raise malformed(f"unsupported Atlas LaTeX environment: {body}")
        if body.startswith("% atlas:"):
            raise malformed(f"unknown or misplaced Atlas LaTeX marker: {body}")
        _extract_cells(body, records, malformed, line_number)

    if state == "env":
        raise malformed(f"unterminated environment {env_name}")
    if state == "tikz":
        raise malformed(f"unterminated TikZ region {tikz_id}")
    if structure_state == "inside":
        raise malformed("unterminated structure appendix")
    if structure_state != "done":
        raise malformed("missing Atlas structure appendix")
    if not header_seen:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-LATEX-HEADER",
                "missing Atlas LaTeX header comment",
                str(source_path) if source_path else "<latex>",
            )
        )
    payload = restore(strict_json_loads("".join(structure_lines or []), location="structure appendix"), records)
    for derived_id, content in derived.items():
        expected = _derived_content(payload, derived_id)
        if expected is None:
            raise AtlasParseError(
                Diagnostic(
                    "ATL-E-DERIVED-UNKNOWN",
                    f"derived region {derived_id!r} has no generator in this version",
                )
            )
        if content != expected:
            raise AtlasParseError(
                Diagnostic(
                    "ATL-E-DERIVED-STALE",
                    f"derived region {derived_id!r} does not match its sources. "
                    "Edit the authoritative text record or structure appendix, then "
                    "regenerate the representation with 'atlas convert'.",
                )
            )
    graph_ids = {graph["id"] for graph in payload["graphs"]}
    for graph_id in graph_ids:
        marker = f"TIKZ-{graph_id}"
        if marker not in tikz:
            raise AtlasParseError(
                Diagnostic(
                    "ATL-E-TIKZ-MISSING",
                    f"the LaTeX source has no derived TikZ diagram for graph {graph_id}; "
                    "regenerate the representation",
                )
            )
        graph = next(g for g in payload["graphs"] if g["id"] == graph_id)
        expected = render_tikz(graph)
        if tikz[marker] != expected:
            raise AtlasParseError(
                Diagnostic(
                    "ATL-E-TIKZ-STALE",
                    f"the derived TikZ diagram for graph {graph_id} does not match the "
                    "graph. Edit the graph structure and regenerate; do not edit the "
                    "derived diagram in place.",
                )
            )
    for marker in tikz:
        if marker not in {f"TIKZ-{graph_id}" for graph_id in graph_ids}:
            raise AtlasParseError(
                Diagnostic(
                    "ATL-E-TIKZ-UNKNOWN",
                    f"derived TikZ region {marker!r} has no matching graph",
                )
            )
    document = {"format": f"atlas-json/{VERSION}", "atlas": payload}
    options.validator.validate(
        document,
        resource_root=options.resource_root or (source_path.parent if source_path else None),
        check_resources=options.check_resources,
    )
    return document


def _extract_cells(body: str, records: dict[str, str], malformed, line_number: int) -> None:
    position = 0
    while True:
        match = CELL_RE.search(body, position)
        if not match:
            return
        slot_id = match.group("id")
        start = match.end()
        depth = 1
        index = start
        while index < len(body) and depth:
            char = body[index]
            if char == "\\":
                index += 2
                continue
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            index += 1
        if depth:
            raise malformed(f"unterminated AtlasCell for {slot_id}")
        raw = body[start : index - 1]
        if slot_id in records:
            raise malformed(f"duplicate text record {slot_id}")
        records[slot_id] = unescape_latex(raw)
        position = index


def escape_latex(content: str, *, inline: bool = False) -> str:
    result: list[str] = []
    for char in content:
        mapped = None
        for source, encoded in ESCAPES:
            if char == source:
                mapped = encoded
                break
        result.append(mapped if mapped is not None else char)
    text = "".join(result)
    if inline:
        for source, encoded in INLINE_ESCAPES:
            text = text.replace(source, encoded)
    return text


def unescape_latex(content: str) -> str:
    return UNESCAPE_RE.sub(lambda match: UNESCAPES[match.group(0)], content)


class LatexPresenter:
    KEY_LABELS = {
        "id": "Identifier",
        "name": "Name",
        "title": "Title",
        "term": "Term",
        "definition": "Definition",
        "meaning": "Meaning",
        "description": "Description",
        "purpose": "Purpose",
        "statement": "Statement",
        "condition": "Condition",
        "label": "Label",
        "kind": "Kind",
        "scope": "Scope",
        "status": "Status",
        "type": "Type",
        "cardinality": "Cardinality",
        "required": "Required",
        "trigger": "Trigger",
        "context": "Context",
        "inputs": "Inputs",
        "outputs": "Outputs",
        "results": "Results",
        "effects": "Effects",
        "failures": "Failures",
        "guarantees": "Guarantees",
        "flow_refs": "Flow references",
        "applies_to": "Applies to",
        "criterion": "Verifiable criterion",
        "verification": "Verification",
        "metric": "Metric",
        "measurement": "Measurement",
        "notes": "Notes",
        "caption": "Caption",
        "alt": "Alternative text",
        "embedded_text": "Text present in the image",
        "variants": "Variants",
        "drawing_source": "Drawing source",
        "nodes": "Nodes",
        "edges": "Edges",
        "requirements": "Requirements",
        "actor": "Actor",
        "permission": "Permission",
        "entity": "Entity",
        "tool": "Tool",
        "operation": "Operation",
        "use_case": "Use case",
        "validations": "Validations",
        "examples": "Examples",
        "data": "Data",
        "flow": "Flow",
        "statement": "Statement",
    }

    def __init__(self, payload: dict, table, full_payload: dict | None = None):
        # ``payload`` is the structural skeleton (text members are @text slots).
        self.payload = payload
        self.full_payload = full_payload or payload
        self.skeleton = table.skeleton
        self.texts = table.texts
        self.used: set[str] = set()
        self.parts: list[str] = []
        self.resource_by_id = {r["id"]: r for r in payload["resources"]}
        self.full_graph_by_id = {g["id"]: g for g in self.full_payload["graphs"]}

    # -- text records ----------------------------------------------------
    def t(self, node: dict) -> tuple[str, str]:
        slot = node["@text"]
        if slot in self.used:
            raise AtlasError(
                Diagnostic(
                    "ATL-E-PRESENTATION-DUPLICATE",
                    f"text record {slot} rendered twice",
                )
            )
        self.used.add(slot)
        return slot, self.texts[slot]

    def text_env(self, node: dict, env: str = "atlastext", *, level: int | None = None, inline: bool = False) -> str:
        slot, content = self.t(node)
        escaped = escape_latex(content, inline=inline)
        if env == "atlasheading":
            return (
                f"\\begin{{atlasheading}}{{{slot}}}{{{level or 2}}}\n"
                + escaped
                + "\n\\end{atlasheading}\n"
            )
        return f"\\begin{{{env}}}{{{slot}}}\n" + escaped + f"\n\\end{{{env}}}\n"

    def cell(self, node: dict) -> str:
        slot, content = self.t(node)
        return f"\\AtlasCell{{{slot}}}{{{escape_latex(content, inline=True)}}}"

    # -- top level -------------------------------------------------------
    def render(self) -> str:
        p = self.parts
        p.append(
            f"% atlas:latex profile=atlas-latex representation={VERSION} "
            f"translator={TRANSLATOR}\n"
        )
        p.append(
            "% Atlas LaTeX. Text records are authoritative for prose; the structure\n"
            "% appendix is authoritative for non-text data. Derived environments are\n"
            "% checked against both sources when the file is imported.\n"
        )
        p.append(_PREAMBLE)
        meta = self.payload
        p.append("\\begin{document}\n")
        p.append(
            "\\AtlasBeginCover{"
            + _escape_plain(meta["document_id"])
            + "}{"
            + _escape_plain(meta["revision"])
            + "}{"
            + _escape_plain(meta["status"])
            + "}\n"
        )
        p.append(self.text_env(meta["title"], "atlastitle"))
        if meta.get("subtitle") is not None:
            p.append(self.text_env(meta["subtitle"], "atlastext"))
        p.append("\\AtlasEndCover\n")
        p.append(self._metadata())
        for section in meta["structure"]:
            level = min(section["level"] + 1, 6)
            p.append(self.text_env(section["title"], "atlasheading", level=level))
            p.append(self._blocks(section["blocks"]))
            by_id = self._elements_by_id()
            for element_id in section["items"]:
                kind, element = by_id[element_id]
                p.append(
                    f"\\AtlasSubheading{{{kind.replace('_', ' ').upper()} "
                    f"\\texttt{{{element['id']}}}}}\n"
                )
                p.append(self._object(element))
        p.append(self._appendices())
        p.append(self._derived_summary())
        p.append(self._structure_appendix())
        unused = sorted(set(self.texts) - self.used)
        if unused:
            p.append("\\AtlasSubheading{Unplaced text records}\n")
            for slot in unused:
                p.append(self.text_env({"@text": slot}, "atlastext"))
        p.append("\\end{document}\n")
        return "".join(p)

    def _metadata(self) -> str:
        meta = self.payload
        p = ["\\AtlasMetaLine{Document}{" + _verb(meta["document_id"]) + "}\n"]
        p.append("\\AtlasMetaLine{Revision}{" + _verb(meta["revision"]) + "}\n")
        p.append("\\AtlasMetaLine{Status}{" + _verb(meta["status"]) + "}\n")
        p.append("\\AtlasMetaLine{Language}{" + _verb(meta["language"]) + "}\n")
        p.append("\\AtlasMetaLine{Atlas version}{" + _verb(meta["spec_version"]) + "}\n")
        p.append("\\AtlasMetaLine{Profile version}{" + _verb(meta["profile_version"]) + "}\n")
        p.append("\\AtlasMetaLine{Translator}{" + _verb(meta["translator_version"]) + "}\n")
        p.append("\\AtlasMetaLine{Created}{" + _verb(meta["created"]) + "}\n")
        p.append("\\AtlasMetaLine{Updated}{" + _verb(meta["updated"]) + "}\n")
        p.append("\\AtlasLabel{Authors}\n")
        for author in meta["authors"]:
            p.append(self.text_env(author["name"], "atlasitem"))
            if "role" in author:
                p.append(self.text_env(author["role"], "atlastext"))
            if "contact" in author:
                p.append(self.text_env(author["contact"], "atlastext"))
        if meta.get("keywords"):
            p.append("\\AtlasLabel{Keywords}\n")
            for keyword in meta["keywords"]:
                p.append(self.text_env(keyword, "atlasitem"))
        if meta.get("notes"):
            p.append("\\AtlasLabel{Document notes}\n")
            p.append(self._blocks(meta["notes"]))
        return "".join(p)

    def _elements_by_id(self) -> dict[str, tuple[str, dict]]:
        mapping = {
            "actor": "actors",
            "term": "vocabulary",
            "type": "types",
            "entity": "entities",
            "tool": "tools",
            "use_case": "use_cases",
            "boundary": "boundaries",
        }
        result: dict[str, tuple[str, dict]] = {}
        for kind, key in mapping.items():
            for element in self.payload[key]:
                result[element["id"]] = (kind, element)
        return result

    # -- generic structural renderer ------------------------------------
    def _object(self, value: dict) -> str:
        p: list[str] = []
        for key, item in value.items():
            if key in {"id", "@text", "extensions"}:
                continue
            p.append(self._field(key, item))
        return "".join(p)

    def _field(self, key: str, value: Any) -> str:
        label = self.KEY_LABELS.get(key, key.replace("_", " ").capitalize())
        p: list[str] = []
        if key in {"data", "meta"}:
            # Literal keys such as @text/id in arbitrary domain data must not
            # be interpreted as codec records or Atlas identities.
            import json

            data_lines = json.dumps(value, ensure_ascii=False, indent=2).splitlines()
            p.append(f"\\AtlasLabel{{{label}}}\n\\begin{{quote}}\\small\\ttfamily\\raggedright\n")
            for line in data_lines:
                p.append("\\noindent " + _escape_plain(line) + "\\par\n")
            p.append("\\end{quote}\n")
            block = "".join(p)
            if sum(max(1, (len(line) + 59) // 60) for line in data_lines) <= 20:
                return "\\par\\noindent\\begin{minipage}{\\linewidth}\n" + block + "\\end{minipage}\\par\n"
            return block
        block_types = {
            "paragraph", "note", "quote", "heading", "list", "code",
            "formula", "figure", "table",
        }
        if isinstance(value, dict) and value.get("type") in block_types:
            p.append(f"\\AtlasLabel{{{label}}}\n")
            p.append(self._block(value))
            return "".join(p)
        if isinstance(value, dict) and "@text" in value:
            p.append(f"\\AtlasLabel{{{label}}}\n")
            p.append(self.text_env(value, "atlastext"))
            return "".join(p)
        if isinstance(value, list) and value and all(
            isinstance(v, dict) and v.get("type") in block_types for v in value
        ):
            p.append(f"\\AtlasLabel{{{label}}}\n")
            p.append(self._blocks(value))
            return "".join(p)
        if isinstance(value, list) and value and all(
            isinstance(v, dict) and "@text" in v for v in value
        ):
            p.append(f"\\AtlasLabel{{{label}}}\n")
            for item in value:
                p.append(self.text_env(item, "atlasitem"))
            return "".join(p)
        if isinstance(value, list):
            if not value:
                p.append(f"\\AtlasMetaLine{{{label}}}{{none}}\n")
            elif all(not isinstance(v, (dict, list)) for v in value):
                p.append(
                    f"\\AtlasMetaLine{{{label}}}{{"
                    + _escape_plain(", ".join(_scalar(v) for v in value))
                    + "}\n"
                )
            elif all(isinstance(v, dict) and "id" in v for v in value):
                p.append(f"\\AtlasLabel{{{label}}}\n")
                for item in value:
                    p.append(f"\\AtlasSubheading{{\\texttt{{{_escape_plain(item['id'])}}}}}\n")
                    p.append(self._object(item))
            else:
                p.append(f"\\AtlasLabel{{{label}}}\n")
                for item in value:
                    p.append(self._value(item))
            return "".join(p)
        if isinstance(value, dict):
            p.append(f"\\AtlasLabel{{{label}}}\n")
            p.append(self._object(value))
            return "".join(p)
        p.append(f"\\AtlasMetaLine{{{label}}}{{{_escape_plain(_scalar(value))}}}\n")
        return "".join(p)

    def _value(self, value: Any) -> str:
        if isinstance(value, dict):
            if "@text" in value:
                return self.text_env(value, "atlastext")
            if value.get("type") in {
                "paragraph",
                "note",
                "quote",
                "heading",
                "list",
                "code",
                "formula",
                "figure",
                "table",
            }:
                return self._block(value)
            return self._object(value)
        if isinstance(value, list):
            return "".join(self._value(item) for item in value)
        return "\\AtlasMetaLine{}{" + _escape_plain(_scalar(value)) + "}\n"

    def _blocks(self, blocks: list[dict]) -> str:
        return "".join(self._block(block) for block in blocks)

    def _block(self, block: dict) -> str:
        btype = block["type"]
        if btype in {"paragraph", "note", "quote"}:
            return self.text_env(block, f"atlas{btype}")
        if btype == "heading":
            return self.text_env(block, "atlasheading", level=block["level"])
        if btype == "list":
            return self._list(block["items"])
        if btype == "code":
            return self.text_env(block, "atlascode")
        if btype == "formula":
            return self.text_env(block, "atlasformula")
        if btype == "figure":
            p = [
                "\\begin{figure}[htbp]\n\\centering\n",
                self._figure(block["resource"]),
                "\\end{figure}\n",
            ]
            if "caption" in block:
                p.append(self.text_env(block["caption"], "atlastext"))
            if "alt" in block:
                p.append("\\AtlasMetaLine{Alternative text}{}\n")
                p.append(self.text_env(block["alt"], "atlastext"))
            return "".join(p)
        if btype == "table":
            columns = block["columns"]
            count = max(1, len(columns))
            # Each column's two tabcolsep paddings are included in the width
            # budget. Paragraph columns wrap prose; longtable can break between
            # rows. Header source occurs once, so repeated PDF headers do not
            # create duplicate authoritative text slots during import.
            width = rf"\dimexpr\linewidth/{count}-2\tabcolsep\relax"
            spec = (r">{\raggedright\arraybackslash}p{" + width + "}") * count
            p = [
                "\\par\\begingroup\\small\n",
                "\\setlength{\\LTleft}{0pt}\\setlength{\\LTright}{0pt plus 1fill}\n",
                "\\begin{longtable}{" + spec + "}\n\\toprule\n",
                "\\rowcolor{AtlasTint}\n",
            ]
            p.append(
                " & ".join(
                    "\\color{AtlasInk}\\bfseries " + self.cell(column)
                    for column in columns
                )
                + " \\\\\n\\midrule\n\\endhead\n\\bottomrule\n\\endfoot\n"
            )
            for row in block["rows"]:
                p.append(
                    " & ".join(self.cell(cell) for cell in row)
                    + " \\\\\n\\addlinespace[0.35em]\n"
                )
            p.append("\\end{longtable}\n\\endgroup\n")
            if "caption" in block:
                p.append(self.text_env(block["caption"], "atlastext"))
            return "".join(p)
        raise AtlasError(Diagnostic("ATL-E-BLOCK", f"unsupported block type {btype!r}"))

    def _list(self, items: list[dict]) -> str:
        p: list[str] = []
        for item in items:
            p.append(self.text_env(item, "atlasitem"))
            if item.get("children"):
                p.append("\\begin{quote}\n")
                p.append(self._list(item["children"]))
                p.append("\\end{quote}\n")
        return "".join(p)

    def _figure(self, resource_id: str) -> str:
        resource = self.resource_by_id.get(resource_id)
        if not resource:
            return "\\AtlasMetaLine{Missing resource}{" + _escape_plain(resource_id) + "}\n"
        candidates = [(v["path"], v["media_type"]) for v in resource.get("variants", [])]
        candidates.append((resource["path"], resource["media_type"]))
        chosen = None
        for path, media_type in candidates:
            if media_type in {"application/pdf", "image/png", "image/jpeg"}:
                chosen = path
                break
        if chosen is None:
            raise AtlasError(
                Diagnostic(
                    "ATL-E-LATEX-RESOURCE",
                    f"resource {resource_id} has no PDF or bitmap variant usable by LaTeX; "
                    "generate a publication variant and record it in the catalog",
                )
            )
        width = self.payload.get("presentation", {}).get("latex", {}).get("figure_width", "0.8\\linewidth")
        return f"\\includegraphics[width={width}]{{{_escape_plain(chosen, wrap=False)}}}\n"

    # -- appendices ------------------------------------------------------
    def _appendices(self) -> str:
        p: list[str] = []
        if self.payload["graphs"]:
            p.append("\\AtlasAppendixHeading{Appendix: graphs}\n")
            for graph in self.payload["graphs"]:
                p.append(f"\\AtlasSubheading{{Graph \\texttt{{{_escape_plain(graph['id'])}}}}}\n")
                p.append(self.text_env(graph["title"], "atlastext"))
                p.append(
                    f"\\AtlasMetaLine{{Kind}}{{{_escape_plain(graph['kind'])}}}\n"
                )
                p.append("\\AtlasLabel{Nodes}\n")
                for node in graph["nodes"]:
                    p.append(
                        f"\\AtlasSubheading{{Node \\texttt{{{_escape_plain(node['id'])}}} "
                        f"({_escape_plain(node['type'])})}}\n"
                    )
                    p.append(self.text_env(node["label"], "atlastext"))
                    if node.get("call"):
                        p.append(
                            "\\AtlasMetaLine{Call}{"
                            + _escape_plain(node["call"]["kind"])
                            + " \\texttt{"
                            + _escape_plain(node["call"]["id"])
                            + "}}\n"
                        )
                    for key in ("inputs", "outputs", "requirement_refs", "details"):
                        if node.get(key):
                            p.append(self._field(key, node[key]))
                p.append("\\AtlasLabel{Edges}\n")
                for edge in graph["edges"]:
                    p.append(
                        f"\\AtlasSubheading{{Edge \\texttt{{{_escape_plain(edge['id'])}}}: "
                        f"\\texttt{{{_escape_plain(edge['from'])}}} $\\rightarrow$ "
                        f"\\texttt{{{_escape_plain(edge['to'])}}}}}\n"
                    )
                    for key in ("label", "condition", "requirement_refs", "priority"):
                        if key in edge:
                            p.append(self._field(key, edge[key]))
                if graph.get("notes"):
                    p.append(self._field("notes", graph["notes"]))
                p.append(self._derived_env(f"DERIVED-GRAPH-{graph['id']}", _graph_topology(graph)))
                full_graph = self.full_graph_by_id[graph["id"]]
                p.append(
                    f"% atlas:tikz:begin id=TIKZ-{graph['id']}\n"
                    + render_tikz(full_graph)
                    + f"\n% atlas:tikz:end id=TIKZ-{graph['id']}\n"
                )
        if self.payload["resources"]:
            p.append("\\AtlasAppendixHeading{Appendix: resources}\n")
            for resource in self.payload["resources"]:
                p.append(
                    f"\\AtlasSubheading{{Resource \\texttt{{{_escape_plain(resource['id'])}}}}}\n"
                )
                p.append(
                    "\\AtlasMetaLine{Path}{\\texttt{"
                    + _escape_plain(resource["path"])
                    + "}}\n"
                )
                p.append(
                    "\\AtlasMetaLine{Media type}{"
                    + _escape_plain(resource["media_type"])
                    + "}\n"
                )
                p.append(
                    "\\AtlasMetaLine{SHA-256}{\\texttt{"
                    + _escape_plain(resource["sha256"])
                    + "}}\n"
                )
                for key in ("source_uri", "drawing_source", "derived_from_graph", "caption", "alt", "embedded_text", "variants"):
                    if key in resource and resource[key] not in (None, "", [], {}):
                        p.append(self._field(key, resource[key]))
        for key, title in (
            ("assumptions", "assumptions"),
            ("decisions", "decisions"),
            ("open_issues", "open issues"),
            ("sources", "sources"),
            ("history", "history"),
        ):
            if self.payload[key]:
                p.append(f"\\AtlasAppendixHeading{{Appendix: {title}}}\n")
                for item in self.payload[key]:
                    p.append(
                        f"\\AtlasSubheading{{\\texttt{{{_escape_plain(item['id'])}}}}}\n"
                    )
                    p.append(self._object(item))
        return "".join(p)

    def _derived_summary(self) -> str:
        return self._derived_env("DERIVED-SUMMARY", _summary(self.payload))

    def _derived_env(self, derived_id: str, content: str) -> str:
        block = (
            f"\\begin{{atlasderived}}{{{derived_id}}}\n"
            + escape_latex(content)
            + "\n\\end{atlasderived}\n"
        )
        estimated_lines = sum(max(1, (len(line) + 71) // 72) for line in content.splitlines())
        if derived_id.startswith("DERIVED-GRAPH-") and estimated_lines <= 45:
            return "\\par\\noindent\\begin{minipage}{\\linewidth}\n" + block + "\\end{minipage}\\par\n"
        return block

    def _structure_appendix(self) -> str:
        import json

        text = json.dumps(self.skeleton, ensure_ascii=False, indent=2)
        commented = "\n".join("% " + line for line in text.splitlines())
        return (
            "%\n"
            + STRUCTURE_BEGIN
            + "\n"
            + commented
            + "\n"
            + STRUCTURE_END
            + "\n"
        )


def _verb(value: str) -> str:
    return "\\texttt{" + _escape_plain(value) + "}"


def _escape_plain(value: str, *, wrap: bool = True) -> str:
    mapping = {
            "\\": r"\textbackslash{}",
            "{": r"\{",
            "}": r"\}",
            "%": r"\%",
            "#": r"\#",
            "&": r"\&",
            "_": r"\_",
            "$": r"\$",
            "^": r"\textasciicircum{}",
            "~": r"\textasciitilde{}",
        }
    pieces: list[str] = []
    token_length = 0
    for char in str(value):
        pieces.append(mapping.get(char, char))
        token_length = token_length + 1 if char.isalnum() else 0
        if wrap and (char in "/-_.:?#=&\\" or token_length >= 16):
            # Structural scalar views (URLs, hashes and IDs) can wrap without
            # inserting a printed hyphen or modifying the authoritative data.
            pieces.append(r"\allowbreak{}")
            token_length = 0
    return "".join(pieces)


def _scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage{iftex}
\ifPDFTeX
  \usepackage[utf8]{inputenc}
  \usepackage[T1]{fontenc}
\else
  \usepackage{fontspec}
\fi
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage[hidelinks]{hyperref}
\usepackage{atlas}
% Optional publication-only settings. The Atlas decoder does not read this file.
\InputIfFileExists{atlas-presentation.tex}{}{}
"""


def _summary(payload: dict) -> str:
    return (
        f"Derived summary: {len(payload['structure'])} sections; "
        f"{len(payload['actors'])} actors; {len(payload['entities'])} entities; "
        f"{len(payload['tools'])} tools; {len(payload['use_cases'])} use cases; "
        f"{len(payload['boundaries'])} boundaries; {len(payload['graphs'])} graphs; "
        f"{len(payload['resources'])} resources."
    )


def _graph_topology(graph: dict) -> str:
    lines = [f"Topology of {graph['id']}:", "", "Nodes:"]
    for node in graph["nodes"]:
        lines.append(f"- {node['id']} ({node['type']})")
    lines.append("")
    lines.append("Edges:")
    if graph["edges"]:
        for edge in graph["edges"]:
            lines.append(f"- {edge['id']}: {edge['from']} -> {edge['to']}")
    else:
        lines.append("- none")
    return "\n".join(lines)


def encode_latex(document: dict, *, options: EncodeOptions) -> str:
    payload = document["atlas"]
    table = externalize(payload)
    presenter = LatexPresenter(table.skeleton, table, payload)
    return presenter.render()
