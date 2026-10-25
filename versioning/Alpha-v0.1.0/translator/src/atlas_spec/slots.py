"""Separate textual content from structural content.

The canonical Atlas JSON keeps text next to the thing it describes.  Atlas
Markdown and Atlas LaTeX need a visible, editable body whose prose is not
duplicated in an opaque payload.  Those codecs therefore externalise every
``{"text": ...}`` record:

* the structural skeleton keeps ``{"@text": "T000001", ...metadata...}``;
* the body contains the exact text once, in a marked text record.

Decoding merges the body text back into the skeleton.  A missing, duplicated,
or unknown record is an error.  Structure lives in a clearly identified
appendix; prose is read from the body.  Extensions are structural and are
never externalised. The same applies to free-form metadata and example data;
their literal text/@text/id keys belong to their own data, not the Atlas codec.
"""

from __future__ import annotations

from dataclasses import dataclass
from copy import deepcopy
from typing import Any

from .errors import AtlasParseError, Diagnostic

OPAQUE_KEYS = {"extensions", "meta", "data"}


@dataclass
class SlotTable:
    skeleton: Any
    texts: dict[str, str]
    roles: dict[str, dict[str, Any]]


def _is_text_record(value: Any) -> bool:
    return isinstance(value, dict) and "text" in value and "@text" not in value


def externalize(payload: Any, *, prefix: str = "T") -> SlotTable:
    texts: dict[str, str] = {}
    roles: dict[str, dict[str, Any]] = {}
    counter = 0

    def walk(value: Any, path: str, *, opaque: bool = False) -> Any:
        nonlocal counter
        if opaque:
            if isinstance(value, dict):
                return {k: walk(v, f"{path}.{k}", opaque=True) for k, v in value.items()}
            if isinstance(value, list):
                return [walk(v, f"{path}[{i}]", opaque=True) for i, v in enumerate(value)]
            return value
        if isinstance(value, dict):
            if _is_text_record(value):
                counter += 1
                slot_id = f"{prefix}{counter:06d}"
                text = value["text"]
                if not isinstance(text, str):
                    raise AtlasParseError(
                        Diagnostic(
                            "ATL-E-TEXT-TYPE",
                            "a text record's 'text' member must be a string",
                            path,
                        )
                    )
                texts[slot_id] = text
                roles[slot_id] = {"path": path, "keys": sorted(value.keys())}
                skeleton = {
                    k: walk(v, f"{path}.{k}", opaque=(k in OPAQUE_KEYS))
                    for k, v in value.items()
                    if k != "text"
                }
                skeleton["@text"] = slot_id
                return skeleton
            return {
                k: walk(v, f"{path}.{k}", opaque=(k in OPAQUE_KEYS))
                for k, v in value.items()
            }
        if isinstance(value, list):
            return [walk(v, f"{path}[{i}]", opaque=opaque) for i, v in enumerate(value)]
        return value

    skeleton = walk(payload, "$")
    return SlotTable(skeleton=skeleton, texts=texts, roles=roles)


def restore(skeleton: Any, texts: dict[str, str]) -> Any:
    used: set[str] = set()

    def walk(value: Any, path: str, *, opaque: bool = False) -> Any:
        if opaque:
            return deepcopy(value)
        if isinstance(value, dict):
            if "@text" in value:
                slot_id = value["@text"]
                if not isinstance(slot_id, str):
                    raise AtlasParseError(
                        Diagnostic("ATL-E-SLOT", "invalid text slot identifier", path)
                    )
                if "text" in value:
                    raise AtlasParseError(
                        Diagnostic("ATL-E-SLOT", "text and @text cannot both define a text record", path)
                    )
                if slot_id in used:
                    raise AtlasParseError(
                        Diagnostic("ATL-E-SLOT-DUPLICATE", f"text record {slot_id!r} is referenced more than once", path)
                    )
                if slot_id not in texts:
                    raise AtlasParseError(
                        Diagnostic(
                            "ATL-E-SLOT-MISSING",
                            f"text record {slot_id!r} is referenced by the structure "
                            "appendix but is absent from the body",
                            path,
                        )
                    )
                used.add(slot_id)
                result = {
                    k: walk(v, f"{path}.{k}", opaque=(k in OPAQUE_KEYS)) for k, v in value.items() if k != "@text"
                }
                result["text"] = texts[slot_id]
                return result
            return {k: walk(v, f"{path}.{k}", opaque=(k in OPAQUE_KEYS)) for k, v in value.items()}
        if isinstance(value, list):
            return [walk(v, f"{path}[{i}]") for i, v in enumerate(value)]
        return value

    restored = walk(skeleton, "$")
    unused = sorted(set(texts) - used)
    if unused:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-SLOT-ORPHAN",
                "text records are not referenced by the structure appendix: "
                + ", ".join(unused),
            )
        )
    return restored


def duplicate_text_ids(ids: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for slot_id in ids:
        if slot_id in seen and slot_id not in duplicates:
            duplicates.append(slot_id)
        seen.add(slot_id)
    return duplicates
