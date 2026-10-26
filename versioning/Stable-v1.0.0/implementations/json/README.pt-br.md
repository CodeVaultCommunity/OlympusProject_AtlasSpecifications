# Atlas JSON · Stable-v1.0.0

[English](README.md) · Português brasileiro · [Manual da edição](../../README.pt-br.md#implementations)

**Comece por:** [starter.atlas.json](starter.atlas.json). Ele contém o mesmo rascunho dos outros dois modelos iniciais. Coleções de domínio vazias e perguntas de escopo/fontes são intencionais; validação estrutural não estabelece especificação L1 completa. Siga o [fluxo de autoria](../../README.pt-br.md#quick-start) e consulte os [exemplos completos](../../examples/README.pt-br.md).

Tradução da definição normativa em inglês desta versão. Schema: [atlas.schema.json](atlas.schema.json). Identificador do perfil: `atlas-json/Stable-v1.0.0`.

Atlas JSON é a implementação estruturada para manipulação, validação, integração e transformação. Também é o intermediário do tradutor. O modelo abstrato é definido separadamente.

## 1. Envelope do documento

O envelope contém `$schema` opcional, `format` e `atlas`. A forma abreviada abaixo ilustra os membros; o modelo inicial é o arquivo completo válido:

```json
{
  "$schema": "atlas.schema.json",
  "format": "atlas-json/Stable-v1.0.0",
  "atlas": { "...": "..." }
}
```

| Membro | Obrigatório | Significado |
| --- | --- | --- |
| `$schema` | Não | Indicação de schema para ferramentas; metadado de transporte. |
| `format` | Sim | Exatamente `atlas-json/Stable-v1.0.0`; metadado de transporte. |
| `atlas` | Sim | Conteúdo Atlas completo. |

Membros desconhecidos no envelope ou em objetos definidos pelo schema são recusados. Contêineres abertos declarados, como `meta` textual, `data` de exemplos de entidade e `extensions`, conservam o comportamento definido pelo schema. Seus dados permanecem opacos para interpretação de slots/IDs e são preservados com valores e tipos.

## 2. Payload Atlas

Membros e grupos, sujeitos às restrições completas do schema:

- Identidade/metadados: `document_id`, `title`, `revision`, `spec_version`, `profile_version`, `translator_version`, `language`, `status`, `authors`, `created`, `updated`.
- Opcionais: `subtitle` (texto ou `null`), `keywords`, `notes`.
- Estrutura editorial: `structure`.
- Conceitos: `actors`, `vocabulary`, `types`, `entities`, `tools`, `use_cases`, `boundaries`.
- Material estruturado: `graphs`, `resources`.
- Registros: `assumptions`, `decisions`, `open_issues`, `sources`, `history`.
- Configuração/extensão: `presentation`, `extensions`.

As coleções principais são obrigatórias. Uma lista vazia significa “declarada e vazia”; sua ausência é inválida. `subtitle` é opcional e pode ser `null` ou registro textual; esses estados são distintos. Consulte o schema para a obrigatoriedade exata de cada membro.

Os membros internos de entidade `assumptions` e `open_issues` são opcionais. Um membro ausente não fornece referências para validar, sem inserir uma lista vazia. Ausência e `[]` são preservados distintamente; `null` é inválido nesses membros.

## 3. Registros de texto

```json
{"text": "Caracteres exatos, incluindo  espaços e\nquebras autorais."}
```

Metadados opcionais: `id`, `nature`, `review_status`, `meta`, `extensions`.

- `text` deve ser string e pode ser vazia.
- O modelo não apara nem normaliza seu conteúdo.
- `nature` e `review_status` são independentes.
- Um membro de texto ausente não equivale a string vazia.

Blocos ricos são listas de objetos. Os tipos estão no [modelo abstrato, seção 5](../../README.pt-br.md#model-5) e no schema. Referências de figura, estrutura de tabela/lista e demais membros estruturais permanecem nos campos declarados; legendas e células autorais continuam registros textuais.

## 4. Identidade

```text
[A-Z][A-Z0-9]*(-[A-Z0-9]+)+
```

IDs são únicos em todo o documento, incluindo campos, condições, operações, nós e arestas. `document_id` usa o mesmo namespace. IDs não são derivados da posição de arrays. Referências são strings de ID, sem índices posicionais.

Referências resolvem para sua categoria declarada, independentemente do prefixo do ID. Figuras em toda profundidade permitida apontam para `resources`; `sources`, `assumptions`, `open_issues` de casos/fronteiras e `assumptions`, `open_issues` de entidades apontam para os catálogos correspondentes. `meta`, `data` e `extensions` opacos não são interpretados como referências. Consulte o [inventário completo de referências](../../verification/reference-inventory.md).

## 5. Ordenação

A ordem de membros de objetos JSON não tem significado. A ordem dos arrays é conteúdo:

| Array | Significado da ordem |
| --- | --- |
| `structure` | Apresentação autoritativa das seções. |
| `section.items` | Apresentação dos conceitos na seção. |
| `blocks`, `list.items`, `children` | Ordem textual autoral. |
| Coleções de conceitos | Ordem de autoria; não substitui `structure.items`. |
| `graphs[].nodes`, `graphs[].edges` | Ordem de autoria/renderização do grafo. |
| `columns`, `rows` | Ordem da tabela. |
| `resources` | Ordem do catálogo. |
| `history` | Ordem declarada do histórico. |

O validador exige que cada ator/termo/tipo/entidade/ferramenta/caso/fronteira apareça exatamente uma vez em `structure`.

## 6. Validação

A validação possui etapas:

1. **Carregamento JSON:** UTF-8 sem BOM, recusa de chaves duplicadas, ponto flutuante e constantes não finitas.
2. **JSON Schema 2020-12:** tipos, membros obrigatórios/desconhecidos, enums e padrões.
3. **Invariantes referenciais:** IDs únicos, referências, posição editorial, proprietários/chamadas/arestas, consistência RF/grafo, RNFs compartilhados, RFs de fronteiras, caminhos/hashes/atualidade de recursos e texto em imagens.

```bash
atlas-spec validate file.atlas.json
atlas-spec validate file.atlas.json --resources path/to/package
```

`--no-check-resources` dispensa existência/tamanho/hash dos arquivos; as verificações estruturais e referenciais continuam. Elas não provam a suficiência semântica de contexto do ator, origem de requisitos, aceite ou contratos de negócio. Revise esses conteúdos pelo modelo abstrato.

## 7. Dados desconhecidos e extensões

Membros desconhecidos de objetos conhecidos são recusados. Dados de extensão declarados ficam em `extensions`:

```json
"extensions": {
  "example.org/custom": {
    "text": "opaco para o tradutor",
    "values": [1, 2, 3]
  }
}
```

O trecho ilustra um membro de objeto. Extensões são preservadas como dados JSON entre Markdown/LaTeX, sem interpretação pelo tradutor. Não substituem conteúdo obrigatório nem mudam a versão declarada. Incapacidade de preservar uma extensão exige recusar a conversão.

## 8. Casos inválidos ou não suportados

| Caso | Resultado |
| --- | --- |
| Chave JSON duplicada | `ATL-E-DUPLICATE-KEY` |
| Ponto flutuante | `ATL-E-FLOAT` |
| ID duplicado | `ATL-E-DUPLICATE-ID` |
| Referência ausente/desconhecida | `ATL-E-REF` |
| Elemento sem posição editorial | `ATL-E-STRUCTURE-MISSING` |
| Posição editorial duplicada | `ATL-E-STRUCTURE-DUPLICATE` |
| Bloco/construção desconhecidos | `ATL-E-SCHEMA` |
| Texto obrigatório ausente | `ATL-E-SCHEMA` |
| Extremo de aresta ausente | `ATL-E-GRAPH-EDGE` |
| Alvo de chamada de grafo ausente | `ATL-E-GRAPH-CALL` |
| Divergência RF/grafo | `ATL-E-RF-FLOW` / `ATL-E-RF-GRAPH` |
| Versão não suportada | `ATL-E-VERSION` / `ATL-E-PROFILE-VERSION` |
| Recurso ausente/tamanho/hash | `ATL-E-RESOURCE-*` |
| Figura derivada desatualizada | `ATL-E-FIGURE-STALE` |

## 9. Conversão

JSON é o intermediário do tradutor fornecido. JSON → Markdown/LaTeX externaliza registros de texto e estrutura; a decodificação restaura e valida o mesmo conteúdo. JSON → JSON é decode/encode normal e mantém conteúdo idêntico, embora a formatação de transporte possa mudar.

Conversão não migra versões, normaliza texto, atualiza recursos, busca URLs, compila PDFs ou descarta campos silenciosamente.

## 10. Valores numéricos

Números de conteúdo são inteiros. Metas decimais usam strings, como `"2"` ou `"0.5"`, para conservar sua escrita exata. `data` de exemplos de entidade pode conter inteiros JSON, booleanos, strings, nulos, arrays e objetos; o carregador estrito recusa números de ponto flutuante.

## 11. Exemplos

Consulte [solicitação mínima](../../examples/minimal/example.atlas.json), [composição](../../examples/composition/example.atlas.json) e [quadro de tarefas](../../examples/task-board/example.atlas.json).

## 12. Obrigações semânticas da autoria

O schema não esgota o modelo abstrato. Siga o [manual](../../README.pt-br.md#abstract-model) para ator iniciador/contexto/autorização, origem individual das obrigações, classificação L1/L4 de fronteiras e declarações responsáveis de Needs-to-L1. Esses assuntos usam campos existentes de texto, fontes e rastreabilidade; não exigem inventar uma extensão.
