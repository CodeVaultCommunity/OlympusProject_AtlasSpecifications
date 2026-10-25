# Atlas JSON — Alpha-v0.1.0

English · [Português brasileiro](README.pt-br.md) · [Edition manual](../../README.md#implementations)

**Start here:** [starter.atlas.json](starter.atlas.json). It carries the same draft content as the other two starters. Empty domain collections and open scope/source questions are intentional; passing structural validation does not establish a complete L1 specification. Follow the [authoring workflow](../../README.md#quick-start) and consult the [complete examples](../../examples/README.md).

Status: normative for this version. Schema: [`atlas.schema.json`](atlas.schema.json). Profile identifier: `atlas-json/Alpha-v0.1.0`.

Atlas JSON is the structured implementation used for manipulation, validation, integration, and transformation. It is also the translator intermediate. It is **not** the abstract model.

## 1. Document envelope

```json
{
  "$schema": "atlas.schema.json",
  "format": "atlas-json/Alpha-v0.1.0",
  "atlas": { "...": "..." }
}
```

| Member | Required | Meaning |
| --- | --- | --- |
| `$schema` | No | Transport metadata pointing to the schema. Not Atlas content. |
| `format` | Yes | Must be exactly `atlas-json/Alpha-v0.1.0`. Not Atlas content. |
| `atlas` | Yes | The complete Atlas content. |

Unknown top-level members are rejected. Unknown members at schema-defined object levels are rejected. Declared open containers such as text `meta`, entity-example `data`, and `extensions` retain their schema-defined behavior. Their contents are opaque to slot/ID interpretation and preserved with their values and types, not silently discarded.

## 2. Atlas payload

Required members (see the schema for full constraints):

- identity and metadata: `document_id`, `title`, `revision`, `spec_version`, `profile_version`, `translator_version`, `language`, `status`, `authors`, `created`, `updated`;
- optional: `subtitle` (text or `null`), `keywords`, `notes`;
- editorial: `structure`;
- concepts: `actors`, `vocabulary`, `types`, `entities`, `tools`, `use_cases`, `boundaries`;
- structured material: `graphs`, `resources`;
- records: `assumptions`, `decisions`, `open_issues`, `sources`, `history`;
- configuration and extension: `presentation`, `extensions`.

All core collections listed above under editorial content, concepts, structured material and records are required. An empty array means “declared and empty”; an absent array is invalid. `subtitle` is optional and may be `null` or a text record; these are distinct states.

## 3. Text records

```json
{"text": "Exact characters, including  trailing spaces and\nauthored breaks."}
```

Optional text metadata: `id`, `nature`, `review_status`, `meta`, `extensions`.

- `text` must be a string. It can be empty.
- The model never trims or normalizes it.
- `nature` and `review_status` are independent.
- A missing text member is not an empty string.

Rich blocks are arrays of objects. See [the abstract model §5](../../README.md#model-5) and the schema for block types. Figure references, table structure, list structure and other structural members remain in their declared fields; authored captions and cells remain text records.

## 4. Identity

ID pattern:

```text
[A-Z][A-Z0-9]*(-[A-Z0-9]+)+
```

All element IDs are globally unique, including nested field, condition, operation, node, and edge IDs. `document_id` shares the namespace. IDs are never derived from array position. References are ID strings, not indexes.

## 5. Ordering

JSON object member order is not meaningful. Array order is meaningful:

| Array | Order meaning |
| --- | --- |
| `structure` | Authoritative presentation order of sections. |
| `section.items` | Presentation order of concept elements inside a section. |
| `blocks`, `list.items`, list `children` | Authored text order. |
| Every concept array | Authoring order; it does not replace `structure.items`. |
| `graphs[].nodes`, `graphs[].edges` | Graph authoring/rendering order. |
| `columns`, `rows` | Table order. |
| `resources` | Catalog order. |
| `history` | Declared history order. |

The validator requires every actor/term/type/entity/tool/use case/boundary to occur exactly once in `structure`.

## 6. Validation

Validation is layered:

1. **JSON loading** — UTF-8 without BOM, duplicate keys rejected, binary floats and non-finite constants rejected.
2. **JSON Schema 2020-12** — types, required members, unknown members, enum values, patterns.
3. **Referential and semantic rules** — ID uniqueness, reference resolution, editorial placement, graph owners/calls/edges, RF/list/graph consistency, RNF sharing, boundary RF ownership, resource paths/hashes/freshness, embedded-image text.

Run:

```bash
atlas-spec validate file.atlas.json
atlas-spec validate file.atlas.json --resources path/to/package
```

`--no-check-resources` skips file existence/size/hash checks; the document is still structurally and referentially validated. These checks do not prove that actor-context prose, requirement origins, acceptance criteria or business contracts are semantically sufficient; review them against the abstract model separately.

## 7. Unknown data and extensions

Unknown members at known object levels are rejected. Declared extension data belongs under an `extensions` object:

```json
"extensions": {
  "example.org/custom": {
    "text": "opaque to the translator",
    "values": [1, 2, 3]
  }
}
```

Extensions are preserved as JSON data across Markdown and LaTeX. The translator does not interpret them. They cannot replace required content or change the declared version. A format that cannot preserve an extension must reject the document.

## 8. Invalid and unsupported cases

| Case | Result |
| --- | --- |
| Duplicate JSON key | `ATL-E-DUPLICATE-KEY` |
| Binary float | `ATL-E-FLOAT` |
| Duplicate ID | `ATL-E-DUPLICATE-ID` |
| Missing/unknown reference | `ATL-E-REF` |
| Element not placed in structure | `ATL-E-STRUCTURE-MISSING` |
| Duplicate placement | `ATL-E-STRUCTURE-DUPLICATE` |
| Unknown block/construct | `ATL-E-SCHEMA` |
| Missing required text | `ATL-E-SCHEMA` |
| Graph edge endpoint missing | `ATL-E-GRAPH-EDGE` |
| Graph call target missing | `ATL-E-GRAPH-CALL` |
| RF list/graph divergence | `ATL-E-RF-FLOW` / `ATL-E-RF-GRAPH` |
| Unsupported version | `ATL-E-VERSION` / `ATL-E-PROFILE-VERSION` |
| Resource missing/hash/size | `ATL-E-RESOURCE-*` |
| Stale graph-derived figure | `ATL-E-FIGURE-STALE` |

## 9. Conversion

JSON is the only intermediate. JSON → Markdown/LaTeX externalizes text records and the structural skeleton; decoding restores and validates the same JSON. JSON → JSON through a file is a normal decode/encode and must be content-identical.

A conversion does not migrate versions, normalize text, update resources, fetch URLs, compile PDFs, or silently drop unknown fields.

## 10. Numeric values

Content numbers are integers. Decimal targets (for example, an RNF target) are strings such as `"2"` or `"0.5"` to preserve exact spelling and avoid binary floating-point loss. Entity example `data` may contain JSON integers, booleans, strings, nulls, arrays, and objects; binary floats are rejected by the strict loader.

## 11. Example

See [`examples/minimal/example.atlas.json`](../../examples/minimal/example.atlas.json) and [`examples/composition/example.atlas.json`](../../examples/composition/example.atlas.json).

## 12. Semantic authoring obligations

The schema does not exhaust the abstract model. Follow [the implementation guide](../../README.md#implementations) and [abstract model](../../README.md#abstract-model) for initiating actor/context and authorization, individual obligation origins, L1/L4 boundary classifications and accountable Needs-to-L1 claims. These subjects use the existing text/source/trace fields; no invented extension is required. The [task-board instance](../../examples/task-board/example.atlas.json) demonstrates these conventions.
