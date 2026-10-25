# Exemplos do Atlas Specifications

[English](README.md) · [Guia da versão](../README.pt-br.md) · [Implementações](../implementations/json/README.pt-br.md)

Estes são **exemplos sintéticos de especificação**, não aplicações de negócio em execução. Regras de produto, políticas de atores e condições de qualidade são escolhas didáticas identificadas. Os arquivos demonstram conteúdo Atlas e preservação entre representações; passar no validador documental não comprova o comportamento da aplicação descrita.

## Escolha um exemplo

| Exemplo | Finalidade | Identidades estáveis dos casos | Representações |
| --- | --- | --- | --- |
| [Quadro de tarefas](task-board/README.pt-br.md) | Referência principal: criar, concluir e listar; contexto do chamador, entidades prontas, persistência atômica e resultado incerto de escrita. | `UC-TASK-CREATE`, `UC-TASK-COMPLETE`, `UC-TASK-LIST` | [JSON](task-board/example.atlas.json), [Markdown](task-board/example.atlas.md), [LaTeX](task-board/example.atlas.tex), [PDF](task-board/example.atlas.pdf) |
| [Registro de solicitações](minimal/README.pt-br.md) | Exemplo menor com imagens locais, validade canônica dos campos, recusa de duplicidade e aceite vinculado à origem. | `UC-REQUEST-SUBMIT` | [JSON](minimal/example.atlas.json), [Markdown](minimal/example.atlas.md), [LaTeX](minimal/example.atlas.tex), [PDF](minimal/example.atlas.pdf) |
| [Composição de reservas](composition/README.pt-br.md) | Entidade e ferramenta compartilhadas, composição de casos, obrigação de qualidade canônica e transição de estado. | `UC-BOOKING-LOOKUP`, `UC-BOOKING-CREATE`, `UC-BOOKING-CANCEL` | [JSON](composition/example.atlas.json), [Markdown](composition/example.atlas.md), [LaTeX](composition/example.atlas.tex), [PDF](composition/example.atlas.pdf) |

JSON, Markdown e LaTeX transportam o mesmo conteúdo Atlas. PDF é uma publicação compilada do LaTeX, não uma quarta implementação editável. Diagramas técnicos são visões derivadas; os registros dos grafos preservam nós, arestas, rótulos, chamadas e referências de requisitos. A publicação padrão também tem uma capa vetorial decorativa desenhada por `atlas.sty`; esse ornamento não carrega informação da especificação e fica fora do catálogo de recursos. O [guia de estilo de publicação](../implementations/latex/README.pt-br.md#publication-style) explica temas, arte local opcional e a distinção entre aparência e conteúdo preservado.

## Regenerar e verificar

O JSON de cada diretório de exemplo é sua fonte autoral canônica. No diretório da edição:

```bash
python examples/build.py
python examples/build.py --check
python examples/build.py --pdf
```

O primeiro comando regenera Markdown, LaTeX e a matriz de rastreabilidade do quadro. Também produz os starters Markdown e LaTeX a partir de `implementations/json/starter.atlas.json`. `--check` compara, sem alterar os arquivos distribuídos, suas representações e executa as seis direções de conversão para cada exemplo e para o starter. `--pdf` regenera as fontes e compila os três PDFs com pdfLaTeX e `implementations/latex/atlas.sty`.

Instale as dependências Python a partir do `pyproject.toml` desta edição. Uma distribuição TeX só é necessária para compilar PDF. Use `--pdflatex CAMINHO` ou `ATLAS_PDFLATEX` quando o executável não estiver no PATH. A compilação usa um diretório temporário e substitui o PDF existente somente após sucesso. `--keep-intermediates`, combinado com `--pdf`, preserva os diagnósticos do TeX.

## Escopo e proveniência

- `task-board/needs.md`, revisão 1, é uma base didática sintética. Não comprova aprovação de partes interessadas nem afirma uma derivação real Needs→L1.
- As fontes `SRC-REQUEST-BRIEF` e `SRC-BOOKING-BRIEF` são bases sintéticas versionadas dentro das instâncias. Seus números de tempo permanecem hipóteses didáticas, não SLAs de produção.
- A `traceability` de cada caso liga origem → RF/RNF e aceite → obrigação. RFs e elementos dos grafos mantêm referências correspondentes nos dois sentidos.
- O formulário web e a linha de comando são propostas ilustrativas de canal. Tela e sintaxe de comandos não se tornam requisitos obrigatórios de L1. O quadro de tarefas não escolhe um canal.
- Uma aplicação futura deverá implementar e verificar persistência, autorização e qualidade. Este repositório entrega a especificação, suas representações, o tradutor e as verificações desses artefatos.

A [matriz do quadro de tarefas](task-board/traceability.md) permite inspecionar a referência principal. Os exemplos pertencem à primeira edição publicável, `Alpha-v0.1.0`.

## Autoria

Douglas de Oliveira Alkimim.
