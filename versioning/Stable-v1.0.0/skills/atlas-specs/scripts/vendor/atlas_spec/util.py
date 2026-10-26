"""Deterministic I/O helpers.

Atlas treats UTF-8 source characters as content.  Files are decoded without
newline translation and are written without newline translation.  Structural
line endings emitted by the codecs are LF, except a CRLF separator after an
authored final CR prevents coalescing the content with its terminator. Authored
line endings inside text records are whatever the source contains.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .errors import AtlasParseError, Diagnostic


def _reject_float(value: str) -> Any:
    raise AtlasParseError(
        Diagnostic(
            "ATL-E-FLOAT",
            f"binary floating-point value {value!r} is not allowed in Atlas content; "
            "use an integer or a decimal string",
        )
    )


def _object_pairs(pairs: list[tuple[str, Any]]) -> dict:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AtlasParseError(
                Diagnostic("ATL-E-DUPLICATE-KEY", f"duplicate JSON object key {key!r}")
            )
        result[key] = value
    return result


def strict_json_loads(text: str, *, location: str = "JSON input") -> Any:
    """Parse JSON while rejecting duplicate keys and binary floats."""

    try:
        return json.loads(
            text,
            object_pairs_hook=_object_pairs,
            parse_float=_reject_float,
            parse_constant=_reject_float,
        )
    except AtlasParseError:
        raise
    except json.JSONDecodeError as exc:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-JSON",
                f"invalid JSON: {exc.msg}",
                f"{location}:{exc.lineno}:{exc.colno}",
            )
        ) from exc


def strict_json_bytes(data: bytes, *, location: str = "JSON input") -> Any:
    if data.startswith(b"\xef\xbb\xbf"):
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-BOM",
                "UTF-8 BOM is not allowed; Atlas source starts with the first character",
                location,
            )
        )
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-UTF8",
                f"source is not valid UTF-8: {exc.reason} at byte {exc.start}",
                location,
            )
        ) from exc
    return strict_json_loads(text, location=location)


def read_text_exact(path: Path) -> str:
    """Read UTF-8 preserving every authored line ending."""

    data = path.read_bytes()
    return decode_text_exact(data, location=str(path))


def decode_text_exact(data: bytes, *, location: str) -> str:
    if data.startswith(b"\xef\xbb\xbf"):
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-BOM",
                "UTF-8 BOM is not allowed; Atlas source starts with the first character",
                location,
            )
        )
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AtlasParseError(
            Diagnostic(
                "ATL-E-UTF8",
                f"source is not valid UTF-8: {exc.reason} at byte {exc.start}",
                location,
            )
        ) from exc


def write_text_exact(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def json_dumps(document: Any, *, indent: int = 2) -> str:
    return json.dumps(document, ensure_ascii=False, indent=indent, separators=(",", ": "), allow_nan=False)


def atlas_content_equal(left: dict, right: dict) -> bool:
    """Compare Atlas payloads, excluding representation wrapper metadata.

    Object member order is insignificant; array order, scalar types, null,
    absent members and every text character are significant. In particular,
    Python's ``True == 1`` must not conceal a changed extension value.
    Call this on validated Atlas JSON transport documents.
    """

    def equal(a: Any, b: Any) -> bool:
        if type(a) is not type(b):
            return False
        if isinstance(a, dict):
            return a.keys() == b.keys() and all(equal(a[key], b[key]) for key in a)
        if isinstance(a, list):
            return len(a) == len(b) and all(equal(x, y) for x, y in zip(a, b))
        return a == b

    return equal(left["atlas"], right["atlas"])


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def detect_newline(text: str) -> str:
    index = text.find("\n")
    if index > 0 and text[index - 1] == "\r":
        return "\r\n"
    return "\n"


def split_lines_keepends(text: str) -> list[str]:
    """Split on LF, CRLF, or CR while keeping every line ending."""

    # str.splitlines also splits U+0085/U+2028/U+2029 and other content
    # characters. The profile only treats CR, LF and CRLF as line endings.
    return re.findall(r"[^\r\n]*(?:\r\n|\r|\n)|[^\r\n]+$", text)


def strip_line_ending(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    if line.endswith("\r"):
        return line[:-1], "\r"
    return line, ""


def line_of_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1
