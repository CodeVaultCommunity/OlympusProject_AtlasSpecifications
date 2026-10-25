> Canonical English source: `implementations/latex/README.md`. This snapshot relocates links for standalone use. Follow SKILL.md for commands inside this bundle.

# Atlas LaTeX — Alpha-v0.1.0

English · Português brasileiro (edition source: `README.pt-br.md`) · [Edition manual](atlas-specification.md#implementations)

**Start here:** starter.atlas.tex (edition source: `starter.atlas.tex`). It carries the same draft content as the other two starters. Empty domain collections and open scope/source questions are intentional; passing structural validation does not establish a complete L1 specification. Follow the [authoring workflow](atlas-specification.md#quick-start) and consult the complete examples (edition source: `../../examples/README.md`).

Status: normative for this version. Profile identifier: `atlas-latex/Alpha-v0.1.0`. Style file: [`atlas.sty`](../scripts/vendor/atlas_spec/templates/atlas.sty).

Atlas LaTeX is the structured implementation for authoring and visual publication by compilation. It uses a controlled set of comments, environments, and commands. It is not arbitrary LaTeX.

## 1. Header and document

The first line is:

```text
% atlas:latex profile=atlas-latex representation=Alpha-v0.1.0 translator=0.1.0
```

The document uses `\documentclass{article}` (or a compatible class) and loads the Atlas style:

```text
\usepackage{atlas}
```

The example preamble uses:

- `iftex`; under pdfTeX `inputenc`/`fontenc`, otherwise `fontspec`;
- `geometry`, `graphicx`, `xcolor`, `booktabs`, `longtable`, `array`, `amsmath`, `tikz`, `hyperref`;
- `atlas.sty` additionally supplies its typography and layout through `lmodern` under pdfTeX, `microtype`, `needspace`, `fancyhdr`, `colortbl`, and `tcolorbox` with its `breakable` and `skins` libraries. It also uses `iftex`, `xcolor`, `graphicx`, `tikz`, `booktabs`, and `array`;
- TikZ libraries `shapes.geometric`, `arrows.meta`, and `positioning`, loaded by `atlas.sty`.

Immediately after loading `atlas`, the generated preamble includes optional local publication settings:

```text
\InputIfFileExists{atlas-presentation.tex}{}{}
```

This file is consumed by TeX during compilation. The Atlas decoder does not open it. The default style works without this file or any decorative image files. See [publication style](#publication-style) for the configuration template and its preservation scope.

The conditional preamble supports pdfLaTeX and provides a XeLaTeX/LuaLaTeX path for broader Unicode. Preamble support does not establish that every engine/font combination has been tested. See the edition’s [verification and publication guide](atlas-specification.md#verification).

## 2. Source authority

- Visible text environments are authoritative for prose.
- The commented structure appendix is authoritative for non-text data.
- Derived environments (`atlasderived`) and `% atlas:tikz` regions are derived presentation and are checked on import.
- Import reads the source file. It never extracts text from the PDF and never executes macros to discover meaning.
- Themes, ornamental cover artwork, and other purely decorative publication assets are outside the `atlas` payload. They are not semantic resources or additional JSON fields. An image that communicates a requirement, graph, entity, rule, or evidence remains a catalogued resource; styling cannot reclassify semantic content as decoration.

## 3. Text environments

| Environment | Arguments | Meaning |
| --- | --- | --- |
| `atlastitle` | text ID | Document title. |
| `atlasheading` | text ID, level | Heading 1–6. |
| `atlastext` | text ID | Paragraph/prose. |
| `atlasparagraph` | text ID | Paragraph block. |
| `atlasitem` | text ID | List item. |
| `atlasquote` | text ID | Quote. |
| `atlasnote` | text ID | Note. |
| `atlascode` | text ID | Literal code; `\obeylines\obeyspaces`. |
| `atlasformula` | text ID | Literal formula source. |
| `atlasderived` | derived ID | Generated summary/topology text. |

Shape:

```text
\begin{atlastext}{T000001}
...encoded content...
\end{atlastext}
```

The environment name, ID, and end marker are structure. Content starts after the line ending the begin line and ends before the line ending immediately preceding `\end{...}`; that last structural line ending is removed. Authored line endings inside content are preserved by the decoder.

## 4. Character encoding

Content is UTF-8. The following characters are encoded with unique macros:

| Character | Source form |
| --- | --- |
| `\` | `\AtlasCharBackslash{}` |
| `{` | `\AtlasCharLBrace{}` |
| `}` | `\AtlasCharRBrace{}` |
| `%` | `\AtlasCharPercent{}` |
| `#` | `\AtlasCharHash{}` |
| `&` | `\AtlasCharAmp{}` |
| `_` | `\AtlasCharUnderscore{}` |
| `$` | `\AtlasCharDollar{}` |
| `^` | `\AtlasCharCaret{}` |
| `~` | `\AtlasCharTilde{}` |

Inline table cells additionally encode newline as `\AtlasCharNewline{}` and tab as `\AtlasCharTab{}`. Other characters, including Unicode and ordinary spaces, remain literal. Decoding reverses the macros exactly. Because all backslashes are encoded, a literal `\end{atlastext}` cannot terminate an environment, and a literal `% atlas:...` cannot be mistaken for a marker.

The style defines each macro to typeset the intended character. Text remains human-readable in the PDF while the source is exactly recoverable.

## 5. Tables and inline cells

Rich tables are typeset from the structure. Cells use:

```text
\AtlasCell{T000042}{...encoded cell...}
```

The decoder extracts each cell macro with balanced braces and restores the text. The table layout itself is derived presentation; cell text is authoritative. Cell content is inline-escaped, so a newline is represented by `\AtlasCharNewline{}`.

The supplied renderer uses wrapping `longtable` columns and `booktabs` rules. A heading row can repeat on later PDF pages; each authoritative cell record still occurs only once in the source. Column widths, row styling, page breaks, and repeated visual headings do not create additional Atlas content.

## 6. Structure appendix

At the end:

```text
%
% atlas:structure:begin
% {
%   "document_id": "ATLAS-EX-MINIMAL",
%   "title": {"@text": "T000001"},
%   ...
% }
% atlas:structure:end
```

Every line is a LaTeX comment. The decoder removes `% ` (or `%`) and parses the JSON strictly. It restores text slots exactly as in Markdown. Missing/duplicate/orphan slots and unknown fields are errors. Declared `meta`, entity-example `data`, and `extensions` remain opaque structural values; literal `text`, `@text`, or `id` keys there are not Atlas slots or element declarations.

## 7. Derived regions and TikZ

### Derived text

```text
\begin{atlasderived}{DERIVED-SUMMARY}
Derived summary: ...
\end{atlasderived}
```

The content is encoded with the same character macros. The decoder regenerates the expected text and compares; an isolated edit is `ATL-E-DERIVED-STALE`.

### TikZ diagrams

Flow/state/relation graphs are rendered as TikZ between:

```text
% atlas:tikz:begin id=TIKZ-GRAPH-REQUEST-SUBMIT
\clearpage
... deterministic diagram and edge-key legend ...
\clearpage
% atlas:tikz:end id=TIKZ-GRAPH-REQUEST-SUBMIT
```

The TikZ source is generated deterministically from the graph and its label text. The decoder regenerates it and compares; an isolated edit is `ATL-E-TIKZ-STALE`. Every graph must have one `TIKZ-<graph-id>` region. The graph data, not the drawing, is authoritative.

TikZ layout is deterministic and bounded to the page width/height. Nodes use wrapped labels; arrows use short `E1`, `E2`, … keys with an exact edge-ID/label legend. The full structured node/edge listing remains authoritative. A very large graph can become small when scaled; authors can declare meaningful subflows to improve presentation. There is no fixed semantic limit on node/edge count. Every publication still requires visual inspection; a successful compile alone does not establish legibility.

## 8. Resources and figures

### Figures that carry specification content

A figure block uses `\includegraphics` with a PDF, PNG, or JPEG variant from the resource catalog. The original SVG remains the editable source and is preserved; the PNG/PDF is an explicit variant.

```text
\begin{figure}[htbp]
\centering
\includegraphics[width=0.62\linewidth]{assets/request-form.png}
\end{figure}
```

If no compilable variant exists, encoding rejects the document with `ATL-E-LATEX-RESOURCE`. Paths are relative to the document package root. Compilation does not fetch URLs and does not rewrite assets.

<a id="publication-style"></a>
### Publication style and decorative images

The default **editorial** style adds an illustrated cover, consistent typography, a restrained navy/cyan/teal palette, clearer section and field labels, page headers and footers, and styled notes and tables. Cover artwork is a self-contained vector ornament drawn by the style; it represents no Atlas graph or system behavior. The **plain** theme uses a white cover and subdued grayscale accents with the same document content. It changes the style palette; semantic images and generated graphs retain their own colors.

Generated documents place the authoritative title and optional subtitle inside a cover opened by `\AtlasBeginCover{document-id}{revision}{status}` and closed by `\AtlasEndCover`. The full metadata, authors, and specification follow. These cover commands arrange the publication; the title/subtitle environments and structural appendix remain the sources of authority. Page furniture and theme selection do not change those sources.

Use the same `atlas.sty` file for both themes. Copy [atlas-presentation.example.tex](../assets/atlas-presentation.example.tex) beside the generated document and rename the copy to `atlas-presentation.tex`. Keep the `.tex` document's directory as the working directory when compiling. The configuration template enables the default theme and leaves optional image paths commented out.

| Command | Placement | Effect |
| --- | --- | --- |
| `\AtlasTheme{editorial}` | `atlas-presentation.tex`, before `\begin{document}`. | Select the default illustrated style. |
| `\AtlasTheme{plain}` | Same settings file. | Select the restrained grayscale style. |
| `\AtlasCoverImage{presentation/cover.png}` | Same settings file. | Use a local decorative cover image. |
| `\AtlasDecorativeImage[width=0.55\linewidth]{presentation/ornament.png}` | Document body, between authoritative environments and before the structure appendix. | Typeset a local ornamental image with `graphicx` options. |

For example, the complete optional settings file can be:

```text
\AtlasTheme{editorial}
% Uncomment only after placing the local file beside this publication:
% \AtlasCoverImage{presentation/cover.png}
```

Only use these image commands for decoration: a cover texture, emblem, or visual divider that adds no requirements, entities, flow conditions, explanations, acceptance criteria, or evidence. Keep titles, captions with semantic meaning, author statements, and specification text in their authoritative records. Do not place Atlas text records, cells, structure data, or graph markers in the settings file; the importer never reads that file. Do not insert decoration into an authoritative text environment, a checked `atlasderived` region, or a checked `% atlas:tikz` region. The latter regions remain subject to their normal validation.

Decorative image paths are local publication paths, resolved when TeX compiles from the document directory. They require no resource ID, hash, `figure` block, or JSON entry. A missing configured cover image emits a TeX warning and falls back to the built-in vector ornament; a missing body decoration emits a warning and is omitted. Those presentation warnings are separate from the strict errors for missing semantic resources. Conversion does not open or fetch decorative files and does not execute the settings file.

**Conversion preserves specification content, not a custom publication layout.** LaTeX → JSON or Markdown omits the settings, decorative image commands, and their files. JSON or Markdown → LaTeX regenerates the default source layout, including the optional settings-file lookup; it does not recover a deleted theme file or custom image path. Keeping the same local settings file allows a regenerated document in that directory to use the same cover/theme when compiled. A body decoration inserted manually must be reapplied after regeneration.

The `package` command includes semantic resources and the supplied style; it does not copy `atlas-presentation.tex` or uncatalogued decorative artwork. To reproduce a custom publication in another folder, copy that settings file and its local artwork explicitly and inspect the rendered result. Their absence does not alter the decoded `atlas` payload or weaken semantic resource checks.

## 9. Compilation

The starter (edition source: `starter.atlas.tex`) is an actual document. `atlas.sty` is the supporting style package, not a document template. From the edition directory, compile the complete examples with:

```bash
python examples/build.py --pdf
```

The builder runs two pdfLaTeX passes with the local style available through `TEXINPUTS`. It retains an existing publication if compilation fails. Install the TeX packages listed in §1 through the selected TeX distribution. For a standalone document, copy `atlas.sty` beside its `.tex` file and run the following command twice from that document directory, replacing the filename with the actual document:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape specification.atlas.tex
```

Alternatively, add the absolute `implementations/latex` directory to `TEXINPUTS`, followed by the platform path separator (`:` on Unix; `;` on Windows) to retain TeX's default search path. Copy optional publication settings and artwork separately when preserving a custom design. These files are TeX publication inputs and are processed only by the compiler.

The translator itself never compiles a PDF. Compiling a document and reviewing the rendered pages are publication steps. Referenced resources must remain available relative to the package root.

## 10. Profile limits

- Arbitrary LaTeX outside the Atlas markers is ignored on import. It is never guessed into Atlas content.
- Macros in authored text are encoded, not executed.
- The structure appendix is required.
- PDF text extraction, page layout, font substitution, and pagination are not part of reversible conversion.
- Decorative artwork and local publication settings are intentionally excluded from conversion. Semantic figures and derived graph regions retain their existing preservation and validation obligations.
- The profile does not support every LaTeX package or construct. Unknown constructions in Atlas content are rejected by the schema; foreign presentation commands are outside the profile.
- Text records must be UTF-8; the source must be valid UTF-8 without BOM.
- The included examples use pdfLaTeX-compatible characters. XeLaTeX/LuaLaTeX may be needed for broader scripts.

## 11. Schematic shape

The abbreviated snippet illustrates delimiters; use the starter linked above for a valid complete file.

```text
% atlas:latex profile=atlas-latex representation=Alpha-v0.1.0 translator=0.1.0
\documentclass[11pt,a4paper]{article}
...
\usepackage{atlas}
\InputIfFileExists{atlas-presentation.tex}{}{}
\begin{document}
\AtlasBeginCover{ATLAS-EX-MINIMAL}{1}{draft}
\begin{atlastitle}{T000001}
Minimal request register
\end{atlastitle}
\AtlasEndCover
...
% atlas:structure:begin
% { ... }
% atlas:structure:end
\end{document}
```

Full instances: `examples/minimal/example.atlas.tex` (edition source: `../../examples/minimal/example.atlas.tex`), `examples/composition/example.atlas.tex` (edition source: `../../examples/composition/example.atlas.tex`). Compiled publications are the adjacent PDFs.
