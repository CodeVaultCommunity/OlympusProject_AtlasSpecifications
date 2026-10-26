> Canonical English source: `COMPATIBILITY.md`. This snapshot relocates links for standalone use. Follow SKILL.md for commands inside this bundle.

# Stable surface and compatibility

Português (edition source: `COMPATIBILITY.pt-br.md`) · [Normative manual](atlas-specification.md#versioning)

English is normative. Stable identifies a contract, not publication or stakeholder approval.

| Identity / operation | Contract |
| --- | --- |
| Model / profile | Both exactly `Stable-v1.0.0`. |
| Representation declaration | `atlas-json/Stable-v1.0.0`; Markdown/LaTeX headers declare `representation=Stable-v1.0.0`. |
| Implementation / new producer | Package `atlas-spec` and producer of newly authored documents: `1.0.0`. |
| Existing producer / revision / history | Authored data; preserved exactly by conversion, even if producer differs from the running package. |
| Stable input → Stable representation | Supported in all six directions under the preservation/resource contract. |
| Alpha input → Stable runtime | Rejected with explicit version diagnostics. Use the preserved Alpha edition and its own runtime for Alpha documents. |
| Alpha → Stable content | Separate editorial migration with source, destination, accountable person, intended changes and revision. No generic migrator is supplied. |
| Other / future model or profile | Unsupported unless explicitly implemented and documented. No promise of interoperability with another major version. |
| PDF | Publication only; no reverse import or payload equality claim. |

## Stable public surface

The [manual](atlas-specification.md#abstract-model), three [profile grammars](atlas-specification.md#implementations), JSON Schema and canonical LaTeX macros define model and representation obligations. Exact text, absent/null/empty distinctions, opaque data and resource preservation are included.

The CLI's `formats`, `validate`, `convert` and `package` commands, documented arguments/options and exit meanings are public. See the CLI guide (edition source: `translator/README.md`). Success is 0; diagnosed Atlas errors and invalid command usage return 2. Human-readable diagnostic wording and progress output are not machine protocols.

The public Python exports are `ALL_FORMATS`, `FUNDAMENTAL`, `SUPPORTED_PROFILE_VERSION`, `SUPPORTED_SPEC_VERSION`, `Adapter`, `AdapterRegistry`, `AtlasError`, `AtlasParseError`, `AtlasValidationError`, `AtlasVersionError`, `DecodeOptions`, `Diagnostic`, `EncodeOptions`, `JsonAdapter`, `LatexAdapter`, `MarkdownAdapter`, `Validator`, `default_registry`, `validate_document`, and `atlas_content_equal`, plus package `__version__`. Their documented signatures, options and behavior are the API contract. Private helpers and internal module layout are not extension contracts. The [diagnostic catalog](diagnostics.md) identifies stable codes and their meanings; diagnostic ordering and precise locations may improve without changing a code's meaning.

## Evolution policy

Incompatible model semantics, accepted-language changes that reject previously valid content, removed commands/options/APIs, incompatible signatures, or changed diagnostic meanings require a major version and an explicit migration policy. New mandatory semantic constraints are incompatible, even if implemented in a validator.

Compatible optional additions require a minor version and a declared capability/profile where representation changes are involved. An older runtime need not recognize a newly selected profile. Patch releases correct implementation defects without changing the contract. Rejecting a reference that was already invalid under the published rules is an implementation correction; inventing a new domain restriction is not. New reversible spellings in this edition belong to its new Stable profile and are not retroactively added to Alpha.

Package versions describe implementation evolution. Model/profile identities select contracts independently; package updates must not silently relabel payloads. A document revision records authored changes rather than codec executions. Historical versions remain addressable by their own edition directories.

The supplied starter and three examples record an explicit Alpha revision 1 → Stable revision 2 migration in `HIST-MIGRATION-STABLE`. The migration ledger (edition source: `verification/editorial-migration.json`) retains input hashes and responsibility; the task-board revision demonstration (edition source: `examples/task-board/revisions/README.md`) is a separate revision 2 → 3 change.

Before formal migration acceptance, identify the accountable person explicitly; a requester or tool is not automatically that person. An unconfirmed candidate records `responsibility_status: pending_confirmation`, `responsible_person: null` and no human approval claim. Presentation-only evolution accepts both the original Stable TikZ form and the current compact form, each regenerated exactly from its graph; arbitrary edits still fail.
