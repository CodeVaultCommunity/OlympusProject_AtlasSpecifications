"""Adapter registry and the four fundamental transformations."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .adapters.base import Adapter, DecodeOptions, EncodeOptions
from .adapters.json_adapter import JsonAdapter
from .adapters.latex_adapter import LatexAdapter
from .adapters.markdown_adapter import MarkdownAdapter
from .errors import AtlasError, AtlasVersionError, Diagnostic
from .validation import Validator
from .util import atlas_content_equal, write_text_exact

FUNDAMENTAL = (
    ("markdown", "json"),
    ("json", "markdown"),
    ("latex", "json"),
    ("json", "latex"),
)
ALL_FORMATS = ("json", "markdown", "latex")


@dataclass
class AdapterRegistry:
    representation_version: str = "Alpha-v0.1.0"
    adapter_factories: dict[tuple[str, str], type[Adapter]] = field(default_factory=dict)
    validator: Validator = field(default_factory=Validator)

    def __post_init__(self) -> None:
        self.register(JsonAdapter, "json", "Alpha-v0.1.0")
        self.register(MarkdownAdapter, "markdown", "Alpha-v0.1.0")
        self.register(LatexAdapter, "latex", "Alpha-v0.1.0")

    def register(
        self, adapter: type[Adapter] | Adapter, format_name: str, version: str
    ) -> None:
        key = (version, format_name)
        if key in self.adapter_factories:
            raise ValueError(f"adapter already registered for {version}/{format_name}")
        self.adapter_factories[key] = adapter if isinstance(adapter, type) else type(adapter)

    def get(self, format_name: str, version: str | None = None) -> Adapter:
        version = version or self.representation_version
        key = (version, format_name)
        if key not in self.adapter_factories:
            raise AtlasVersionError(
                Diagnostic(
                    "ATL-E-ADAPTER",
                    f"no adapter for representation {format_name!r} version {version!r}; "
                    f"available: {self.available()}",
                )
            )
        return self.adapter_factories[key]()

    def available(self) -> str:
        return ", ".join(f"{fmt}/{ver}" for ver, fmt in sorted(self.adapter_factories))

    def decode_to_atlas_json(
        self,
        source,
        *,
        source_format: str,
        representation_version: str | None = None,
        resource_root: Path | None = None,
        check_resources: bool = True,
    ) -> dict:
        version = representation_version or self.representation_version
        adapter = self.get(source_format, version)
        options = DecodeOptions(
            validator=self.validator,
            resource_root=resource_root,
            check_resources=check_resources,
        )
        document = adapter.decode(source, options)
        self.validator.validate(
            document,
            resource_root=resource_root,
            check_resources=check_resources,
        )
        return document

    def encode_from_atlas_json(
        self,
        document: dict,
        *,
        target_format: str,
        representation_version: str | None = None,
        resource_root: Path | None = None,
        check_resources: bool = True,
    ) -> str:
        version = representation_version or self.representation_version
        self.validator.validate(
            document,
            resource_root=resource_root,
            check_resources=check_resources,
        )
        adapter = self.get(target_format, version)
        options = EncodeOptions(
            validator=self.validator,
            resource_root=resource_root,
            check_resources=check_resources,
        )
        return adapter.encode(document, options)

    def convert_file(
        self,
        source: Path,
        target: Path,
        *,
        source_format: str,
        target_format: str,
        representation_version: str | None = None,
        resource_root: Path | None = None,
        check_resources: bool = True,
    ) -> dict:
        """Convert and verify one file through a validated Atlas JSON document.

        Decode the generated target and compare its exact Atlas payload before
        writing. Return the validated source document for API compatibility;
        callers auditing disk output may independently read the target again.

        Resources are never copied or rewritten; paths remain relative to the
        document's package root.  The caller is responsible for packaging.
        """

        document = self.decode_to_atlas_json(
            source,
            source_format=source_format,
            representation_version=representation_version,
            resource_root=resource_root or source.parent,
            check_resources=check_resources,
        )
        output = self.encode_from_atlas_json(
            document,
            target_format=target_format,
            representation_version=representation_version,
            resource_root=resource_root or target.parent,
            check_resources=check_resources,
        )
        recovered = self.decode_to_atlas_json(
            output,
            source_format=target_format,
            representation_version=representation_version,
            resource_root=resource_root or target.parent,
            check_resources=check_resources,
        )
        if not atlas_content_equal(document, recovered):
            raise AtlasError(
                "post-encode verification failed: Atlas content changed; nothing was written"
            )
        write_text_exact(target, output)
        return document


def default_registry() -> AdapterRegistry:
    return AdapterRegistry()
