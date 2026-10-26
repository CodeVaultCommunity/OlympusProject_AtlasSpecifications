# Agent guide · Atlas Specifications

## Select the edition first

Respect the edition explicitly requested by the user or unambiguously identified by the requested path. A document's `spec_version` and `profile_version` identify its contract; selecting another edition or changing file format does not migrate that document. Resolve a conflict affecting the requested operation before changing identities. Comparisons can involve several editions, with their contracts kept separate.

If no edition is indicated, select the highest available `Stable-vMAJOR.MINOR.PATCH` directory under `versioning/` containing `README.md`, comparing the three version components numerically. Consult the root [version table](README.md#versions) for navigation. Ask only if the requested edition is missing or ambiguous, conflicting document identities prevent the operation, or no Stable edition is available. State the selected edition when it matters to the work. `CITATION.cff` identifies the repository release for citation and inventory metadata; it does not override the user's selection or the default selection rule.

Keep the model, representation profiles, translator, examples and skill from that edition together. Preserve historical Alpha content byte for byte when maintaining Stable. Do not infer compatibility from a similar filename or relabel documents using another edition's skill. Published commit/tag snapshots are immutable.

## Locate authoritative sources

Use these paths inside `versioning/<selected-edition>/`, checking their existence and the edition's own instructions before choosing commands:

| Need | Edition-relative source |
| --- | --- |
| Model, invariants, preservation and OAL correspondence | `README.md` is normative; `README.pt-br.md` is its translation. |
| Representation grammars and starters | `implementations/json/README.md`, `implementations/markdown/README.md`, `implementations/latex/README.md`. |
| JSON structure | `implementations/json/atlas.schema.json`. |
| Translator | `translator/README.md`, `translator/atlas_translate.py`, `translator/src/atlas_spec/`. |
| Examples and publication | `examples/README.md`. |
| Dependencies and checks | `pyproject.toml`, `tests/`, and the manual's verification guide. |
| Portable agent workflow | `skills/atlas-specs/SKILL.md`, when supplied. |

Read the selected model and relevant representation guide. Validate structural claims with its translator and review semantic claims against its manual and the user's sources. A schema pass does not establish complete requirements or stakeholder approval. If an edition lacks a skill or check, use its documented alternatives; never substitute another edition's implementation silently.

The root [README.md](README.md) and [README.pt-br.md](README.pt-br.md) are illustrated introductions. Root [assets/](assets/README.md) contains presentation artwork and editable sources; the edition runtime does not require it.

## Locate and install the skill

When supplied, the complete installation unit is `versioning/<selected-edition>/skills/atlas-specs/`. Read its `SKILL.md`. Copy the whole directory, retaining its `atlas-specs` name, references, scripts, assets, agent metadata, license and source correspondence. Use the skills location configured for the host; no universal path or automatic discovery is assumed. Compare an existing destination's edition and local customizations before replacement. A copy operation must not silently merge or overwrite it.

Install dependencies and run the bundled translator using that skill's instructions and supported Python version. Register or reload the directory through the host's mechanism; reading this guide does not install it. Consumers do not run the repository's skill builder.

## Maintain and verify

Maintain English and Portuguese together. Edit canonical sources before regenerating affected reading formats and bundled files with the selected edition's helpers. For Stable-v1.0.0, Python 3.11+ is supported: from its directory, `python skills/build.py` synchronizes the skill and packaged resources; `python skills/build.py --check` detects drift. Use that edition's verification guide for tests, conversions and publication. Inspect rendered PDFs after publication changes. Do not automatically apply these commands to another edition.

Repository-wide tooling lives in `scripts/`. From the root, run `python -m pytest scripts/tests` and `python scripts/content_inventory.py --check`. The single root `CONTENT-SHA256.json` covers every indexed delivery file except itself, including historical editions, reports, raw evidence and `.github/`. No active per-edition release inventory is maintained. Historical checkpoint records describe their original commits and remain unchanged.

Follow [the release procedure](docs/releasing.md). Stage intended additions, modifications and deletions before generating the inventory; delivery paths come from Git's index. Hash actual canonical bytes without newline normalization during hashing; never rewrite historical files to hide checkout differences. Complete sources, generated skill files, tests and evidence before generating the inventory last. Inspect the final ZIP and extracted repository with `python scripts/check_archive.py PATH`, which requires no Git. Keep the final commit ID and ZIP digest in an external receipt to avoid circular references. Publication requires explicit authorization; a local commit does not publish a release.
