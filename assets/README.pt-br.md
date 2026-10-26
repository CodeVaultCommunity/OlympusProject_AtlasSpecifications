# Recursos visuais · Atlas Specifications

[English](README.md) · [Apresentação do repositório](../README.pt-br.md) · [Manual da edição](../versioning/Stable-v1.0.0/README.pt-br.md)

A identidade do Atlas usa o emblema fornecido do Atlas, o emblema complementar do Olympus e uma paleta azul-marinho, ciano e branca. O cabeçalho mantém a arte celeste, com um ícone pequeno do Olympus ao lado do nome do ecossistema e um ícone maior do Atlas ao lado do título do projeto. Os dois ícones também são fornecidos como arquivos PNG transparentes independentes. O cabeçalho tem cantos arredondados de 40 pixels no tamanho original de 1600 × 534, com transparência nos cantos externos tanto no SVG quanto no PNG.

Esses recursos de apresentação compartilhados ficam na raiz do repositório e ilustram os READMEs externos. Os manuais das versões fornecem especificações detalhadas em texto e não dependem dessas imagens; cada edição continua podendo ser copiada e usada de forma independente.

| Recurso | English | Português |
| --- | --- | --- |
| Cabeçalho | [PNG](atlas-banner-en.png) · [SVG](sources/atlas-banner-en.svg) | [PNG](atlas-banner-pt-br.png) · [SVG](sources/atlas-banner-pt-br.svg) |
| Modelo e representações | [PNG](atlas-model-en.png) · [SVG](sources/atlas-model-en.svg) | [PNG](atlas-model-pt-br.png) · [SVG](sources/atlas-model-pt-br.svg) |
| Composição da especificação | [PNG](atlas-content-en.png) · [SVG](sources/atlas-content-en.svg) | [PNG](atlas-content-pt-br.png) · [SVG](sources/atlas-content-pt-br.svg) |
| Tradução | [PNG](atlas-translation-en.png) · [SVG](sources/atlas-translation-en.svg) | [PNG](atlas-translation-pt-br.png) · [SVG](sources/atlas-translation-pt-br.svg) |
| Ícone Atlas | [PNG](atlas-icon.png) | Compartilhado, sem texto |
| Ícone Olympus | [PNG](olympus-icon.png) | Compartilhado, sem texto |

## Editar e reproduzir

Edite [render_images.py](sources/render_images.py) e execute na raiz do repositório:

```bash
python -m pip install cairosvg==2.9.1
python assets/sources/render_images.py
```

CairoSVG depende de Cairo. DejaVu Sans é a fonte de referência; instale-a para reproduzir a tipografia entregue. Os PNGs entregues não precisam dessas dependências para visualização. O script grava os oito pares SVG/PNG e restaura os dois arquivos públicos de ícone a partir dos originais inalterados. Ele não chama um gerador de imagens nem baixa arte. Cada SVG incorpora suas entradas raster, podendo ser usado isoladamente.

Os seis diagramas técnicos têm canvas transparente, nós opacos legíveis, setas mais grossas e pictogramas vetoriais nativos. Os títulos visíveis ficam no documento Markdown, fora da imagem. O título SVG e o rótulo de acessibilidade continuam disponíveis para leitores que usam tecnologia assistiva. Revise os dois idiomas em temas claro e escuro após alterar textos ou geometria. Relações e rótulos técnicos são definidos em SVG; a arte gerada não contém significado técnico.

## Originais e origem da arte

- [Original Atlas](sources/atlas-icon-original.png): imagem fornecida por Douglas de Oliveira Alkimim. O arquivo `assets/atlas-icon.png` tem bytes idênticos. É uma arte raster, não uma fonte vetorial.
- [Original Olympus](sources/olympus-icon-original.png): gerado em 2026-10-25 como emblema ilustrado complementar ao ícone Atlas fornecido. A orientação visual foi um templo grego sobre o Monte Olimpo, com os mesmos contornos azul-marinho, gradientes azuis/ciano, destaques brancos e silhueta de emblema transparente. O arquivo `assets/olympus-icon.png` tem bytes idênticos.
- [Ilustração celeste](sources/atlas-hero-art.png): ilustração decorativa gerada em 2026-10-25 para o cabeçalho original, mantida sem alteração. A orientação foi uma esfera armilar sobre folhas em camadas, em azul-marinho/ciano com dourado discreto e espaço calmo para tipografia definida separadamente. A imagem não codifica modelo, fluxo ou requisito.

A tipografia e os diagramas podem ser editados pelas fontes SVG e pelo renderizador. Reconstruir o banner não redesenha nem recolore os ícones originais. A [licença](../LICENSE) do repositório acompanha esses recursos.
