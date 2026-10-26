"""Atlas Markdown adapter.

The readable body carries every text record once, delimited by Atlas comments.
A structure appendix carries all non-text data with ``@text`` placeholders.
Both sources are required: text is never read from the appendix and structure
is never guessed from prose.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from ..errors import AtlasError, AtlasParseError, AtlasVersionError, Diagnostic
from ..slots import externalize, restore
from ..util import (
    decode_text_exact,
    sha256_text,
    split_lines_keepends,
    strict_json_loads,
    strip_line_ending,
    write_text_exact,
)
from .base import Adapter, DecodeOptions, EncodeOptions

PROFILE = "atlas-markdown"
VERSION = "Alpha-v0.1.0"
TRANSLATOR = "0.1.0"

HEADER_RE = re.compile(
    r"^<!-- atlas:markdown profile=atlas-markdown representation=(?P<version>\S+) "
    r"translator=(?P<translator>\S+) -->$"
)
TEXT_START_RE = re.compile(r"^<!-- atlas:text (?P<attrs>[^>]*) -->$")
TEXT_END_RE = re.compile(r"^<!-- /atlas:text id=(?P<id>T[0-9]{6}) -->$")
DERIVED_START_RE = re.compile(r"^<!-- atlas:derived id=(?P<id>[A-Z][A-Z0-9-]*) -->$")
DERIVED_END_RE = re.compile(r"^<!-- /atlas:derived id=(?P<id>[A-Z][A-Z0-9-]*) -->$")
STRUCTURE_BEGIN = "<!-- atlas:structure:begin -->"
STRUCTURE_END = "<!-- atlas:structure:end -->"
STRUCTURE_FENCE_RE = re.compile(r"^(?P<fence>`{3,})atlas-structure$")
ATLAS_LIKE_RE = re.compile(r"^(?P<slashes>\\*)(?P<marker><!-- /?atlas:.*)$")


class MarkdownAdapter(Adapter):
    format_name = "markdown"

    def decode(self, source: str | bytes | Path, options: DecodeOptions) -> dict:
        text, source_path = self._read_source(source)
        return decode_markdown(text, source_path=source_path, options=options)

    def encode(self, document: dict, options: EncodeOptions) -> str:
        return encode_markdown(document, options=options)

    # -- adapter helpers -------------------------------------------------
    def _read_source(self, source: str | bytes | Path) -> tuple[str, Path | None]:
        if isinstance(source, Path):
            return decode_text_exact(source.read_bytes(), location=str(source)), source
        if isinstance(source, bytes):
            return decode_text_exact(source, location="<bytes>"), None
        return source, None


def decode_markdown(
    text: str, *, source_path: Path | None = None, options: DecodeOptions | None = None
) -> dict:
    options = options or DecodeOptions()
    lines = split_lines_keepends(text)
    records: dict[str, str] = {}
    record_roles: dict[str, dict[str, str]] = {}
    derived: dict[str, str] = {}
    structure_json: str | None = None
    header_seen = False
    seen_ids: set[str] = set()
    state = "normal"
    text_id: str | None = None
    text_role: dict[str, str] = {}
    content_lines: list[str] = []
    derived_id: str | None = None
    structure_fence: str | None = None
    structure_lines: list[str] = []
    line_number = 0

    def malformed(message: str) -> AtlasParseError:
        return AtlasParseError(
            Diagnostic("ATL-E-MARKDOWN", message, f"{source_path or '<markdown>'}:{line_number}")
        )

    def finish_text() -> None:
        nonlocal content_lines, text_id, text_role
        assert text_id is not None
        raw = "".join(content_lines)
        if raw:
            _, eol = strip_line_ending(content_lines[-1])
            if eol:
                raw = raw[: -len(eol)]
        if text_id in records:
            raise malformed(f"duplicate text record {text_id}")
        value = _unescape_markdown_lines(raw, malformed)
        role = text_role.get("role")
        if role == "heading":
            try:
                level = int(text_role.get("level", "2"))
            except ValueError as exc:
                raise malformed("heading text record has a non-numeric level") from exc
            prefix = "#" * level + " "
            if not value.startswith(prefix):
                raise malformed(
                    f"heading text record {text_id} must start with its Markdown "
                    f"prefix {prefix!r}"
                )
            value = value[len(prefix) :]
        elif role == "list-item":
            if value.startswith("- "):
                value = value[2:]
            elif value.startswith("1. "):
                value = value[3:]
            else:
                raise malformed(
                    f"list-item text record {text_id} must start with '- ' or '1. '"
                )
        records[text_id] = value
        record_roles[text_id] = text_role
        content_lines = []
        text_id = None
        text_role = {}

    for line in lines:
        line_number += 1
        body, _eol = strip_line_ending(line)
        if state == "text":
            end_match = TEXT_END_RE.match(body)
            if end_match:
                if end_match.group("id") != text_id:
                    raise malformed(
                        f"text record {text_id} closed by {end_match.group('id')}"
                    )
                finish_text()
                state = "normal"
                continue
            if TEXT_START_RE.match(body):
                raise malformed(f"nested text record inside {text_id}")
            content_lines.append(line)
            continue
        if state == "derived":
            end_match = DERIVED_END_RE.match(body)
            if end_match:
                if end_match.group("id") != derived_id:
                    raise malformed(
                        f"derived region {derived_id} closed by {end_match.group('id')}"
                    )
                raw = "".join(content_lines)
                if raw:
                    _, eol = strip_line_ending(content_lines[-1])
                    if eol:
                        raw = raw[: -len(eol)]
                derived[derived_id] = raw
                content_lines = []
                derived_id = None
                state = "normal"
                continue
            if DERIVED_START_RE.match(body):
                raise malformed("nested derived region")
            if TEXT_START_RE.match(body):
                raise malformed("text records are not allowed inside derived regions")
            content_lines.append(line)
            continue
        if state == "structure":
            assert structure_fence is not None
            if body == structure_fence:
                structure_json = "".join(structure_lines)
                state = "after_structure"
                continue
            structure_lines.append(line)
            continue
        if state == "after_structure":
            if body == STRUCTURE_END:
                state = "normal"
                continue
            if not body.strip():
                continue
            raise malformed("expected the end of the Atlas structure appendix")

        if body == STRUCTURE_BEGIN:
            if structure_json is not None:
                raise malformed("the structure appendix appears more than once")
            state = "structure_header"
            continue
        if state == "structure_header":
            match = STRUCTURE_FENCE_RE.match(body)
            if match:
                structure_fence = match.group("fence")
                state = "structure"
                continue
            if not body.strip():
                continue
            raise malformed("expected an atlas-structure fenced block")
        text_match = TEXT_START_RE.match(body)
        if text_match:
            attrs = _parse_attrs(text_match.group("attrs"), malformed)
            if "id" not in attrs:
                raise malformed("text record without an id")
            text_id = attrs["id"]
            text_role = {k: v for k, v in attrs.items() if k != "id"}
            if not re.fullmatch(r"T[0-9]{6}", text_id):
                raise malformed(f"invalid text record id {text_id!r}")
            if text_id in seen_ids:
                raise malformed(f"text record {text_id} starts more than once")
            seen_ids.add(text_id)
            content_lines = []
            state = "text"
            continue
        derived_match = DERIVED_START_RE.match(body)
        if derived_match:
            derived_id = derived_match.group("id")
            content_lines = []
            state = "derived"
            continue
        header_match = HEADER_RE.match(body)
        if header_match:
            if header_seen:
                raise malformed("duplicate Atlas Markdown header")
            header_seen = True
            if header_match.group("version") != VERSION:
                raise AtlasVersionError(
                    Diagnostic(
                        "ATL-E-VERSION",
                        f"Atlas Markdown version {header_match.group('version')!r} is not "
                        f"supported; this translator implements {VERSION!r}",
                        f"{source_path or '<markdown>'}:{line_number}",
                    )
                )
            continue
        if body.startswith("<!-- atlas:") or body.startswith("<!-- /atlas:"):
            raise malformed(f"unknown or misplaced Atlas marker: {body}")
        if state == "structure_header":
            continue

    if state == "text":
        raise malformed(f"unterminated text record {text_id}")
    if state == "derived":
        raise malformed(f"unterminated derived region {derived_id}")
    if state in {"structure", "structure_header", "after_structure"}:
        raise malformed("unterminated structure appendix")
    if not header_seen:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-MARKDOWN-HEADER",
                "missing Atlas Markdown header; the first structural line must identify "
                "the profile and representation version",
                str(source_path) if source_path else "<markdown>",
            )
        )
    if structure_json is None:
        raise malformed("missing Atlas structure appendix")
    structure = strict_json_loads(structure_json, location="Atlas structure appendix")
    if not isinstance(structure, dict):
        raise malformed("Atlas structure appendix must contain a JSON object")
    payload = restore(structure, records)

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
                    "regenerate the representation with 'atlas convert'. Do not edit "
                    "derived presentation in place.",
                )
            )
    document = {"format": f"atlas-json/{VERSION}", "atlas": payload}
    result = options.validator.validate(
        document,
        resource_root=options.resource_root or (source_path.parent if source_path else None),
        check_resources=options.check_resources,
    )
    return document


def _parse_attrs(attrs: str, malformed) -> dict[str, str]:
    result: dict[str, str] = {}
    for token in attrs.split():
        if "=" not in token:
            raise malformed(f"malformed text record attribute {token!r}")
        key, value = token.split("=", 1)
        if key in result:
            raise malformed(f"duplicate text record attribute {key!r}")
        result[key] = value
    return result


def _escape_markdown_lines(content: str) -> str:
    lines = split_lines_keepends(content)
    result: list[str] = []
    for line in lines:
        body, eol = strip_line_ending(line)
        if ATLAS_LIKE_RE.match(body):
            body = "\\" + body
        result.append(body + eol)
    return "".join(result)


def _unescape_markdown_lines(content: str, malformed) -> str:
    lines = split_lines_keepends(content)
    result: list[str] = []
    for line in lines:
        body, eol = strip_line_ending(line)
        match = ATLAS_LIKE_RE.match(body)
        if match:
            body = body[1:]
        result.append(body + eol)
    return "".join(result)


class MarkdownPresenter:
    def __init__(self, payload: dict, table):
        # ``payload`` is the structural skeleton: text members are @text slots.
        self.payload = payload
        self.skeleton = table.skeleton
        self.texts = table.texts
        self.used: set[str] = set()
        self.parts: list[str] = []

    def t(self, node: dict) -> str:
        slot = node["@text"]
        if slot in self.used:
            raise AtlasError(
                Diagnostic(
                    "ATL-E-PRESENTATION-DUPLICATE",
                    f"text record {slot} rendered twice",
                )
            )
        self.used.add(slot)
        return self.texts[slot]

    def record(self, node: dict, role: str, *, level: int | None = None, ordered: bool = False) -> str:
        slot = node["@text"]
        content = self.t(node)
        if role == "heading":
            body = "#" * (level or 2) + " " + content
        elif role == "list-item":
            body = ("1. " if ordered else "- ") + content
        else:
            body = content
        attrs = f"id={slot} role={role}"
        if level is not None:
            attrs += f" level={level}"
        if role == "list-item":
            attrs += f" ordered={'yes' if ordered else 'no'}"
        # A bare final CR followed by LF would become one CRLF, which the
        # reader removes as structural syntax. CR + CRLF keeps them distinct.
        ending = "\r\n" if body.endswith("\r") else "\n"
        return (
            "\n"
            + f"<!-- atlas:text {attrs} -->\n"
            + _escape_markdown_lines(body)
            + ending + "<!-- /atlas:text id="
            + slot
            + " -->\n"
        )

    def render(self) -> str:
        p = self.parts
        meta = self.payload
        p.append(
            f"<!-- atlas:markdown profile=atlas-markdown representation={VERSION} "
            f"translator={TRANSLATOR} -->\n"
        )
        p.append(
            "<!-- Atlas Markdown. Text records below are authoritative for prose. "
            "The structure appendix is authoritative for non-text data. -->\n\n"
        )
        p.append(self.record(meta["title"], "heading", level=1))
        p.append("\n")
        if meta.get("subtitle") is not None:
            p.append(self.record(meta["subtitle"], "paragraph"))
            p.append("\n")
        p.append(self._render_metadata(meta))
        for section in meta["structure"]:
            p.append(self._render_section(section))
        p.extend(self._render_graphs())
        p.extend(self._render_resources())
        p.extend(self._render_records())
        p.extend(self._render_extensions())
        p.append(self._render_derived_summary())
        p.append(self._render_structure_appendix())
        unused = sorted(set(self.texts) - self.used)
        if unused:
            p.append("\n## Appendix: unplaced text records\n\n")
            p.append(
                "This appendix is a safety net. A well-formed presentation places every "
                "record in context.\n\n"
            )
            for slot in unused:
                p.append(self.record({"@text": slot}, "paragraph"))
                p.append("\n")
        return "".join(p)

    def _render_metadata(self, meta: dict) -> str:
        p: list[str] = []
        p.append("## Document metadata\n\n")
        p.append(
            f"**Document:** `{meta['document_id']}` · **Revision:** {meta['revision']} · "
            f"**Status:** {meta['status']} · **Language:** {meta['language']}\n\n"
        )
        p.append(
            f"**Atlas specification:** {meta['spec_version']} · "
            f"**Profile:** {meta['profile_version']} · "
            f"**Translator:** {meta['translator_version']}\n\n"
        )
        p.append(f"**Created:** {meta['created']} · **Updated:** {meta['updated']}\n\n")
        p.append("**Authors**\n\n")
        for author in meta["authors"]:
            p.append(self.record(author["name"], "list-item"))
            if "role" in author:
                p.append(self.record(author["role"], "paragraph"))
            if "contact" in author:
                p.append(self.record(author["contact"], "paragraph"))
            p.append("\n")
        if meta.get("keywords"):
            p.append("**Keywords:**\n\n")
            for keyword in meta["keywords"]:
                p.append(self.record(keyword, "list-item"))
            p.append("\n")
        if meta.get("notes"):
            p.append("**Document notes**\n\n")
            p.append(self._blocks(meta["notes"]))
        return "".join(p)

    def _render_section(self, section: dict) -> str:
        p: list[str] = []
        level = min(section["level"] + 1, 6)
        p.append(self.record(section["title"], "heading", level=level))
        p.append("\n")
        p.append(self._blocks(section["blocks"]))
        by_id = self._elements_by_id()
        for element_id in section["items"]:
            kind, element = by_id[element_id]
            p.append(self._render_element(kind, element))
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

    def _render_element(self, kind: str, element: dict) -> str:
        p: list[str] = []
        p.append(f"\n### {kind.replace('_', ' ').upper()} `{element['id']}`\n\n")
        renderer = getattr(self, f"_render_{kind}")
        p.append(renderer(element))
        p.append("\n")
        return "".join(p)

    # -- concrete element renderers -------------------------------------
    def _render_actor(self, actor: dict) -> str:
        p = [f"**Kind:** {actor['kind']}\n\n", "**Name**\n\n", self.record(actor["name"], "paragraph")]
        p.append("\n**Description**\n\n")
        p.append(self._blocks(actor["description"]))
        return "".join(p)

    def _render_term(self, term: dict) -> str:
        p = ["**Term**\n\n", self.record(term["term"], "paragraph")]
        if term.get("synonyms"):
            p.append("\n**Synonyms**\n\n")
            for synonym in term["synonyms"]:
                p.append(self.record(synonym, "list-item"))
        p.append("\n**Definition**\n\n")
        p.append(self._blocks(term["definition"]))
        return "".join(p)

    def _render_type(self, definition: dict) -> str:
        p = ["**Name**\n\n", self.record(definition["name"], "paragraph")]
        p.append("\n**Definition**\n\n")
        p.append(self._blocks(definition["definition"]))
        if definition.get("constraints"):
            p.append("\n**Constraints**\n\n")
            p.append(self._blocks(definition["constraints"]))
        if definition.get("examples"):
            p.append("\n**Examples**\n\n")
            for example in definition["examples"]:
                p.append(self.record(example, "list-item"))
        return "".join(p)

    def _render_entity(self, entity: dict) -> str:
        p: list[str] = ["**Name**\n\n", self.record(entity["name"], "paragraph")]
        p.append("\n**Meaning**\n\n")
        p.append(self._blocks(entity["meaning"]))
        p.append("\n**Identity**\n\n")
        p.append(self._blocks(entity["identity"]["description"]))
        if entity["identity"]["fields"]:
            p.append("\nIdentity fields: " + ", ".join(f"`{x}`" for x in entity["identity"]["fields"]) + "\n")
        p.append("\n**Fields**\n\n")
        for field in entity["fields"]:
            p.append(f"#### Field `{field['id']}`\n\n")
            p.append(self.record(field["name"], "paragraph"))
            p.append(
                f"\n\nType `{field['type']}` · Cardinality `{field['cardinality']}` · "
                f"Required: {'yes' if field['required'] else 'no'}\n\n"
            )
            p.append(self._blocks(field["description"]))
            if field.get("constraints"):
                p.append("\n**Constraints**\n\n")
                p.append(self._blocks(field["constraints"]))
            if field.get("examples"):
                for kind, label in (("valid", "Valid examples"), ("invalid", "Invalid examples")):
                    values = field["examples"].get(kind) or []
                    if values:
                        p.append(f"\n**{label}**\n\n")
                        for value in values:
                            p.append(self.record(value, "list-item"))
        if entity["relationships"]:
            p.append("\n**Relationships**\n\n")
            for rel in entity["relationships"]:
                p.append(
                    f"#### Relationship `{rel['id']}` → `{rel['target']}`\n\n"
                    f"Kind `{rel['kind']}` · Cardinality `{rel['cardinality']}` · "
                    f"Structural: {'yes' if rel['structural'] else 'no'}\n\n"
                )
                p.append(self._blocks(rel["description"]))
                p.append("\n")
        if entity["states"]:
            p.append("\n**States**\n\n")
            for state in entity["states"]:
                p.append(f"#### State `{state['id']}`\n\n")
                p.append(self.record(state["name"], "paragraph"))
                p.append("\n")
                p.append(self._blocks(state["description"]))
                p.append("\n")
        if entity["transitions"]:
            p.append("\n**Transitions**\n\n")
            for transition in entity["transitions"]:
                p.append(
                    f"#### Transition `{transition['id']}`: `{transition['from']}` → "
                    f"`{transition['to']}`\n\n"
                )
                if "name" in transition:
                    p.append(self.record(transition["name"], "paragraph"))
                    p.append("\n")
                p.append(self._blocks(transition["description"]))
                p.append("\n")
        if entity["validations"]:
            p.append("\n**Validations**\n\n")
            for validation in entity["validations"]:
                p.append(self._render_validation(validation))
        if entity["examples"]:
            p.append("\n**Examples**\n\n")
            for example in entity["examples"]:
                p.append(
                    f"#### Example `{example['id']}` ({example['kind']})\n\n"
                )
                p.append(self._blocks(example["description"]))
                p.append("\n**Data**\n\n```json\n")
                import json

                p.append(json.dumps(example["data"], ensure_ascii=False, indent=2))
                p.append("\n```\n\n")
        return "".join(p)

    def _render_validation(self, validation: dict) -> str:
        p: list[str] = [f"#### Validation `{validation['id']}`\n\n"]
        p.append(self.record(validation["name"], "paragraph"))
        p.append(f"\n\n**Scope:** {validation['scope']} · **Flow:** `{validation['flow']}`\n\n")
        p.append(self._blocks(validation["statement"]))
        if validation["inputs"]:
            p.append("\n**Inputs**\n\n")
            for item in validation["inputs"]:
                p.append(self.record(item["name"], "list-item"))
                p.append(f"Source `{item['source']}`\n\n")
                p.append(self._blocks(item["meaning"]))
        if validation["conditions"]:
            p.append("\n**Conditions**\n\n")
            for condition in validation["conditions"]:
                p.append(f"- `{condition['id']}` ")
                p.append(self.record(condition["condition"], "paragraph"))
                p.append("\n")
                p.append(self._blocks(condition["meaning"]))
        if validation["results"]:
            p.append("\n**Results**\n\n")
            for result in validation["results"]:
                p.append(f"- **{result['outcome']}**\n\n")
                p.append(self._blocks(result["description"]))
        if validation.get("notes"):
            p.append("\n**Notes**\n\n")
            p.append(self._blocks(validation["notes"]))
        return "".join(p)

    def _render_tool(self, tool: dict) -> str:
        p: list[str] = ["**Name**\n\n", self.record(tool["name"], "paragraph")]
        p.append("\n**Purpose**\n\n")
        p.append(self._blocks(tool["purpose"]))
        for operation in tool["operations"]:
            p.append(f"\n#### Operation `{operation['id']}`\n\n")
            p.append(self.record(operation["name"], "paragraph"))
            p.append("\n\n**Purpose**\n\n")
            p.append(self._blocks(operation["purpose"]))
            if operation["inputs"]:
                p.append("\n**Inputs**\n\n")
                for item in operation["inputs"]:
                    p.append(self.record(item["name"], "list-item"))
                    p.append(
                        f"Type `{item['type']}` · Required: "
                        f"{'yes' if item['required'] else 'no'}\n\n"
                    )
                    p.append(self._blocks(item["meaning"]))
            if operation["conditions"]:
                p.append("\n**Conditions of use**\n\n")
                p.append(self._blocks(operation["conditions"]))
            if operation["results"]:
                p.append("\n**Results**\n\n")
                for result in operation["results"]:
                    p.append(self.record(result["name"], "list-item"))
                    p.append(f"Type `{result['type']}`\n\n")
                    p.append(self._blocks(result["meaning"]))
                    if result.get("guarantees"):
                        p.append("\n*Guarantees.* ")
                        p.append(self._blocks(result["guarantees"]))
            if operation["effects"]:
                p.append("\n**Effects**\n\n")
                p.append(self._blocks(operation["effects"]))
            if operation["failures"]:
                p.append("\n**Failures**\n\n")
                for failure in operation["failures"]:
                    p.append(f"- `{failure['code']}`\n\n")
                    p.append(self._blocks(failure["meaning"]))
                    p.append("\n*Consumer distinction.* ")
                    p.append(self._blocks(failure["consumer_distinction"]))
            if operation["guarantees"]:
                p.append("\n**Guarantees**\n\n")
                p.append(self._blocks(operation["guarantees"]))
        return "".join(p)

    def _render_use_case(self, case: dict) -> str:
        p: list[str] = ["**Name**\n\n", self.record(case["name"], "paragraph")]
        p.append("\n**Objective**\n\n")
        p.append(self._blocks(case["objective"]))
        p.append("\n**Actors and permissions**\n\n")
        for actor in case["actors"]:
            p.append(f"- `{actor['actor']}` — ")
            p.append(self.record(actor["permission"], "paragraph"))
            p.append("\n")
            p.append(self._blocks(actor["description"]))
        p.append("\n**Trigger**\n\n")
        p.append(self._blocks(case["trigger"]))
        p.append("\n**Context**\n\n")
        p.append(self._blocks(case["context"]))
        if case["inputs"]:
            p.append("\n**Inputs**\n\n")
            for item in case["inputs"]:
                p.append(self.record(item["name"], "list-item"))
                p.append(
                    f"Type `{item['type']}` · Required: "
                    f"{'yes' if item['required'] else 'no'}\n\n"
                )
                p.append(self._blocks(item["meaning"]))
        p.append("\n**Entry conditions**\n\n")
        p.append(self._blocks(case["entry_conditions"]))
        if case["entities"]:
            p.append("\n**Entities and validations used**\n\n")
            for use in case["entities"]:
                p.append(f"- Entity `{use['entity']}`")
                if use["validations"]:
                    p.append(
                        "; validations "
                        + ", ".join(f"`{v}`" for v in use["validations"])
                    )
                p.append("\n\n")
                p.append(self._blocks(use["purpose"]))
        if case["tools"]:
            p.append("\n**Tools and operations used**\n\n")
            for use in case["tools"]:
                p.append(f"- Tool `{use['tool']}`, operation `{use['operation']}`\n\n")
                p.append(self._blocks(use["purpose"]))
        if case["calls"]:
            p.append("\n**Other use cases used**\n\n")
            for call in case["calls"]:
                p.append(f"- Use case `{call['use_case']}`\n\n")
                p.append("**Contract.** ")
                p.append(self._blocks(call["contract"]))
                p.append("\n**Authorization.** ")
                p.append(self._blocks(call["authorization"]))
        if case["outcomes"]:
            p.append("\n**Outcomes**\n\n")
            for outcome in case["outcomes"]:
                p.append(f"- `{outcome['id']}` — {outcome['kind']}\n\n")
                p.append(self._blocks(outcome["description"]))
                p.append("\n*Effects.* ")
                p.append(self._blocks(outcome["effects"]))
        p.append("\n**Functional requirements**\n\n")
        if not case["functional_requirements"]:
            p.append("*None declared.*\n\n")
        for rf in case["functional_requirements"]:
            p.append(f"#### `{rf['id']}`\n\n")
            p.append(self._blocks(rf["statement"]))
            p.append(
                f"\n\nScope `{rf['scope']}` · Flow refs "
                + (", ".join(f"`{x}`" for x in rf["flow_refs"]) or "none")
                + " · Applies to "
                + (", ".join(f"`{x}`" for x in rf["applies_to"]) or "none")
                + "\n\n"
            )
            if rf.get("notes"):
                p.append(self._blocks(rf["notes"]))
        p.append("\n**Non-functional requirements**\n\n")
        if not case["nonfunctional_requirements"]:
            p.append("*None declared.*\n\n")
        for rnf in case["nonfunctional_requirements"]:
            p.append(f"#### `{rnf['id']}`\n\n")
            if rnf.get("reference_to"):
                p.append(f"Reference to canonical definition `{rnf['reference_to']}`.\n\n")
            if "statement" in rnf:
                p.append(self._blocks(rnf["statement"]))
            p.append(
                f"\n\nScope `{rnf['scope']}` · Applies to "
                + (", ".join(f"`{x}`" for x in rnf["applies_to"]) or "none")
                + "\n\n"
            )
            for key, label in (
                ("applicability", "Applicability"),
                ("criterion", "Verifiable criterion"),
                ("verification", "Verification method"),
            ):
                if key in rnf:
                    p.append(f"**{label}.** ")
                    p.append(self._blocks(rnf[key]))
                    p.append("\n")
            if rnf.get("metric") is not None:
                metric = rnf["metric"]
                p.append("**Metric.** ")
                p.append(self.record(metric["name"], "paragraph"))
                p.append(" · Unit ")
                p.append(self.record(metric["unit"], "paragraph"))
                p.append(
                    f" · Target `{metric['target']}` · Operator `{metric['operator']}`\n"
                )
            if rnf.get("measurement") is not None:
                p.append("**Measurement start.** ")
                p.append(self._blocks(rnf["measurement"]["start"]))
                p.append("\n**Measurement end.** ")
                p.append(self._blocks(rnf["measurement"]["end"]))
                p.append("\n")
            if rnf.get("references"):
                p.append("**References:** " + ", ".join(f"`{x}`" for x in rnf["references"]) + "\n")
        p.append("\n**Flows**\n\n")
        p.append(f"Main: `{case['flows']['main']}`\n\n")
        if case["flows"]["subflows"]:
            p.append(
                "Subflows: "
                + ", ".join(f"`{x}`" for x in case["flows"]["subflows"])
                + "\n\n"
            )
        p.append("**Complete textual flow**\n\n")
        p.append(self._blocks(case["flow_text"]))
        p.append("\n**Acceptance criteria**\n\n")
        if not case["acceptance_criteria"]:
            p.append("*None declared.*\n\n")
        for ac in case["acceptance_criteria"]:
            p.append(f"#### `{ac['id']}`\n\n")
            p.append(self._blocks(ac["statement"]))
            p.append(
                "\n\nVerifies "
                + (", ".join(f"`{x}`" for x in ac["verifies"]) or "nothing declared")
                + "\n\n"
            )
            if ac.get("notes"):
                p.append(self._blocks(ac["notes"]))
        p.append("\n**Traceability**\n\n")
        if not case["traceability"]:
            p.append("*None declared.*\n\n")
        for trace in case["traceability"]:
            p.append(
                f"- `{trace['id']}`: `{trace['source']}` → "
                + (", ".join(f"`{x}`" for x in trace["targets"]) or "no targets")
                + "\n\n"
            )
            if trace.get("note"):
                p.append(self._blocks(trace["note"]))
        for key, label in (
            ("assumptions", "Assumptions"),
            ("sources", "Sources"),
            ("open_issues", "Open issues"),
        ):
            if case[key]:
                p.append(f"\n**{label}:** " + ", ".join(f"`{x}`" for x in case[key]) + "\n")
        return "".join(p)

    def _render_boundary(self, boundary: dict) -> str:
        p: list[str] = ["**Name**\n\n", self.record(boundary["name"], "paragraph")]
        p.append(f"\n\n**Modality:** {boundary['modality']}\n\n")
        p.append("**Purpose**\n\n")
        p.append(self._blocks(boundary["purpose"]))
        p.append("\n**Audience**\n\n")
        p.append(self._blocks(boundary["audience"]))
        for interaction in boundary["interactions"]:
            p.append(f"\n#### Interaction `{interaction['id']}`\n\n")
            p.append(self.record(interaction["name"], "paragraph"))
            p.append(f"\n\nExposes use case `{interaction['use_case']}`\n\n")
            p.append(self._blocks(interaction["description"]))
            p.append("\n**Trigger**\n\n")
            p.append(self._blocks(interaction["trigger"]))
            for key, label in (("input_mapping", "Input mapping"), ("result_mapping", "Result mapping")):
                if interaction[key]:
                    p.append(f"\n**{label}**\n\n")
                    for mapping in interaction[key]:
                        p.append(
                            f"- `{mapping['source']}` → `{mapping['target']}`\n\n"
                        )
                        p.append(self._blocks(mapping["meaning"]))
            if interaction["requirement_refs"]:
                p.append(
                    "\n**Requirements:** "
                    + ", ".join(f"`{x}`" for x in interaction["requirement_refs"])
                    + "\n"
                )
            if interaction["resources"]:
                p.append(
                    "**Resources:** "
                    + ", ".join(f"`{x}`" for x in interaction["resources"])
                    + "\n"
                )
            if interaction.get("examples"):
                p.append("\n**Examples**\n\n")
                p.append(self._blocks(interaction["examples"]))
        for key, label in (
            ("assumptions", "Assumptions"),
            ("sources", "Sources"),
            ("open_issues", "Open issues"),
        ):
            if boundary[key]:
                p.append(f"\n**{label}:** " + ", ".join(f"`{x}`" for x in boundary[key]) + "\n")
        return "".join(p)

    # -- blocks ----------------------------------------------------------
    def _blocks(self, blocks: list[dict]) -> str:
        p: list[str] = []
        for block in blocks:
            btype = block["type"]
            if btype in {"paragraph", "note", "quote"}:
                p.append(self.record(block, btype))
                p.append("\n")
            elif btype == "heading":
                p.append(self.record(block, "heading", level=block["level"]))
                p.append("\n")
            elif btype == "list":
                p.append(self._list_items(block["items"], block["ordered"], 0))
            elif btype == "code":
                p.append(self.record(block, "code"))
                p.append("\n")
            elif btype == "formula":
                p.append(self.record(block, "formula"))
                p.append("\n")
            elif btype == "figure":
                p.append(f"*Figure uses resource `{block['resource']}`.*\n\n")
                if "caption" in block:
                    p.append("**Caption.** ")
                    p.append(self.record(block["caption"], "paragraph"))
                    p.append("\n")
                if "alt" in block:
                    p.append("**Alternative text.** ")
                    p.append(self.record(block["alt"], "paragraph"))
                    p.append("\n")
            elif btype == "table":
                p.append("**Table**\n\n")
                for index, column in enumerate(block["columns"]):
                    p.append(f"- Column {index + 1}: ")
                    p.append(self.record(column, "table-cell"))
                    p.append("\n")
                for row_index, row in enumerate(block["rows"]):
                    p.append(f"\n*Row {row_index + 1}*\n\n")
                    for col_index, cell in enumerate(row):
                        p.append(f"- Cell {row_index + 1}.{col_index + 1}: ")
                        p.append(self.record(cell, "table-cell"))
                        p.append("\n")
                if "caption" in block:
                    p.append("\n**Caption.** ")
                    p.append(self.record(block["caption"], "paragraph"))
                    p.append("\n")
        return "".join(p)

    def _list_items(self, items: list[dict], ordered: bool, depth: int) -> str:
        p: list[str] = []
        for item in items:
            p.append(self.record(item, "list-item", ordered=ordered))
            p.append("\n")
            if item.get("children"):
                p.append(self._list_items(item["children"], ordered, depth + 1))
        return "".join(p)

    # -- appendices ------------------------------------------------------
    def _render_graphs(self) -> list[str]:
        p: list[str] = []
        if not self.payload["graphs"]:
            return p
        p.append("\n## Appendix: graphs\n\n")
        for graph in self.payload["graphs"]:
            p.append(f"### Graph `{graph['id']}`\n\n")
            p.append(self.record(graph["title"], "paragraph"))
            p.append(
                f"\n\n**Kind:** {graph['kind']} · **Owner:** {graph['owner']['kind']} "
                f"`{graph['owner']['id']}`\n\n"
            )
            p.append("**Nodes**\n\n")
            for node in graph["nodes"]:
                p.append(f"#### Node `{node['id']}` ({node['type']})\n\n")
                p.append(self.record(node["label"], "paragraph"))
                p.append("\n\n")
                if node.get("call"):
                    p.append(
                        f"Call: {node['call']['kind']} `{node['call']['id']}`\n\n"
                    )
                if node.get("inputs"):
                    p.append("**Inputs**\n\n")
                    p.append(self._blocks(node["inputs"]))
                if node.get("outputs"):
                    p.append("**Outputs**\n\n")
                    p.append(self._blocks(node["outputs"]))
                if node.get("requirement_refs"):
                    p.append(
                        "**Requirements:** "
                        + ", ".join(f"`{x}`" for x in node["requirement_refs"])
                        + "\n\n"
                    )
                if node.get("details"):
                    p.append(self._blocks(node["details"]))
            p.append("**Edges**\n\n")
            for edge in graph["edges"]:
                p.append(
                    f"#### Edge `{edge['id']}`: `{edge['from']}` → `{edge['to']}`\n\n"
                )
                if "label" in edge:
                    p.append(self.record(edge["label"], "paragraph"))
                    p.append("\n\n")
                if edge.get("condition"):
                    p.append("**Condition**\n\n")
                    p.append(self._blocks(edge["condition"]))
                if edge.get("requirement_refs"):
                    p.append(
                        "**Requirements:** "
                        + ", ".join(f"`{x}`" for x in edge["requirement_refs"])
                        + "\n\n"
                    )
                if "priority" in edge:
                    p.append(f"**Priority:** {edge['priority']}\n\n")
            if graph.get("notes"):
                p.append("**Notes**\n\n")
                p.append(self._blocks(graph["notes"]))
            p.append(self._derived_block(f"DERIVED-GRAPH-{graph['id']}", _graph_topology(graph)))
        return p

    def _render_resources(self) -> list[str]:
        p: list[str] = []
        if not self.payload["resources"]:
            return p
        p.append("\n## Appendix: resources\n\n")
        for resource in self.payload["resources"]:
            p.append(f"### Resource `{resource['id']}`\n\n")
            p.append(
                f"Path `{resource['path']}` · Media type `{resource['media_type']}` · "
                f"Size `{resource['size']}` bytes\n\n"
            )
            p.append(f"SHA-256 `{resource['sha256']}`\n\n")
            if resource.get("source_uri"):
                p.append(f"Source URI: {resource['source_uri']}\n\n")
            p.append("**Caption**\n\n")
            p.append(self._blocks(resource["caption"]))
            p.append("\n**Alternative text**\n\n")
            p.append(self._blocks(resource["alt"]))
            if resource["embedded_text"]:
                p.append("\n**Text present in the image**\n\n")
                for item in resource["embedded_text"]:
                    p.append(self.record(item, "list-item"))
            if resource.get("drawing_source"):
                source = resource["drawing_source"]
                p.append(
                    f"\n\n**Drawing source:** `{source['path']}` · Revision "
                    f"`{source['revision']}`"
                )
                if source.get("tool"):
                    p.append(f" · Tool `{source['tool']}`")
                p.append("\n")
            if resource.get("derived_from_graph"):
                p.append(f"**Derived from graph:** `{resource['derived_from_graph']}`\n")
            if resource.get("variants"):
                p.append("\n**Variants**\n\n")
                for variant in resource["variants"]:
                    p.append(
                        f"- `{variant['path']}` · {variant['media_type']} · "
                        f"{variant['size']} bytes · relation `{variant['relation']}` · "
                        f"derived from `{variant['derived_from']}`\n"
                    )
        return p

    def _render_records(self) -> list[str]:
        p: list[str] = []
        payload = self.payload
        if payload["assumptions"]:
            p.append("\n## Appendix: assumptions\n\n")
            for item in payload["assumptions"]:
                p.append(f"### Assumption `{item['id']}` ({item['status']})\n\n")
                p.append(self._blocks(item["statement"]))
                if item.get("affected"):
                    p.append(
                        "\nAffected: " + ", ".join(f"`{x}`" for x in item["affected"]) + "\n"
                    )
        if payload["decisions"]:
            p.append("\n## Appendix: decisions\n\n")
            for item in payload["decisions"]:
                p.append(f"### Decision `{item['id']}` ({item['status']})\n\n")
                p.append(self.record(item["title"], "heading", level=4))
                p.append("\n")
                for key in ("context", "decision", "alternatives", "consequences"):
                    p.append(f"**{key.capitalize()}**\n\n")
                    p.append(self._blocks(item[key]))
                    p.append("\n")
                if item.get("refs"):
                    p.append("Refs: " + ", ".join(f"`{x}`" for x in item["refs"]) + "\n")
        if payload["open_issues"]:
            p.append("\n## Appendix: open issues\n\n")
            for item in payload["open_issues"]:
                p.append(f"### Open issue `{item['id']}` ({item['status']})\n\n")
                p.append(self.record(item["title"], "paragraph"))
                p.append("\n\n")
                p.append(self._blocks(item["description"]))
                if item.get("refs"):
                    p.append("\nRefs: " + ", ".join(f"`{x}`" for x in item["refs"]) + "\n")
        if payload["sources"]:
            p.append("\n## Appendix: sources\n\n")
            for item in payload["sources"]:
                p.append(f"### Source `{item['id']}`\n\n")
                p.append(self.record(item["title"], "paragraph"))
                p.append("\n\n")
                if item.get("uri") is not None:
                    p.append(f"URI: {item['uri']}\n\n")
                if item.get("revision") is not None:
                    p.append(f"Revision: {item['revision']}\n\n")
                if item.get("accessed") is not None:
                    p.append(f"Accessed: {item['accessed']}\n\n")
                if item.get("note"):
                    p.append(self._blocks(item["note"]))
        if payload["history"]:
            p.append("\n## Appendix: history\n\n")
            for item in payload["history"]:
                p.append(f"### {item['version']} — {item['date']}\n\n")
                p.append(self._blocks(item["description"]))
        return p

    def _render_extensions(self) -> list[str]:
        extensions = self.payload.get("extensions") or {}
        if not extensions:
            return []
        import json

        return [
            "\n## Appendix: extensions (structural data)\n\n"
            "Extensions are preserved as declared data and are not interpreted by the translator.\n\n"
            "```json\n"
            + json.dumps(extensions, ensure_ascii=False, indent=2)
            + "\n```\n"
        ]

    def _render_derived_summary(self) -> str:
        return "\n## Appendix: derived summary\n\n" + self._derived_block(
            "DERIVED-SUMMARY", _summary_text(self.payload)
        )

    def _derived_block(self, derived_id: str, content: str) -> str:
        escaped = _escape_markdown_lines(content)
        return (
            f"<!-- atlas:derived id={derived_id} -->\n"
            + escaped
            + "\n<!-- /atlas:derived id="
            + derived_id
            + " -->\n\n"
        )

    def _render_structure_appendix(self) -> str:
        import json

        json_text = json.dumps(self.skeleton, ensure_ascii=False, indent=2)
        return (
            "\n## Appendix: Atlas structural record\n\n"
            "This appendix is authoritative for non-text data. Text is not duplicated here; "
            "each `@text` placeholder names a text record in the body above.\n\n"
            + STRUCTURE_BEGIN
            + "\n````atlas-structure\n"
            + json_text
            + "\n````\n"
            + STRUCTURE_END
            + "\n"
        )


def _summary_text(payload: dict) -> str:
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


def _derived_content(payload: dict, derived_id: str) -> str | None:
    if derived_id == "DERIVED-SUMMARY":
        return _summary_text(payload)
    if derived_id.startswith("DERIVED-GRAPH-"):
        graph_id = derived_id[len("DERIVED-GRAPH-") :]
        graph = next((g for g in payload["graphs"] if g["id"] == graph_id), None)
        if graph is not None:
            return _graph_topology(graph)
    return None


def encode_markdown(document: dict, *, options: EncodeOptions) -> str:
    payload = document["atlas"]
    table = externalize(payload)
    presenter = MarkdownPresenter(table.skeleton, table)
    return presenter.render()
