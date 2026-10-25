# Agent guide · Atlas Specifications

Use this file to locate the selected edition and its portable skill. The illustrated project introduction is in [README.md](README.md); [README.pt-br.md](README.pt-br.md) is the Portuguese introduction.

## Select an edition

Start with the root [version table](README.md#versions). The current and only edition is **Alpha-v0.1.0**, under `versioning/Alpha-v0.1.0/`. Keep the model, representation profiles, translator, examples, and skill from that same edition together. A document's `spec_version` and `profile_version` select its contract; changing file format does not migrate a document to another edition.

For another edition added later, use its own directory and the links in the version table. Do not infer compatibility from a similar filename or use one edition's skill to relabel another edition's document.

## Find the authoritative information

Paths below are relative to this repository root.

| Need | Current-edition source |
| --- | --- |
| Detailed model, invariants, resources, preservation, and OAL correspondence | [English manual](versioning/Alpha-v0.1.0/README.md), the normative source; [Portuguese translation](versioning/Alpha-v0.1.0/README.pt-br.md). |
| Representation grammar and starter files | [JSON](versioning/Alpha-v0.1.0/implementations/json/README.md), [Markdown](versioning/Alpha-v0.1.0/implementations/markdown/README.md), and [LaTeX](versioning/Alpha-v0.1.0/implementations/latex/README.md). |
| JSON structure | [atlas.schema.json](versioning/Alpha-v0.1.0/implementations/json/atlas.schema.json). |
| Translator commands and implementation | [CLI guide](versioning/Alpha-v0.1.0/translator/README.md), `translator/atlas_translate.py`, and `translator/src/atlas_spec/` inside the edition. |
| Worked specifications and publication instructions | [Examples guide](versioning/Alpha-v0.1.0/examples/README.md). |
| Dependencies and executable checks | `pyproject.toml` and `tests/` inside the edition; [verification guide](versioning/Alpha-v0.1.0/README.md#verification). |
| Agent workflow and portable installation unit | [skills/atlas-specs/SKILL.md](versioning/Alpha-v0.1.0/skills/atlas-specs/SKILL.md). |
| Project identity, illustrations, and editable artwork | Root [assets/](assets/README.md). The edition's runtime does not require this presentation artwork. |

Read the model and relevant representation guide for the task. Validate structural claims with the translator and review semantic claims against the manual and the user's sources. A passing schema check does not establish complete requirements or stakeholder approval.

## Locate and install the skill

The complete installation unit is:

`versioning/Alpha-v0.1.0/skills/atlas-specs/`

It contains `SKILL.md`, `references/`, `scripts/`, `assets/`, agent metadata, the license, and source correspondence. Copy the **whole directory**, retaining its `atlas-specs` name. Its bundled references, runtime, and starter support use without this repository.

Choose the skills directory configured for the host agent. This repository does not prescribe a universal installation path or imply that every host discovers skills automatically. If a destination already exists, compare its edition and local changes before replacing it; retain any user customizations deliberately.

The example below runs from the repository root. Replace `/absolute/path/to/agent-skills/atlas-specs` with the chosen destination. `copytree` refuses an existing destination, so it cannot silently merge or overwrite a previous installation.

```bash
python -c "import shutil, sys; shutil.copytree(sys.argv[1], sys.argv[2])" versioning/Alpha-v0.1.0/skills/atlas-specs "/absolute/path/to/agent-skills/atlas-specs"
```

To run the bundled translator, use Python 3.11+ in the selected Python environment, then run from the installed skill directory:

```bash
cd "/absolute/path/to/agent-skills/atlas-specs"
python -m pip install -r scripts/requirements.txt
python scripts/atlas_translate.py formats
python scripts/atlas_translate.py validate assets/starter.atlas.json
```

Register or reload that directory according to the host's skill mechanism, then follow its `SKILL.md`. Merely reading this guide does not install the skill. The distributed skill is already built; consumers do not run `skills/build.py`.

## Maintain this edition

Keep root READMEs as illustrated introductions and edition READMEs as detailed textual manuals. Maintain the English source and its Portuguese translation together. Edit canonical implementation files in the edition, then regenerate affected reading formats and bundled skill files using that edition's documented helpers.

From `versioning/Alpha-v0.1.0/`, `python skills/build.py` synchronizes the portable skill and packaged schema/style copies. `python skills/build.py --check` detects drift without writing. Use the [verification guide](versioning/Alpha-v0.1.0/README.md#verification) to select checks relevant to the change and inspect rendered PDFs after publication changes.
