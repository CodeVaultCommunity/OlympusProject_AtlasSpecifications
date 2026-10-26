# Claude entry point · Atlas Specifications

Use [AGENTS.md](AGENTS.md) as the repository navigation and maintenance guide. Select the edition through the root [version table](README.md#versions); the current edition is **Stable-v1.0.0**.

- **Normative model and contracts:** [versioning/Stable-v1.0.0/README.md](versioning/Stable-v1.0.0/README.md).
- **Portuguese translation:** [versioning/Stable-v1.0.0/README.pt-br.md](versioning/Stable-v1.0.0/README.pt-br.md).
- **Representation guides and starters:** the edition's `implementations/json/`, `implementations/markdown/`, and `implementations/latex/` directories.
- **Portable skill entry:** [versioning/Stable-v1.0.0/skills/atlas-specs/SKILL.md](versioning/Stable-v1.0.0/skills/atlas-specs/SKILL.md).

To install the skill, copy the complete `versioning/Stable-v1.0.0/skills/atlas-specs/` directory to the skills location configured for your Claude environment. Keep its `references/`, `scripts/`, `assets/`, and metadata together. [Installation instructions](AGENTS.md#locate-and-install-the-skill) include a copy command that refuses an existing destination and the bundled translator's dependency/setup commands.

Use the selected edition's model, translator, and skill together. Follow `SKILL.md` for authoring, auditing, conversion, and publication; consult `AGENTS.md` for canonical sources and maintenance checks. This file provides guidance and does not perform installation or configure the host.
