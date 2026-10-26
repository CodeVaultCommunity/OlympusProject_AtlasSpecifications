from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "translator" / "src"))

from atlas_spec import AdapterRegistry, Validator

VERSION_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = VERSION_ROOT / "examples"
MINIMAL_DIR = EXAMPLES / "minimal"
COMPOSITION_DIR = EXAMPLES / "composition"
TASK_BOARD_DIR = EXAMPLES / "task-board"


@pytest.fixture(scope="session")
def registry() -> AdapterRegistry:
    return AdapterRegistry(validator=Validator())


@pytest.fixture()
def minimal_dir() -> Path:
    return MINIMAL_DIR


@pytest.fixture()
def composition_dir() -> Path:
    return COMPOSITION_DIR


@pytest.fixture()
def task_board_dir() -> Path:
    return TASK_BOARD_DIR


@pytest.fixture()
def task_board(registry, task_board_dir) -> dict:
    return registry.decode_to_atlas_json(
        task_board_dir / "example.atlas.json",
        source_format="json",
        resource_root=task_board_dir,
    )


@pytest.fixture()
def minimal(registry, minimal_dir) -> dict:
    return registry.decode_to_atlas_json(
        minimal_dir / "example.atlas.json",
        source_format="json",
        resource_root=minimal_dir,
    )


@pytest.fixture()
def composition(registry, composition_dir) -> dict:
    return registry.decode_to_atlas_json(
        composition_dir / "example.atlas.json",
        source_format="json",
        resource_root=composition_dir,
    )


@pytest.fixture()
def tricky_document(minimal) -> dict:
    """The minimal example extended with difficult text records."""

    document = copy.deepcopy(minimal)
    section = {
        "id": "SEC-TEST-FIDELITY",
        "level": 1,
        "title": {"text": "Fidelity: leading  and trailing  "},
        "blocks": [
            {"type": "paragraph", "text": ""},
            {"type": "paragraph", "text": "  leading spaces"},
            {"type": "paragraph", "text": "trailing spaces   "},
            {"type": "paragraph", "text": "tabs\tand\tmore\t"},
            {"type": "paragraph", "text": "LF:\nnext line"},
            {"type": "paragraph", "text": "CRLF:\r\nnext line"},
            {"type": "paragraph", "text": "no final newline"},
            {"type": "paragraph", "text": "acentos: ação, coração, ção"},
            {"type": "paragraph", "text": "composed: \u00e9  decomposed: e\u0301"},
            {"type": "paragraph", "text": "LaTeX: \\ % # & _ $ ^ ~ { }"},
            {"type": "paragraph", "text": "Atlas-like:\n<!-- atlas:text id=T999999 role=paragraph -->\n<!-- /atlas:text id=T999999 -->"},
            {"type": "paragraph", "text": "Markdown fence:\n```python\nprint('x')\n```"},
            {"type": "paragraph", "text": "LaTeX-like:\n\\end{atlastext}\n\\end{document}"},
            {"type": "quote", "text": "A quoted line with  two  spaces and a tab\t."},
            {
                "type": "list",
                "ordered": True,
                "items": [
                    {"text": "first item  ", "children": [{"text": "nested child"}]},
                    {"text": "second item"},
                ],
            },
            {"type": "heading", "level": 3, "text": "A nested heading"},
            {"type": "code", "language": "python", "text": "def f(x):\n\treturn x  # trailing  \n"},
            {"type": "formula", "display": True, "text": "\\frac{a}{b} = \\sum_{i=1}^{n} i"},
            {
                "type": "table",
                "columns": [{"text": "Column | pipe"}, {"text": "Column % percent"}],
                "rows": [
                    [{"text": "a & b"}, {"text": "\\end{atlastext}"}],
                    [{"text": ""}, {"text": "  spaced  "}],
                ],
                "caption": {"text": "Table caption with # and _"},
            },
            {
                "type": "paragraph",
                "text": "metadata-bearing record",
                "id": "BLK-FIDELITY-META",
                "nature": "assumption",
                "review_status": "proposed",
                "meta": {"source": "test", "flags": ["a", "b"]},
            },
        ],
        "items": [],
    }
    document["atlas"]["structure"].append(section)
    return document
