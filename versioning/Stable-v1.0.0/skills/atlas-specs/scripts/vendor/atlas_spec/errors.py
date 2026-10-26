"""Diagnostics shared by every Atlas adapter."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Diagnostic:
    code: str
    message: str
    location: str | None = None
    severity: str = "error"

    def format(self) -> str:
        where = f" [{self.location}]" if self.location else ""
        return f"{self.severity.upper()} {self.code}{where}: {self.message}"


class AtlasError(Exception):
    """Base class for a conversion or validation failure."""

    def __init__(self, diagnostics: list[Diagnostic] | Diagnostic | str):
        if isinstance(diagnostics, str):
            diagnostics = [Diagnostic("ATL-E-GENERAL", diagnostics)]
        elif isinstance(diagnostics, Diagnostic):
            diagnostics = [diagnostics]
        self.diagnostics = list(diagnostics)
        super().__init__("\n".join(d.format() for d in self.diagnostics))


class AtlasParseError(AtlasError):
    """The source representation could not be decoded."""


class AtlasValidationError(AtlasError):
    """The decoded Atlas document is structurally or referentially invalid."""


class AtlasVersionError(AtlasError):
    """The requested representation version is not registered."""


@dataclass
class SourcePosition:
    path: Path | None = None
    line: int | None = None

    def label(self) -> str:
        if self.path is None:
            return f"line {self.line}" if self.line else "source"
        if self.line is None:
            return str(self.path)
        return f"{self.path}:{self.line}"


@dataclass
class DecodeResult:
    """A decoded Atlas document plus the source file's resource directory."""

    document: dict
    source_path: Path | None = None
    resource_root: Path | None = None
    warnings: list[Diagnostic] = field(default_factory=list)
