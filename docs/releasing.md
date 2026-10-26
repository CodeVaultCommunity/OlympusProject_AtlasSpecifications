# Preparing an Atlas release

[Português](releasing.pt-br.md) · [Home](../README.md) · [Agent guide](../AGENTS.md)

This procedure adds no Atlas model requirements. Select the intended edition before choosing its contracts, translator, skill and checks. `CITATION.cff` supplies the release identity for inventory metadata; document revisions and translator package versions retain their independent meanings. A local verified commit and ZIP do not imply publication or stakeholder approval.

## Finalize sources and verify

Check the branch and working tree, preserving user changes and historical editions. Coordinate English/Portuguese, versions, OAL snapshots and skill hashes. Confirm the person responsible for editorial migration separately from authorship and approval of example requirements. Preserve previous logs and checkpoints with their original scope, without relabeling them as a new execution.

Use a canonical clean checkout or Git-index export and respect `.gitattributes`, including literal line endings in Atlas documents and raw evidence. Hash actual bytes without normalization during hashing; never rewrite frozen Alpha files or regenerate the inventory to hide mixed checkout bytes. Keep environments and temporary outputs outside the delivery tree.

From the repository root, run `python -m pytest scripts/tests`. For Stable-v1.0.0, use Python 3.11+ and run from its directory:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

When canonical sources change, run `python skills/build.py` before checking the skill. Publication changes also require `python examples/build.py --pdf`, documented LaTeX dependencies and visual inspection. Tool/guide changes alone do not require rebuilding unchanged PDFs; preserve prior visual evidence and report what was actually rerun. Rebuilding PDFs can change timestamps and hashes.

## Generate the single inventory

Root `CONTENT-SHA256.json` is the only active distribution inventory, following the OAL pattern. It records `algorithm`, `atlas_edition` (matching `CITATION.cff`), scope, exclusions and relative POSIX `path`, `size_bytes` and `sha256` entries. It covers every indexed delivery file, including Alpha, PDFs, artwork, scripts, reports, raw evidence, historical checkpoints and `.github/`. Only the inventory itself is excluded. Generation sorts paths deterministically; verification compares identity and content independently of record order and rejects duplicate paths.

Finalize sources and execution evidence, then stage intended additions, modifications and deletions with explicit paths. Untracked additions are not discovered automatically. From the root:

```bash
python scripts/content_inventory.py --write
python scripts/content_inventory.py --check
git add -- CONTENT-SHA256.json
```

The generator reads indexed paths and actual working-tree bytes. Confirm those bytes also match the staged Git blobs before committing. There is no active `release-inputs.json` per edition and no fixed file count. Older checkpoint inventories remain historical evidence; never regenerate them. Execution records may identify their source baseline and relevant changed-file hashes, excluding themselves and the final inventory to avoid cycles. All completed evidence is covered by the final root inventory. Generate/check that inventory last, then commit the complete tree locally.

## Package and inspect

After the commit, run from the root:

```bash
python scripts/build_distribution.py --output /absolute/path/Atlas-Stable-v1.0.0.zip
python scripts/check_archive.py /absolute/path/Atlas-Stable-v1.0.0.zip
```

The builder refuses dirty tracked content, stale inventory, tracked caches/intermediates and existing output. It archives committed files and verifies complete coverage and exact bytes. The ZIP contains all editions inside `Atlas_Stable/`, without `.git`; the checker also accepts files directly at a ZIP's root.

Extract the actual ZIP into a new empty directory, then check the extracted repository root **before** installing or regenerating anything:

```bash
python /path/to/extracted/Atlas_Stable/scripts/check_archive.py /path/to/extracted/Atlas_Stable
```

The archive/directory checker uses only Python's standard library, without Git, and rejects missing, additional, duplicate or changed files. `content_inventory.py` instead requires a Git checkout. Keep a fresh environment outside the extracted tree and follow the edition's installation/validation instructions. Generated caches and installation metadata count as extra files in a strict archive audit.

Keep the final commit ID, ZIP size/SHA-256, file count, checks and limits in an external receipt, outside the commit and ZIP it identifies. The commit and external ZIP digest protect the inventory itself.

## Optional publication

Only after explicit authorization, send the intended commit and require successful CI for that revision in the supported Windows/Linux and Python jobs, plus the publication job. Configuration alone is not execution evidence. Create the annotated edition tag and release from that commit, attach the checked ZIP and SHA-256, and confirm their identities. A local-only delivery stops at the verified commit, ZIP and external receipt; it creates no push, tag or remote release. Published snapshots are immutable.
