# Atlas LaTeX · Alpha-v0.1.0

[English](README.md) · Português brasileiro · [Manual da edição](../../README.pt-br.md#implementations)

**Comece por:** [starter.atlas.tex](starter.atlas.tex). Ele contém o mesmo rascunho dos outros dois documentos iniciais. Coleções de domínio vazias e perguntas de escopo/fontes são intencionais; validação estrutural não estabelece especificação L1 completa. Siga o [fluxo de autoria](../../README.pt-br.md#quick-start) e consulte os [exemplos completos](../../examples/README.pt-br.md).

Tradução da definição normativa em inglês desta versão. Identificador: `atlas-latex/Alpha-v0.1.0`. Estilo: [atlas.sty](atlas.sty).

Atlas LaTeX é a implementação estruturada para autoria e publicação visual por compilação. Usa um conjunto controlado de comentários, ambientes e comandos.

## 1. Cabeçalho e documento

A primeira linha é:

```text
% atlas:latex profile=atlas-latex representation=Alpha-v0.1.0 translator=0.1.0
```

O documento usa `\documentclass{article}` ou classe compatível e carrega:

```text
\usepackage{atlas}
```

O preâmbulo dos exemplos usa:

- `iftex`; `inputenc`/`fontenc` com pdfTeX e `fontspec` nos outros caminhos.
- `geometry`, `graphicx`, `xcolor`, `booktabs`, `longtable`, `array`, `amsmath`, `tikz`, `hyperref`.
- `atlas.sty` fornece tipografia e diagramação com `lmodern` sob pdfTeX, `microtype`, `needspace`, `fancyhdr`, `colortbl` e `tcolorbox` com suas bibliotecas `breakable` e `skins`. Também usa `iftex`, `xcolor`, `graphicx`, `tikz`, `booktabs` e `array`.
- Bibliotecas TikZ `shapes.geometric`, `arrows.meta` e `positioning`, carregadas por `atlas.sty`.

Imediatamente depois de carregar `atlas`, o preâmbulo gerado inclui configurações locais opcionais de publicação:

```text
\InputIfFileExists{atlas-presentation.tex}{}{}
```

Esse arquivo é consumido pelo TeX durante a compilação. O decodificador Atlas não o abre. O estilo padrão funciona sem esse arquivo e sem arquivos de imagens decorativas. Consulte [estilo de publicação](#publication-style) para o exemplo de configuração e seu escopo de preservação.

O preâmbulo condicional oferece caminho pdfLaTeX e alternativa XeLaTeX/LuaLaTeX para outros sistemas de escrita. Isso não prova que toda combinação de fontes/mecanismos foi testada. Consulte [verificação e publicação](../../README.pt-br.md#verification).

## 2. Autoridade da fonte

- Ambientes de texto visíveis são autoritativos para a prosa.
- O apêndice estrutural comentado é autoritativo para dados não textuais.
- `atlasderived` e regiões `% atlas:tikz` são apresentação derivada, verificada na importação.
- A importação lê o arquivo-fonte; não extrai texto do PDF nem executa macros para descobrir significado.
- Temas, arte ornamental de capa e outros recursos puramente decorativos de publicação ficam fora do payload `atlas`. Não são recursos semânticos nem novos campos JSON. Uma imagem que comunique requisito, grafo, entidade, regra ou evidência continua sendo recurso catalogado; aplicar um estilo não reclassifica conteúdo semântico como decoração.

## 3. Ambientes textuais

| Ambiente | Argumentos | Significado |
| --- | --- | --- |
| `atlastitle` | ID textual | Título do documento. |
| `atlasheading` | ID textual, nível | Título de nível 1–6. |
| `atlastext` | ID textual | Parágrafo/prosa. |
| `atlasparagraph` | ID textual | Bloco de parágrafo. |
| `atlasitem` | ID textual | Item de lista. |
| `atlasquote` | ID textual | Citação. |
| `atlasnote` | ID textual | Nota. |
| `atlascode` | ID textual | Código literal; `\obeylines\obeyspaces`. |
| `atlasformula` | ID textual | Fonte literal de fórmula. |
| `atlasderived` | ID derivado | Resumo/topologia gerados. |

Forma abreviada:

```text
\begin{atlastext}{T000001}
...conteúdo codificado...
\end{atlastext}
```

Nome, ID e marcador final são estrutura. O conteúdo começa após a quebra que termina a linha inicial e termina antes da quebra imediatamente anterior a `\end{...}`; essa última quebra estrutural é removida. Quebras autorais dentro do conteúdo são preservadas pelo decodificador.

Um CR autoral final é seguido de separador estrutural CRLF, produzindo CR + CRLF em vez de fundir aquele CR com um LF. Os demais separadores gerados são LF.

## 4. Codificação de caracteres

O conteúdo é UTF-8. Caracteres especiais usam macros únicas:

| Caractere | Forma na fonte |
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

Células em linha codificam LF como `\AtlasCharNewline{}`, CRLF como `\AtlasCharCRLF{}`, CR como `\AtlasCharCR{}` e tabulação como `\AtlasCharTab{}`. CRLF é codificado antes dos caracteres individuais. As formas distintas preservam sequências mistas e a quebra autoral final, embora o estilo renderize as três formas de quebra como espaço. Demais caracteres, incluindo Unicode e espaços comuns, permanecem literais. A decodificação reverte exatamente as macros em uma única passagem. Como barras invertidas e chaves autorais são codificadas, nomes literais de macros permanecem texto; `\end{atlastext}` literal não encerra um ambiente e `% atlas:...` literal não é confundido com marcador.

O estilo renderiza o caractere pretendido, mantendo a fonte recuperável e o PDF legível.

## 5. Tabelas e células

Tabelas ricas são renderizadas a partir da estrutura. Células usam:

```text
\AtlasCell{T000042}{...célula codificada...}
```

O decodificador extrai a macro com balanceamento de chaves e restaura seu texto. O layout é apresentação derivada; o texto da célula é autoritativo. As células usam os escapes distintos de LF/CRLF/CR descritos acima.

O renderizador fornecido usa colunas `longtable` com quebra de linha e traços `booktabs`. O cabeçalho de uma tabela pode se repetir nas páginas seguintes do PDF; cada registro autoritativo de célula continua aparecendo uma única vez na fonte. Larguras, estilo das linhas, quebras de página e repetição visual de cabeçalhos não criam conteúdo Atlas adicional.

## 6. Apêndice estrutural

No final do arquivo, a estrutura é JSON comentado. Este é um trecho ilustrativo, não um documento completo:

```text
% atlas:structure:begin
% {
%   "document_id": "ATLAS-EX-MINIMAL",
%   "title": {"@text": "T000001"},
%   ...
% }
% atlas:structure:end
```

Cada linha é um comentário. O decodificador remove `% ` ou `%`, analisa o JSON estritamente e restaura slots como no Markdown. Slots ausentes/duplicados/órfãos e membros desconhecidos são erros. `meta`, `data` de exemplos de entidade e `extensions` permanecem dados estruturais opacos; chaves `text`, `@text` e `id` nesses contêineres não são slots ou declarações Atlas.

Somente CR, LF e CRLF delimitam linhas físicas do perfil. O codificador comenta as linhas de layout LF emitidas pela serialização JSON. U+0085, U+2028 e U+2029 dentro de strings estruturais permanecem conteúdo literal; nem escritor nem leitor os tratam como limites de comentários ou os normalizam.

## 7. Regiões derivadas e TikZ

### Texto derivado

```text
\begin{atlasderived}{DERIVED-SUMMARY}
Derived summary: ...
\end{atlasderived}
```

O conteúdo usa as mesmas macros de caracteres. O decodificador regenera e compara o texto esperado; edição isolada gera `ATL-E-DERIVED-STALE`.

### Diagramas TikZ

Grafos de fluxo/estado/relação são renderizados entre delimitadores:

```text
% atlas:tikz:begin id=TIKZ-GRAPH-REQUEST-SUBMIT
\clearpage
... diagrama determinístico e legenda das chaves de arestas ...
\clearpage
% atlas:tikz:end id=TIKZ-GRAPH-REQUEST-SUBMIT
```

A fonte TikZ deriva deterministicamente do grafo e de seus rótulos. O decodificador a regenera e compara; edição isolada gera `ATL-E-TIKZ-STALE`. Cada grafo tem exatamente uma região `TIKZ-<graph-id>`. Os dados do grafo são autoritativos.

O layout fica limitado à largura/altura da página. Rótulos dos nós têm quebra de linha; arestas usam chaves `E1`, `E2`, … e legenda com IDs/rótulos exatos. A listagem estruturada completa continua autoritativa. Um grafo muito grande pode ficar pequeno ao ser escalado; subfluxos significativos podem melhorar a apresentação. Não há limite semântico fixo de nós/arestas. Toda publicação exige revisão visual; compilar com sucesso não prova legibilidade.

## 8. Recursos e figuras

### Figuras que carregam conteúdo da especificação

Um bloco de figura usa `\includegraphics` com recurso PDF/PNG/JPEG ou variante do catálogo. O SVG original permanece fonte editável preservada; a variante é explícita.

```text
\begin{figure}[htbp]
\centering
\includegraphics[width=0.62\linewidth]{assets/request-form.png}
\end{figure}
```

Sem variante compilável, a codificação relata `ATL-E-LATEX-RESOURCE`. Caminhos são relativos à raiz do pacote documental. A compilação não busca URLs nem reescreve recursos.

<a id="publication-style"></a>
### Estilo de publicação e imagens decorativas

O estilo **editorial**, padrão, acrescenta capa ilustrada, tipografia consistente, paleta sóbria em azul-marinho/ciano/verde-azulado, títulos e rótulos mais claros, cabeçalhos e rodapés de página, notas e tabelas estilizadas. A arte da capa é um ornamento vetorial autocontido, desenhado pelo estilo; não representa grafo Atlas nem comportamento do sistema. O tema **plain** usa capa branca e destaques discretos em tons de cinza, com o mesmo conteúdo documental. Ele altera a paleta do estilo; imagens semânticas e grafos gerados mantêm suas próprias cores.

Os documentos gerados colocam o título autoritativo e o subtítulo opcional dentro de uma capa iniciada por `\AtlasBeginCover{document-id}{revision}{status}` e encerrada por `\AtlasEndCover`. Os metadados completos, autores e a especificação aparecem em seguida. Esses comandos organizam a publicação; os ambientes do título/subtítulo e o apêndice estrutural continuam sendo fontes de autoridade. Cabeçalhos, rodapés e seleção de tema não alteram essas fontes.

Use o mesmo arquivo `atlas.sty` nos dois temas. Copie [atlas-presentation.example.tex](atlas-presentation.example.tex) para a pasta do documento gerado e renomeie a cópia para `atlas-presentation.tex`. Compile com a pasta do documento `.tex` como diretório de trabalho. O exemplo de configuração ativa o tema padrão e mantém comentados os caminhos opcionais de imagem.

| Comando | Local | Efeito |
| --- | --- | --- |
| `\AtlasTheme{editorial}` | `atlas-presentation.tex`, antes de `\begin{document}`. | Seleciona o estilo ilustrado padrão. |
| `\AtlasTheme{plain}` | Mesmo arquivo de configuração. | Seleciona o estilo sóbrio em tons de cinza. |
| `\AtlasCoverImage{presentation/cover.png}` | Mesmo arquivo de configuração. | Usa uma imagem decorativa local na capa. |
| `\AtlasDecorativeImage[width=0.55\linewidth]{presentation/ornament.png}` | Corpo do documento, entre ambientes autoritativos e antes do apêndice estrutural. | Insere imagem ornamental local com opções de `graphicx`. |

Por exemplo, o arquivo opcional de configuração completo pode ser:

```text
\AtlasTheme{editorial}
% Descomente somente depois de colocar o arquivo local nesta publicação:
% \AtlasCoverImage{presentation/cover.png}
```

Use esses comandos de imagem somente para decoração: textura de capa, emblema ou separador visual que não acrescente requisitos, entidades, condições de fluxo, explicações, critérios de aceite ou evidências. Mantenha títulos, legendas com significado semântico, declarações de autoria e texto da especificação nos registros autoritativos. Não coloque registros de texto, células, dados estruturais ou marcadores de grafo Atlas no arquivo de configuração; o importador nunca lê esse arquivo. Não insira decoração dentro de ambiente textual autoritativo, região verificada `atlasderived` ou região verificada `% atlas:tikz`. Essas regiões continuam sujeitas à validação normal.

Caminhos de imagens decorativas são caminhos locais de publicação, resolvidos quando o TeX compila a partir da pasta do documento. Não exigem ID de recurso, hash, bloco `figure` ou entrada JSON. A ausência de uma imagem de capa configurada gera aviso TeX e usa o ornamento vetorial embutido; uma decoração do corpo ausente gera aviso e é omitida. Esses avisos de apresentação são separados dos erros estritos por recursos semânticos ausentes. A conversão não abre nem busca arquivos decorativos e não executa o arquivo de configuração.

**A conversão preserva o conteúdo da especificação, não uma diagramação personalizada.** LaTeX → JSON ou Markdown omite configurações, comandos de imagens decorativas e seus arquivos. JSON ou Markdown → LaTeX regenera o layout padrão da fonte, incluindo a busca opcional pelo arquivo de configuração; não recupera um arquivo de tema apagado nem caminhos de imagem personalizados. Manter o mesmo arquivo de configuração local permite que um documento regenerado naquela pasta use a mesma capa/tema ao compilar. Uma decoração inserida manualmente no corpo precisa ser reaplicada após regeneração.

O comando `package` inclui recursos semânticos e o estilo fornecido; ele não copia `atlas-presentation.tex` nem arte decorativa não catalogada. Para reproduzir a publicação personalizada em outra pasta, copie explicitamente o arquivo de configuração e suas imagens locais e revise o resultado renderizado. A ausência deles não altera o payload `atlas` decodificado nem enfraquece as verificações de recursos semânticos.

## 9. Compilação

O [documento inicial](starter.atlas.tex) é um documento real. `atlas.sty` é o pacote de estilo auxiliar. A partir da pasta da edição, compile os exemplos completos com:

```bash
python examples/build.py --pdf
```

O construtor executa duas passagens pdfLaTeX com o estilo local disponível em `TEXINPUTS`. Uma falha conserva a publicação anterior. Instale os pacotes TeX listados no §1 pela distribuição TeX escolhida. Para um documento isolado, copie `atlas.sty` ao lado de seu `.tex` e execute o comando abaixo duas vezes naquela pasta, substituindo o nome pelo documento real:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape specification.atlas.tex
```

Alternativamente, adicione o caminho absoluto de `implementations/latex` a `TEXINPUTS`, seguido do separador de caminhos da plataforma (`:` em Unix; `;` em Windows), conservando a busca padrão do TeX. Copie as configurações opcionais de publicação e as imagens separadamente para conservar um design personalizado. Esses arquivos são entradas de publicação TeX, processadas somente pelo compilador.

O tradutor não compila PDFs. Compilar e revisar páginas renderizadas são etapas de publicação. Recursos referenciados devem continuar disponíveis em relação à raiz do pacote.

## 10. Limites e exemplos

- LaTeX arbitrário fora dos marcadores é apresentação ignorada na importação; não é inferido como conteúdo Atlas.
- Macros em texto autoral são codificadas, sem execução.
- O apêndice estrutural é obrigatório.
- Extração de texto de PDF, layout, substituição de fontes e paginação ficam fora da conversão reversível.
- Arte decorativa e configurações locais de publicação são intencionalmente excluídas da conversão. Figuras semânticas e regiões derivadas de grafos mantêm as obrigações existentes de preservação e validação.
- O perfil não suporta todo pacote/construção LaTeX. Construções desconhecidas no conteúdo Atlas são recusadas pelo schema; comandos externos de apresentação ficam fora do perfil.
- A fonte exige UTF-8 válido sem BOM.
- Os exemplos usam caracteres compatíveis com pdfLaTeX; XeLaTeX/LuaLaTeX podem ser necessários para outros sistemas de escrita.

Arquivos completos: [documento inicial](starter.atlas.tex), [solicitação mínima](../../examples/minimal/example.atlas.tex) e [composição](../../examples/composition/example.atlas.tex). Os PDFs compilados ficam junto dos exemplos.
