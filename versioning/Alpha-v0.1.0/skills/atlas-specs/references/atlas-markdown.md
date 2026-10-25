> Canonical English source: `implementations/markdown/README.md`. This snapshot relocates links for standalone use. Follow SKILL.md for commands inside this bundle.

# Atlas Markdown — Alpha-v0.1.0

English · Português brasileiro (edition source: `README.pt-br.md`) · [Edition manual](atlas-specification.md#implementations)

**Start here:** starter.atlas.md (edition source: `starter.atlas.md`). It carries the same draft content as the other two starters. Empty domain collections and open scope/source questions are intentional; passing structural validation does not establish a complete L1 specification. Follow the [authoring workflow](atlas-specification.md#quick-start) and consult the complete examples (edition source: `../../examples/README.md`).

Status: normative for this version. Profile identifier: `atlas-markdown/Alpha-v0.1.0`.

Atlas Markdown is the readable textual implementation. It is intended for direct reading and for supplying the raw document to agents. It is a controlled profile, not arbitrary Markdown.

## 1. Source authority

- The visible **text records** are authoritative for prose.
- The **structure appendix** is authoritative for non-text data.
- Displayed labels, headings generated around records, summaries, topology text, and diagrams are derived presentation and are checked or ignored as stated below.
- Text is never read from the appendix. Structure is never guessed from prose.

A visible edit to a text record is imported. A visible edit outside text records does not create content; a derived region edit is diagnosed.

## 2. File header

The first Atlas marker must be:

`````text
<!-- atlas:markdown profile=atlas-markdown representation=Alpha-v0.1.0 translator=0.1.0 -->
`````

The representation version must match the adapter. A mismatch is rejected. The translator version is informational.

## 3. Text records

A text record has a start marker, exact content, and an end marker:

`````text
<!-- atlas:text id=T000001 role=paragraph -->
Exact text
<!-- /atlas:text id=T000001 -->
`````

Marker attributes:

| Attribute | Required | Values |
| --- | --- | --- |
| `id` | Yes | `T` followed by six digits; unique in the document. |
| `role` | Yes | `heading`, `paragraph`, `note`, `quote`, `list-item`, `code`, `formula`, `table-cell`. |
| `level` | For headings | 1–6. |
| `ordered` | For list items | `yes` or `no` (presentation hint). |

### Content boundaries

Content begins immediately after the newline that ends the start marker and ends at the start of the line containing the end marker. The one line ending immediately before the end marker is structural and is removed. Therefore:

- content `abc` is written as `abc` then the structural newline;
- content `abc\n` has an additional blank line before the end marker;
- content `""` has no content line before the end marker.

Authored CRLF/LF/CR inside the content are preserved exactly. The codec does not normalize line endings.

### Prefix syntax

- A heading record's content starts with `#` repeated `level` times and one space. The decoder removes exactly that prefix.
- A list-item record's content starts with `- ` or `1. `. The decoder removes exactly that prefix.
- Other roles have no prefix.

If a heading/list prefix is absent, decoding fails rather than guessing. The prefix is representation syntax, not authored text.

### Escaping marker-like content

If a content line begins with optional backslashes followed by `<!-- atlas:` or `<!-- /atlas:`, the encoder prefixes an additional backslash. The decoder removes one leading backslash from such lines. This preserves literal Atlas-like comments and closing markers inside authored text. Example:

`````text
\<!-- atlas:text id=T999999 role=paragraph -->
`````

decodes to:

`````text
<!-- atlas:text id=T999999 role=paragraph -->
`````

No other escaping is applied to Markdown text. Backslashes, fences, pipes, HTML, and Unicode remain as authored.

## 4. Block presentation

Every declared human text record is externalized once. Rich block structure is in the structure appendix; the body provides one record for each such text value. Structural strings (IDs, enums, paths and raw example data) remain structural. Declared `meta`, entity-example `data`, and `extensions` containers are opaque and stay in the appendix even if their own data happens to use a key named `text`, `@text`, or `id`; their complete values and types are still preserved.

| Block | Markdown presentation |
| --- | --- |
| `paragraph`, `note`, `quote` | One record with the matching role. |
| `heading` | One record with a Markdown heading prefix. |
| `list` | One record per item (`- ` or `1. `), children follow; structure in appendix. |
| `code` | One record with role `code`; content is raw and is not fenced automatically. |
| `formula` | One record with role `formula`; source is raw and is not executed. |
| `figure` | A visible resource reference plus caption/alternative-text records. No binary is embedded. |
| `table` | Column and cell text records with labels; the Markdown file does not use a pipe table as the authoritative form. LaTeX renders the table. |

The body may also contain derived headings/labels such as `## Document metadata` or `**Name**`. These are presentation. Only marked text records are imported.

## 5. Structure appendix

The last structural part of the file is:

`````text
<!-- atlas:structure:begin -->
````atlas-structure
{ ... JSON skeleton ... }
````
<!-- atlas:structure:end -->
`````

The fenced block contains the Atlas payload with every text value replaced by `{"@text": "T…"}`. It keeps all non-text data, including IDs, references, enums, booleans, numbers, graph topology, resource catalogs, extensions, and orders. The fence uses four backticks; serialized JSON cannot contain a raw line break inside a string, so a line equal to the closing fence is not produced from content.

Decoding:

1. collect text records;
2. parse the structure JSON strictly (duplicate keys rejected);
3. restore text into slots;
4. reject missing, duplicate, orphan, or unknown slots;
5. validate the complete Atlas document;
6. verify derived regions.

The appendix is not a second copy of the profile's text records and cannot override body text. Structural string values and opaque metadata/example/extension data are not prose slots.

## 6. Derived regions

### Summary and topology

`````text
<!-- atlas:derived id=DERIVED-SUMMARY -->
Derived summary: 5 sections; ...
<!-- /atlas:derived id=DERIVED-SUMMARY -->
`````

Graph topology regions use `DERIVED-GRAPH-<graph-id>`. They contain no authored text records. The decoder regenerates the expected text from the current structure and compares exactly. Editing one produces `ATL-E-DERIVED-STALE` and instructions to regenerate.

### TikZ

TikZ is a LaTeX-only derived region. See [the LaTeX profile](atlas-latex.md).

## 7. Metadata placement

- Document identity/version metadata is small and appears in generated metadata lines near the top.
- Text metadata (`id`, `nature`, `review_status`, `meta`) lives in the structure appendix as part of the `@text` placeholder; the body carries the text.
- Element IDs and structural values appear near their elements as derived presentation; the appendix is authoritative.
- No huge header of opaque JSON precedes the readable text.

## 8. Nesting and references

- Text records do not nest.
- A start marker without a matching end marker is an error.
- A nested text start inside a text record is an error.
- A record inside a derived region is an error.
- IDs are references; visual position and nesting are not.
- The appendix preserves all array orders.

## 9. Structured data that does not fit prose

Use the structure appendix for tables, graph data, mappings, resource catalogs, and lists of IDs. The body must still carry every text value. Do not encode prose only in appendix JSON.

## 10. Collisions and malformed markers

- Atlas marker lines inside content are escaped as described above.
- An unknown `<!-- atlas:` or `<!-- /atlas:` marker outside a text/derived/structure region is rejected.
- Duplicate text record IDs, mismatched start/end IDs, duplicate structure appendices, and missing appendices are rejected.
- A content line that looks like a closing marker with the current ID is escaped on encoding; if hand-written unescaped, it terminates the record and the following mismatch is diagnosed.

## 11. Limits

- This is not a generic Markdown importer. Only marked records and the structure appendix are read.
- Autofences are not added around code; use the structure's code block and the record role.
- Rich tables are represented as cell records in Markdown, not as rendered pipe tables.
- A derived edit requires regeneration; it is not merged.
- The text record prefix syntax is part of the profile and must be respected.

## 12. Schematic shape

The abbreviated snippet illustrates delimiters; use the starter linked above for a valid complete file.

`````text
<!-- atlas:markdown profile=atlas-markdown representation=Alpha-v0.1.0 translator=0.1.0 -->

<!-- atlas:text id=T000001 role=heading level=1 -->
# Minimal request register
<!-- /atlas:text id=T000001 -->

<!-- atlas:text id=T000002 role=paragraph -->
The register retains requests identified by code.
<!-- /atlas:text id=T000002 -->

...

<!-- atlas:structure:begin -->
````atlas-structure
{ "document_id": "ATLAS-EX-MINIMAL", "title": {"@text": "T000001"}, ... }
````
<!-- atlas:structure:end -->
`````

Full instances: `examples/minimal/example.atlas.md` (edition source: `../../examples/minimal/example.atlas.md`), `examples/composition/example.atlas.md` (edition source: `../../examples/composition/example.atlas.md`).
