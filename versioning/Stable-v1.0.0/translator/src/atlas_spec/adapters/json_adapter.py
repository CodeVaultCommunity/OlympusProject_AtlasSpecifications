"""Atlas JSON adapter."""

from __future__ import annotations

from pathlib import Path

from ..errors import AtlasParseError, AtlasVersionError, Diagnostic
from ..util import decode_text_exact, json_dumps, strict_json_loads
from .base import Adapter, DecodeOptions, EncodeOptions

PROFILE_VERSION = "Alpha-v0.1.0"
FORMAT = f"atlas-json/{PROFILE_VERSION}"


class JsonAdapter(Adapter):
    format_name = "json"

    def decode(self, source: str | bytes | Path, options: DecodeOptions) -> dict:
        text, source_path = self._read_source(source)
        document = strict_json_loads(text, location=str(source_path) if source_path else "JSON")
        if not isinstance(document, dict):
            raise AtlasParseError(
                Diagnostic("ATL-E-JSON", "the JSON top level must be an object")
            )
        fmt = document.get("format")
        if not isinstance(fmt, str) or not fmt.startswith("atlas-json/"):
            raise AtlasVersionError(
                Diagnostic(
                    "ATL-E-FORMAT",
                    "the document does not declare an Atlas JSON representation in 'format'",
                    str(source_path) if source_path else "JSON",
                )
            )
        if fmt != FORMAT:
            raise AtlasVersionError(
                Diagnostic(
                    "ATL-E-VERSION",
                    f"Atlas JSON version {fmt!r} is not supported; this translator "
                    f"implements {FORMAT!r}",
                    str(source_path) if source_path else "JSON",
                )
            )
        options.validator.validate(
            document,
            resource_root=options.resource_root or (source_path.parent if source_path else None),
            check_resources=options.check_resources,
        )
        return document

    def encode(self, document: dict, options: EncodeOptions) -> str:
        return json_dumps(document) + "\n"

    def _read_source(self, source: str | bytes | Path) -> tuple[str, Path | None]:
        if isinstance(source, Path):
            return decode_text_exact(source.read_bytes(), location=str(source)), source
        if isinstance(source, bytes):
            return decode_text_exact(source, location="<bytes>"), None
        return source, None
