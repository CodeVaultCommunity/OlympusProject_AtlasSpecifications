# Visual assets · Atlas Specifications

[Português brasileiro](README.pt-br.md) · [Repository overview](../README.md) · [Edition manual](../versioning/Alpha-v0.1.0/README.md)

The Atlas identity uses the supplied Atlas emblem, the companion Olympus emblem and a navy, cyan and white palette. The header retains the celestial artwork, with a small Olympus icon beside the ecosystem name and a larger Atlas icon beside the project title. Both icons are also supplied as independent transparent PNG files. The header has 40-pixel rounded corners at its native 1600 × 534 size, with transparent outer corners in both SVG and PNG.

These shared presentation assets live at the repository root and illustrate the root READMEs. Version manuals provide detailed textual specifications and do not depend on these images; each edition can still be copied and used independently.

| Asset | English | Português |
| --- | --- | --- |
| Header | [PNG](atlas-banner-en.png) · [SVG](sources/atlas-banner-en.svg) | [PNG](atlas-banner-pt-br.png) · [SVG](sources/atlas-banner-pt-br.svg) |
| Model and representations | [PNG](atlas-model-en.png) · [SVG](sources/atlas-model-en.svg) | [PNG](atlas-model-pt-br.png) · [SVG](sources/atlas-model-pt-br.svg) |
| Specification composition | [PNG](atlas-content-en.png) · [SVG](sources/atlas-content-en.svg) | [PNG](atlas-content-pt-br.png) · [SVG](sources/atlas-content-pt-br.svg) |
| Translation | [PNG](atlas-translation-en.png) · [SVG](sources/atlas-translation-en.svg) | [PNG](atlas-translation-pt-br.png) · [SVG](sources/atlas-translation-pt-br.svg) |
| Atlas icon | [PNG](atlas-icon.png) | Shared, without text |
| Olympus icon | [PNG](olympus-icon.png) | Shared, without text |

## Edit and reproduce

Edit [render_images.py](sources/render_images.py), then run from the repository root:

```bash
python -m pip install cairosvg==2.9.1
python assets/sources/render_images.py
```

CairoSVG requires Cairo. DejaVu Sans is the reference font; install it to match the delivered typography. The delivered PNGs need neither dependency for viewing. The script writes the eight SVG/PNG pairs and restores the two public icon files from their unchanged originals. It does not call an image generator or download artwork. Each SVG embeds its raster inputs, so it remains portable on its own.

The six technical diagrams have a transparent canvas, opaque readable nodes, thicker arrows and native vector pictograms. Visible titles belong to the Markdown document rather than the image. The SVG title and accessibility label remain available to readers using assistive technology. Review both languages in light and dark themes after editing labels or geometry. Technical relationships and labels are authored in SVG; generated art carries no technical meaning.

## Original artwork and provenance

- [Atlas original](sources/atlas-icon-original.png): the image supplied by Douglas de Oliveira Alkimim. The file in `assets/atlas-icon.png` has identical bytes. It is raster artwork, not a vector source.
- [Olympus original](sources/olympus-icon-original.png): generated on 2026-10-25 as an illustrated companion to the supplied Atlas icon. Its visual brief was a Greek temple on Mount Olympus, with the same navy outlines, blue/cyan gradients, white highlights and transparent emblem silhouette. The file in `assets/olympus-icon.png` has identical bytes.
- [Celestial illustration](sources/atlas-hero-art.png): the decorative illustration generated on 2026-10-25 for the original header, retained unchanged. Its brief specified an armillary sphere above layered manuscript sheets, navy/cyan with restrained gold, and quiet space for separately authored typography. It does not encode a model, workflow or requirement.

Typography and diagrams are editable through the SVG sources and renderer. Reconstructing the banner does not redraw or recolor the original icons. The repository [license](../LICENSE) accompanies these assets.
