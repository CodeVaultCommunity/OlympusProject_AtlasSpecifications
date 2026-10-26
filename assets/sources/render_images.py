#!/usr/bin/env python3
"""Render bilingual Atlas banners and transparent technical diagrams.

Run from the repository root with ``python assets/sources/render_images.py``.
Requires CairoSVG. PNG artwork and icons are embedded unchanged into standalone
SVGs. Technical geometry, labels and typography are authored as native SVG.
"""
from __future__ import annotations

import base64
import html
from pathlib import Path
import cairosvg

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
NAVY, INK, MUTED = '#0b1d36', '#15314f', '#415e78'
BLUE, CYAN, TEAL, EDGE = '#1576cb', '#009db8', '#007786', '#297fbb'


def svg(width, height, body, title, clip_radius=None):
    clip = (f'<clipPath id="canvas-clip"><rect width="{width}" height="{height}" '
            f'rx="{clip_radius}" ry="{clip_radius}"/></clipPath>') if clip_radius else ''
    clip_attr = ' clip-path="url(#canvas-clip)"' if clip else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">
<title>{html.escape(title)}</title><defs>
<marker id="arrow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M1 1L11 6L1 11Z" fill="{EDGE}"/></marker>
<linearGradient id="brand-title" x1="0" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="0.56" stop-color="#e6faff"/><stop offset="1" stop-color="#67dbfa"/></linearGradient>
{clip}</defs><g font-family="DejaVu Sans,Arial,sans-serif"{clip_attr}>{body}</g></svg>'''


def text(x, y, value, size=24, color=INK, weight=400, anchor='start', **attrs):
    options = ''.join(f' {k.replace("_", "-")}="{html.escape(str(v))}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}"{options}>{html.escape(value)}</text>'


def lines(x, y, values, size=23, color=MUTED, gap=34, anchor='start'):
    return ''.join(text(x, y+i*gap, v, size, color, anchor=anchor) for i, v in enumerate(values))


def rect(x, y, w, h, fill='#ffffff', stroke='#9cc9df', radius=18):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'


def arrow(d, dashed=False):
    dash = ' stroke-dasharray="10 8"' if dashed else ''
    return f'<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"{dash}/>'


def tag(cx, cy, value, width, size=20):
    """Give edge labels an opaque surface readable in light and dark themes."""
    return rect(cx-width/2, cy-22, width, 40, '#f4fbff', '#c4dfed', 10) + text(cx, cy+5, value, size, INK, 500, 'middle')


def icon(kind, x, y, color=BLUE, size=40):
    shapes = {
        'layers': '<path d="M4 12L20 3L36 12L20 21Z"/><path d="M4 20L20 29L36 20M4 28L20 37L36 28"/>',
        'model': '<rect x="3" y="3" width="11" height="11" rx="2"/><rect x="26" y="3" width="11" height="11" rx="2"/><rect x="14" y="26" width="12" height="11" rx="2"/><path d="M8 14V20H32V14M20 20V26"/>',
        'document': '<path d="M9 3H25L33 11V37H9Z"/><path d="M25 3V11H33M15 18H27M15 25H27M15 32H23"/>',
        'code': '<path d="M12 9L2 20L12 31M28 9L38 20L28 31M24 3L16 37"/>',
        'entity': '<path d="M20 2L36 11V29L20 38L4 29V11ZM4 11L20 20L36 11M20 20V38"/>',
        'tool': '<path d="M25 3A11 11 0 0 0 12 17L3 29A5 5 0 0 0 11 36L23 24A11 11 0 0 0 37 12L29 18L22 11Z"/>',
        'case': '<circle cx="8" cy="9" r="5"/><path d="M2 25V22A6 6 0 0 1 14 22V25M22 5H37V15H22ZM22 25H37V35H22ZM15 21H29V15M29 21V25"/>',
        'evidence': '<rect x="8" y="5" width="26" height="32" rx="3"/><path d="M14 5V2H27V5M14 16L17 19L23 12M25 16H29M14 28L17 31L23 24M25 28H29"/>',
        'boundary': '<rect x="3" y="3" width="34" height="28" rx="4"/><path d="M3 12H37M13 37H27M20 31V37"/><circle cx="8" cy="8" r="0.7"/>',
        'check': '<circle cx="20" cy="20" r="17"/><path d="M10 20L17 27L30 12"/>',
        'compare': '<path d="M7 8H33M7 20H33M7 32H33"/><circle cx="7" cy="8" r="4" fill="#fff"/><circle cx="26" cy="20" r="4" fill="#fff"/><circle cx="14" cy="32" r="4" fill="#fff"/>',
        'stop': '<path d="M20 2L39 36H1ZM20 12V24"/><circle cx="20" cy="30" r="1"/>',
        'pdf': '<path d="M8 2H26L34 10V38H8ZM26 2V10H34M13 28L18 14L23 28M15 24H22M25 29H29"/>',
    }
    return f'<g transform="translate({x} {y}) scale({size/40})" fill="none" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'


def heading(x, y, label, kind, color=BLUE, size=27):
    return icon(kind, x, y-30, color) + text(x+58, y, label, size, color, 700)


def raster(name, x, y, width, height):
    payload = base64.b64encode((HERE/name).read_bytes()).decode('ascii')
    return f'<image x="{x}" y="{y}" width="{width}" height="{height}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{payload}"/>'


def banner(lang):
    b = f'<rect width="1600" height="534" fill="{NAVY}"/>' + raster('atlas-hero-art.png', 0, 0, 1600, 534)
    b += raster('olympus-icon-original.png', 70, 47, 66, 66)
    b += text(156, 91, 'OLYMPUS  /  OAL L1', 19, '#bddcec', 600, letter_spacing='0.8')
    b += raster('atlas-icon-original.png', 63, 151, 194, 194)
    b += text(287, 231, 'Atlas', 80, 'url(#brand-title)', 700, letter_spacing='-1.5')
    b += text(289, 301, 'Specifications', 54, 'url(#brand-title)', 600, letter_spacing='-1')
    subtitle = 'One abstract contract. Three representations.' if lang=='en' else 'Um contrato abstrato. Três representações.'
    b += text(78, 386, subtitle, 24, '#c0dce9')
    b += text(78, 434, 'JSON    ·    MARKDOWN    ·    LaTeX', 18, '#80e8ef', 600, letter_spacing='0.6')
    b += text(78, 487, 'Stable-v1.0.0', 16, '#afc6d7')
    return svg(1600, 534, b, 'Atlas Specifications · Olympus · Stable-v1.0.0', clip_radius=40)


def model(lang):
    en = lang == 'en'
    b = rect(60, 35, 1280, 130, '#eef7ff', '#84bce0')
    b += heading(92, 84, 'OAL L1 · UCS', 'layers', BLUE, 29)
    b += text(150, 131, 'Obligations for use-case specification models' if en else 'Obrigações para modelos de especificação de casos de uso', 24)
    b += arrow('M700 165V268') + tag(700, 216, 'Conformance' if en else 'Conformidade', 202)
    b += rect(235, 280, 930, 160, NAVY, '#1688b4')
    b += heading(275, 334, 'Atlas Specifications', 'model', '#85edf2', 32)
    b += lines(275, 379, ['Abstract concepts, relationships and obligations' if en else 'Conceitos, relações e obrigações abstratas', 'Preservation contract independent of a file format' if en else 'Contrato de preservação independente de formato de arquivo'], 24, '#e0eef8')
    b += arrow('M450 440V490H365V538') + arrow('M950 440V490H1035V538')
    b += tag(320, 490, 'Semantic mapping' if en else 'Mapeamento semântico', 280)
    b += tag(1080, 490, 'Concrete encoding' if en else 'Representação concreta', 280)
    b += rect(60, 550, 610, 185)
    b += heading(86, 599, 'Implementing models' if en else 'Modelos implementadores', 'model', BLUE, 25)
    b += lines(90, 648, ['Declare a mapping and their own constraints.' if en else 'Declaram mapeamento e restrições próprias.', 'Preserve the applicable Atlas obligations.' if en else 'Preservam as obrigações aplicáveis do Atlas.'], 23)
    b += rect(730, 550, 610, 185, '#f0fcfc', '#8acdd2')
    b += heading(756, 599, 'Representation implementations' if en else 'Implementações de representação', 'code', TEAL, 24)
    b += lines(760, 648, ['Atlas JSON · Atlas Markdown · Atlas LaTeX', 'Encode the same semantic content.' if en else 'Codificam o mesmo conteúdo semântico.'], 23)
    b += arrow('M365 735V790H520V848') + arrow('M1035 735V790H880V848')
    b += tag(335, 790, 'Instantiation' if en else 'Instanciação', 200) + tag(1065, 790, 'Representation' if en else 'Representação', 204)
    b += rect(210, 860, 980, 125, '#eef7ff', '#84bce0')
    b += heading(245, 909, 'Concrete project artifacts' if en else 'Artefatos concretos de projeto', 'document', BLUE, 27)
    b += text(245, 954, 'Instantiate a selected model; may use several representations.' if en else 'Instanciam um modelo escolhido; podem ter várias representações.', 24)
    return svg(1400, 1020, b, 'OAL, the abstract Atlas model, implementing models, representations and project artifacts' if en else 'OAL, modelo abstrato Atlas, modelos implementadores, representações e artefatos de projeto')


def content(lang):
    en = lang == 'en'
    b = rect(55, 35, 530, 175) + heading(85, 87, 'Entities' if en else 'Entidades', 'entity', BLUE, 29)
    b += lines(85, 137, ['Meaning, identity and intrinsic invariants' if en else 'Significado, identidade e invariantes', 'Canonical rules of validity' if en else 'Regras canônicas de validade'], 23)
    b += rect(815, 35, 530, 175) + heading(845, 87, 'Abstract tools' if en else 'Ferramentas abstratas', 'tool', BLUE, 28)
    b += lines(845, 137, ['Inputs, outcomes and guarantees' if en else 'Entradas, resultados e garantias', 'Operate on ready entities' if en else 'Operam sobre entidades prontas'], 23)
    b += arrow('M815 135H598') + tag(700, 93, 'Operate on' if en else 'Operam sobre', 190)
    b += rect(55, 355, 815, 240, NAVY, '#1688b4') + heading(87, 411, 'Use cases' if en else 'Casos de uso', 'case', '#85edf2', 31)
    b += lines(88, 463, ['Initiating actor, caller context and authorization' if en else 'Ator iniciador, contexto do chamador e autorização', 'Functional requirements and structured flows' if en else 'Requisitos funcionais e fluxos estruturados', 'Behavior, effects, failures and observable acceptance' if en else 'Comportamento, efeitos, falhas e aceite observável'], 24, '#e0eef8', 39)
    b += arrow('M760 355V277H1080V223') + tag(946, 277, 'Invoke' if en else 'Invocam', 146)
    b += rect(940, 355, 405, 545, '#f0fcfc', '#8acdd2') + heading(968, 410, 'Shared evidence' if en else 'Evidências comuns', 'evidence', TEAL, 25)
    for idx, s in enumerate(['Stable IDs and references' if en else 'IDs e referências estáveis', 'Quality + acceptance' if en else 'Qualidade + aceite', 'Identified sources' if en else 'Fontes identificadas', 'Assumptions + open issues' if en else 'Premissas + pendências', 'Version + history' if en else 'Versão + histórico', 'Resource provenance' if en else 'Origem dos recursos']):
        y = 475+idx*68
        b += f'<circle cx="972" cy="{y-7}" r="4" fill="{CYAN}"/>' + text(990, y, s, 22)
    b += arrow('M940 505H884', True)
    b += rect(55, 750, 815, 150) + heading(87, 800, 'Interaction boundaries' if en else 'Fronteiras de interação', 'boundary', BLUE, 28)
    b += lines(88, 843, ['Externally imposed interaction constraints: L1' if en else 'Restrições de interação impostas externamente: L1', 'Solution-introduced channels: L4' if en else 'Canais introduzidos pela solução: L4'], 23, gap=32)
    b += arrow('M455 750V608') + tag(455, 674, 'Expose cases' if en else 'Expõem casos', 220)
    return svg(1400, 940, b, 'Entities, tools, use cases, interaction boundaries and shared evidence' if en else 'Entidades, ferramentas, casos de uso, fronteiras de interação e evidências comuns')


def translation(lang):
    en = lang == 'en'
    b = rect(40, 35, 325, 250) + heading(68, 88, 'Source' if en else 'Origem', 'document', BLUE, 27)
    b += lines(70, 147, ['Atlas JSON', 'Atlas Markdown', 'Atlas LaTeX'], 26, INK, 44)
    b += rect(515, 35, 370, 250, NAVY, '#1688b4') + heading(544, 88, 'Intermediate' if en else 'Intermediário', 'code', '#85edf2', 26)
    b += text(547, 160, 'Atlas JSON', 34, '#ffffff', 700)
    b += lines(548, 210, ['Validated content' if en else 'Conteúdo validado', 'in memory' if en else 'em memória'], 24, '#d6edf8', 32)
    b += rect(1035, 35, 325, 250) + heading(1063, 88, 'Encoded target' if en else 'Destino codificado', 'document', BLUE, 21)
    b += lines(1065, 147, ['Atlas JSON', 'Atlas Markdown', 'Atlas LaTeX'], 26, INK, 44)
    b += arrow('M365 177H502') + arrow('M885 177H1022')
    b += tag(440, 110, 'Decode' if en else 'Decodificar', 138, 18) + tag(440, 220, '+ validate' if en else '+ validar', 138, 18)
    b += tag(960, 125, 'Encode' if en else 'Codificar', 135, 19)
    b += arrow('M700 285V438') + tag(700, 362, 'Source content' if en else 'Conteúdo de origem', 256)
    b += arrow('M1197 285V525H958') + tag(1197, 362, 'Decode + validate' if en else 'Decodificar + validar', 284)
    b += rect(445, 450, 510, 155, '#f0fcfc', '#8acdd2') + heading(472, 504, 'Compare Atlas content' if en else 'Comparar conteúdo Atlas', 'compare', TEAL, 25)
    b += lines(475, 552, ['Exact text · IDs · order · types' if en else 'Texto exato · IDs · ordem · tipos', 'Graphs · resources · extensions' if en else 'Grafos · recursos · extensões'], 23, gap=33)
    b += arrow('M700 605V645')
    b += f'<path d="M700 657L840 732L700 807L560 732Z" fill="#eef7ff" stroke="{BLUE}" stroke-width="3"/>' + text(700, 741, 'Equal?' if en else 'Igual?', 30, BLUE, 700, 'middle')
    b += arrow('M560 732H265V848') + arrow('M840 732H1135V848')
    b += tag(420, 732, 'No' if en else 'Não', 78) + tag(980, 732, 'Yes' if en else 'Sim', 78)
    b += rect(40, 860, 450, 137, '#fff5ef', '#d4a892') + heading(68, 910, 'Stop and diagnose' if en else 'Parar e diagnosticar', 'stop', '#974f30', 26)
    b += text(70, 953, 'No output accepted on failure' if en else 'Sem saída aceita em caso de falha', 22)
    b += rect(910, 860, 450, 137, '#f0fcfc', '#8acdd2') + heading(938, 910, 'Write verified output' if en else 'Gravar saída verificada', 'check', TEAL, 25)
    b += text(940, 953, 'Preserve resource bytes' if en else 'Preservar bytes dos recursos', 22)
    b += arrow('M1135 997V1080') + tag(1135, 1040, 'LaTeX only' if en else 'Somente LaTeX', 210)
    b += rect(910, 1092, 450, 100) + heading(938, 1151, 'PDF publication' if en else 'Publicação PDF', 'pdf', BLUE, 27)
    return svg(1400, 1222, b, 'Decode, validate, encode, re-read and compare content before writing; optional PDF publication from LaTeX' if en else 'Decodificar, validar, codificar, reler e comparar o conteúdo antes de gravar; publicação PDF opcional a partir do LaTeX')


def write(name, source):
    (HERE/f'{name}.svg').write_text(source, encoding='utf-8')
    cairosvg.svg2png(bytestring=source.encode(), write_to=str(OUT/f'{name}.png'))
    print(f'assets/{name}.png')


def main():
    OUT.mkdir(exist_ok=True)
    for name in ('atlas', 'olympus'):
        (OUT/f'{name}-icon.png').write_bytes((HERE/f'{name}-icon-original.png').read_bytes())
    for lang in ('en', 'pt-br'):
        write(f'atlas-banner-{lang}', banner(lang))
        write(f'atlas-model-{lang}', model(lang))
        write(f'atlas-content-{lang}', content(lang))
        write(f'atlas-translation-{lang}', translation(lang))


if __name__ == '__main__':
    main()
