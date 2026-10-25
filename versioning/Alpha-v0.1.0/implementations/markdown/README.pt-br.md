# Atlas Markdown · Alpha-v0.1.0

[English](README.md) · Português brasileiro · [Manual da edição](../../README.pt-br.md#implementations)

**Comece por:** [starter.atlas.md](starter.atlas.md). Ele contém o mesmo rascunho dos outros dois modelos iniciais. Coleções de domínio vazias e perguntas de escopo/fontes são intencionais; validação estrutural não estabelece especificação L1 completa. Siga o [fluxo de autoria](../../README.pt-br.md#quick-start) e consulte os [exemplos completos](../../examples/README.pt-br.md).

Tradução da definição normativa em inglês desta versão. Identificador: `atlas-markdown/Alpha-v0.1.0`.

Atlas Markdown é a implementação textual para leitura direta, revisão e consumo por agentes. É um perfil controlado de Markdown.

## 1. Autoridade da fonte

- Os **registros visíveis de texto** são autoritativos para a prosa.
- O **apêndice estrutural** é autoritativo para dados não textuais.
- Rótulos, títulos gerados ao redor de registros, resumos, topologia e diagramas são apresentação derivada, verificada ou ignorada conforme as regras abaixo.
- A prosa não é recuperada do apêndice, e a estrutura não é adivinhada a partir da prosa.

Uma edição visível em registro textual é importada. Uma edição fora dos registros não cria conteúdo; edição de região derivada recebe diagnóstico.

## 2. Cabeçalho

O primeiro marcador Atlas deve ser:

`````text
<!-- atlas:markdown profile=atlas-markdown representation=Alpha-v0.1.0 translator=0.1.0 -->
`````

A versão de representação deve coincidir com o adaptador. Divergência é recusada. A versão do tradutor no cabeçalho é informativa.

## 3. Registros de texto

Um registro possui marcador inicial, conteúdo exato e marcador final:

`````text
<!-- atlas:text id=T000001 role=paragraph -->
Texto exato
<!-- /atlas:text id=T000001 -->
`````

| Atributo | Obrigatório | Valores |
| --- | --- | --- |
| `id` | Sim | `T` seguido de seis dígitos; único no documento. |
| `role` | Sim | `heading`, `paragraph`, `note`, `quote`, `list-item`, `code`, `formula`, `table-cell`. |
| `level` | Para título | 1–6. |
| `ordered` | Para item de lista | `yes` ou `no`; indicação de apresentação. |

### Limites do conteúdo

O conteúdo começa imediatamente após a quebra que termina o marcador inicial e termina no início da linha do marcador final. A única quebra imediatamente anterior ao marcador final é estrutural e removida. Assim:

- `abc` é escrito como `abc` seguido da quebra estrutural;
- `abc\n` acrescenta uma linha vazia antes do marcador final;
- `""` não tem linha de conteúdo antes do marcador final.

CRLF/LF/CR autorais dentro do conteúdo são preservados exatamente. O codec não normaliza quebras.

### Prefixos

- Conteúdo de título começa com `#` repetido `level` vezes e um espaço. O decodificador remove exatamente esse prefixo.
- Conteúdo de item começa com `- ` ou `1. `. O decodificador remove exatamente esse prefixo.
- Os demais papéis não têm prefixo.

A falta do prefixo exigido causa erro. O prefixo pertence à sintaxe da representação, não ao texto autoral.

### Conteúdo semelhante a marcadores

Se uma linha de conteúdo começa com barras invertidas opcionais seguidas de `<!-- atlas:` ou `<!-- /atlas:`, o codificador acrescenta uma barra invertida. O decodificador remove exatamente uma. Isso preserva comentários e delimitadores literais no conteúdo. Por exemplo:

`````text
\<!-- atlas:text id=T999999 role=paragraph -->
`````

é decodificado como:

`````text
<!-- atlas:text id=T999999 role=paragraph -->
`````

Não há outro escape do texto Markdown. Barras, cercas de código, pipes, HTML e Unicode permanecem como autorados.

## 4. Apresentação dos blocos

Cada registro humano declarado é externalizado uma vez. O apêndice guarda a estrutura dos blocos e o corpo oferece um registro para cada valor textual. Strings estruturais, como IDs, enums, caminhos e dados brutos de exemplo, continuam estruturais. `meta`, `data` de exemplos de entidade e `extensions` são opacos e permanecem no apêndice, mesmo contendo chaves `text`, `@text` ou `id`; valores e tipos são preservados.

| Bloco | Apresentação Markdown |
| --- | --- |
| `paragraph`, `note`, `quote` | Um registro com o papel correspondente. |
| `heading` | Um registro com prefixo de título. |
| `list` | Um registro por item (`- ` ou `1. `), seguido dos filhos; estrutura no apêndice. |
| `code` | Registro com papel `code`; conteúdo bruto, sem cerca automática. |
| `formula` | Registro com papel `formula`; fonte bruta, sem execução. |
| `figure` | Referência visível ao recurso e registros de legenda/texto alternativo; sem binário embutido. |
| `table` | Registros de colunas/células com rótulos; tabela com pipes não é a fonte autoritativa. LaTeX renderiza a tabela. |

Títulos/rótulos como `## Document metadata` ou `**Name**` podem aparecer como apresentação derivada. Somente registros marcados são importados.

## 5. Apêndice estrutural

A última parte estrutural usa os delimitadores abaixo. O conteúdo abreviado ilustra a gramática; use o modelo inicial para um arquivo completo válido.

`````text
<!-- atlas:structure:begin -->
````atlas-structure
{ ... estrutura JSON ... }
````
<!-- atlas:structure:end -->
`````

O bloco contém o payload Atlas com cada valor textual do perfil substituído por `{"@text": "T…"}`. Mantém dados não textuais: IDs, referências, enums, booleanos, números, grafos, recursos, extensões e ordens. A cerca usa quatro crases; JSON serializado não contém uma quebra literal dentro de string, portanto o conteúdo de uma string não gera uma linha de fechamento da cerca.

A decodificação:

1. Reúne os registros de texto.
2. Analisa o JSON estrutural estritamente, recusando chaves duplicadas.
3. Restaura os textos nos slots.
4. Recusa slots ausentes, duplicados, órfãos ou desconhecidos.
5. Valida o documento Atlas completo.
6. Verifica as regiões derivadas.

O apêndice não contém uma segunda cópia dos textos do perfil e não sobrepõe o corpo. Strings estruturais e dados opacos de metadados/exemplos/extensões não são slots de prosa.

## 6. Regiões derivadas

### Resumo e topologia

`````text
<!-- atlas:derived id=DERIVED-SUMMARY -->
Derived summary: ...
<!-- /atlas:derived id=DERIVED-SUMMARY -->
`````

A topologia usa `DERIVED-GRAPH-<graph-id>`. Essas regiões não contêm registros autorais. O decodificador regenera o texto esperado da estrutura atual e compara exatamente. Editá-lo produz `ATL-E-DERIVED-STALE`, com orientação para regenerar.

TikZ é uma região derivada exclusiva do [perfil LaTeX](../latex/README.pt-br.md).

## 7. Metadados

- Identidade/versão aparecem em pequenas linhas geradas próximas ao início.
- Metadados textuais (`id`, `nature`, `review_status`, `meta`) ficam no apêndice como parte do placeholder `@text`; o corpo carrega o texto.
- IDs e valores estruturais podem aparecer junto dos elementos como apresentação derivada; o apêndice é autoritativo.
- O texto legível não é precedido por um grande cabeçalho de JSON opaco.

## 8. Aninhamento e referências

Registros textuais não se aninham. Marcador inicial sem final correspondente, marcador inicial dentro de outro registro ou registro dentro de região derivada são erros. Referências usam IDs; posição visual/aninhamento não define identidade. O apêndice conserva a ordem de todos os arrays.

## 9. Dados estruturados

Tabelas, grafos, mapeamentos, catálogos e listas de IDs usam o apêndice. Cada texto autoral correspondente ainda deve aparecer no corpo. Não codifique prosa somente no JSON do apêndice.

## 10. Colisões e marcadores malformados

- Linhas semelhantes a marcadores dentro do conteúdo recebem o escape definido acima.
- Marcador desconhecido `<!-- atlas:` ou `<!-- /atlas:` fora de região textual/derivada/estrutural é recusado.
- IDs de texto duplicados, marcadores iniciais/finais divergentes e apêndices ausentes/duplicados são recusados.
- Uma linha de conteúdo semelhante ao marcador final do próprio registro recebe escape na codificação. Se escrita manualmente sem escape, encerra o registro e a divergência posterior é diagnosticada.

## 11. Limites e exemplos

O perfil importa somente registros marcados e apêndice; não infere conteúdo de Markdown genérico. Não acrescenta cercas automaticamente ao código. Tabelas são registros de células, sem tabela com pipes autoritativa. Edição de região derivada exige regeneração e não é mesclada automaticamente. Prefixos de registros fazem parte da gramática.

Arquivos completos: [modelo inicial](starter.atlas.md), [solicitação mínima](../../examples/minimal/example.atlas.md) e [composição](../../examples/composition/example.atlas.md). Eles substituem a necessidade de copiar trechos abreviados da gramática.
