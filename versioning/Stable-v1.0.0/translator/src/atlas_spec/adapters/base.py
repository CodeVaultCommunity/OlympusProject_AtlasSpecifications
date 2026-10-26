"""Bidirectional adapter contract."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from ..validation import Validator


@dataclass
class DecodeOptions:
    validator: Validator = field(default_factory=Validator)
    resource_root: Path | None = None
    check_resources: bool = True


@dataclass
class EncodeOptions:
    validator: Validator = field(default_factory=Validator)
    resource_root: Path | None = None
    check_resources: bool = True


class Adapter:
    """A representation adapter.

    ``decode`` returns an Atlas JSON document (``format`` + ``atlas``).
    ``encode`` receives a validated Atlas JSON document.
    """

    format_name: str = ""

    def decode(self, source, options: DecodeOptions) -> dict:  # pragma: no cover - interface
        raise NotImplementedError

    def encode(self, document: dict, options: EncodeOptions) -> str:  # pragma: no cover - interface
        raise NotImplementedError
