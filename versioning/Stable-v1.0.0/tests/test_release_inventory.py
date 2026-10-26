"""Release inventories compare identities/bytes, never filesystem sort order."""
import copy
import importlib.util
import json
import random

import pytest

from conftest import VERSION_ROOT


@pytest.fixture
def inventory(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("release_inventory", VERSION_ROOT / "verification/capture_release.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    root = tmp_path / "repository"
    edition = root / "versioning/Stable-v1.0.0"
    (edition / "verification").mkdir(parents=True)
    for name in ["README.md", "Z.txt", "a.txt", "Alpha.txt"]:
        (edition / name).write_bytes(name.encode())
    monkeypatch.setattr(module, "ROOT", root)
    monkeypatch.setattr(module, "EDITION", edition)
    monkeypatch.setattr(module, "OUTPUT", edition / "verification/release-inputs.json")
    return module


def check(module, monkeypatch, records):
    module.OUTPUT.write_text(json.dumps({"files": records}), encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["capture_release.py", "--check"])
    module.main()


@pytest.mark.parametrize("order", ["windows", "posix", "shuffled"])
def test_order_is_not_content(inventory, monkeypatch, order):
    rows = inventory.inputs()
    if order == "shuffled":
        random.Random(18).shuffle(rows)
    else:
        rows.sort(key=lambda r: r["path"].casefold() if order == "windows" else r["path"])
    check(inventory, monkeypatch, rows)


@pytest.mark.parametrize("mutation,diagnostic", [("byte", "hash"), ("size", "size"),
                                                 ("add", "added"), ("remove", "missing"),
                                                 ("duplicate", "duplicate")])
def test_changes_are_not_hidden(inventory, monkeypatch, mutation, diagnostic):
    rows = copy.deepcopy(inventory.inputs())
    file = inventory.EDITION / "a.txt"
    if mutation == "byte":
        file.write_bytes(b"b.txt")
    elif mutation == "size":
        file.write_bytes(b"longer")
    elif mutation == "add":
        (inventory.EDITION / "extra.txt").write_bytes(b"extra")
    elif mutation == "remove":
        file.unlink()
    else:
        rows.append(copy.deepcopy(rows[0]))
    with pytest.raises(SystemExit, match=diagnostic):
        check(inventory, monkeypatch, rows)


def test_capture_orders_relative_posix_strings(inventory):
    names = [r["path"] for r in inventory.inputs()]
    assert names == sorted(names)
    assert all("\\" not in name for name in names)
