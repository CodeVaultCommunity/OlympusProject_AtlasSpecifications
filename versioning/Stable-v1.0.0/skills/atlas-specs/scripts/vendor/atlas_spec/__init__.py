"""Atlas Specifications translator, Stable-v1.0.0."""

from .adapters.base import Adapter, DecodeOptions, EncodeOptions
from .adapters.json_adapter import JsonAdapter
from .adapters.latex_adapter import LatexAdapter
from .adapters.markdown_adapter import MarkdownAdapter
from .errors import (
    AtlasError,
    AtlasParseError,
    AtlasValidationError,
    AtlasVersionError,
    Diagnostic,
)
from .registry import ALL_FORMATS, FUNDAMENTAL, AdapterRegistry, default_registry
from .validation import SUPPORTED_PROFILE_VERSION, SUPPORTED_SPEC_VERSION, Validator, validate_document
from .util import atlas_content_equal

__all__ = [
    "ALL_FORMATS",
    "FUNDAMENTAL",
    "SUPPORTED_PROFILE_VERSION",
    "SUPPORTED_SPEC_VERSION",
    "Adapter",
    "AdapterRegistry",
    "AtlasError",
    "AtlasParseError",
    "AtlasValidationError",
    "AtlasVersionError",
    "DecodeOptions",
    "Diagnostic",
    "EncodeOptions",
    "JsonAdapter",
    "LatexAdapter",
    "MarkdownAdapter",
    "Validator",
    "default_registry",
    "validate_document",
    "atlas_content_equal",
]

__version__ = "1.0.0"
