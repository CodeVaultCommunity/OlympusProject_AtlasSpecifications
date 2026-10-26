# Reference validation inventory / Inventário de validação de referências

This inventory reviews every ID-reference position in the JSON Schema. It distinguishes category constraints already present in the contract from generic links. Categories come from declarations, never conventional ID prefixes. Schema validation precedes these checks. This is an implementation audit, not an OAL Stable conformance assessment.

Este inventário revisa cada posição de referência por ID no JSON Schema. Distingue restrições de categoria já presentes no contrato de vínculos genéricos. Categorias vêm das declarações, nunca dos prefixos convencionais de IDs. O schema é verificado antes dessas regras. Esta é uma auditoria de implementação, não uma avaliação de conformidade com OAL Stable.

| Position / Posição | Allowed target / Alvo permitido | Check / Verificação |
| --- | --- | --- |
| `section.items` | Top-level actor, term, type, entity, tool, case, boundary / conceito principal | `ATL-E-REF`; exactly one placement / uma única posição |
| `entity.identity.fields` | Fields of this entity / campos desta entidade | `ATL-E-REF` |
| `relationship.target` | Entity / entidade | `ATL-E-REF` |
| `transition.from`, `transition.to` | States of this entity / estados desta entidade | `ATL-E-REF` |
| `validation.flow` | Graph owned by that validation / grafo da validação | `ATL-E-REF`, `ATL-E-GRAPH-OWNER` |
| `entity.assumptions`, `entity.open_issues` | Corresponding document catalogs / catálogos correspondentes | `ATL-E-REF`; absent lists stay absent / ausência preservada |
| `actorPermission.actor` | Actor / ator | `ATL-E-REF` |
| `entityUse.entity`, `entityUse.validations` | Entity and its own validations / entidade e suas validações | `ATL-E-REF` |
| `toolUse.tool`, `toolUse.operation` | Tool and its own operation / ferramenta e sua operação | `ATL-E-REF` |
| `caseCall.use_case` | Another case / outro caso | `ATL-E-REF`, `ATL-E-SELF-CALL` |
| `useCase.flows.main`, `.subflows` | Graphs owned by the case / grafos do caso | `ATL-E-REF`, `ATL-E-GRAPH-OWNER` |
| `functionalRequirement.applies_to` | This case, an operation or an interaction / este caso, operação ou interação | `ATL-E-REF` |
| `functionalRequirement.flow_refs` | Nodes/edges of this case's flows / nós e arestas dos fluxos do caso | `ATL-E-RF-FLOW`; reciprocal RF links / reciprocidade |
| `nonfunctionalRequirement.reference_to` | Canonical full RNF in another case / RNF canônico completo de outro caso | `ATL-E-REF`, `ATL-E-RNF-CHAIN`, `ATL-E-RNF-LOCAL` |
| `nonfunctionalRequirement.applies_to`, `.references` | Declared ID in global namespace / ID declarado no namespace global | `ATL-E-REF`; broad links retained / vínculos amplos mantidos |
| `acceptanceCriterion.verifies` | Declared ID / ID declarado | `ATL-E-REF` |
| `traceLink.source`, `.targets` | Declared ID / ID declarado | `ATL-E-REF`; a trace source is not restricted to bibliography / origem do vínculo não restrita à bibliografia |
| `useCase.sources`, `.assumptions`, `.open_issues` | Corresponding catalogs / catálogos correspondentes | `ATL-E-REF` |
| `interaction.use_case` | Use case / caso de uso | `ATL-E-REF` |
| `interaction.requirement_refs` | RFs owned by exposed case / RFs do caso exposto | `ATL-E-REF`, `ATL-E-BOUNDARY-RF` |
| `interaction.resources` | Resource catalog / catálogo de recursos | `ATL-E-REF` |
| `boundary.sources`, `.assumptions`, `.open_issues` | Corresponding catalogs / catálogos correspondentes | `ATL-E-REF` |
| `graph.owner.id` | Category selected by `owner.kind`; validation/case flow membership / categoria e vínculo ao fluxo | `ATL-E-GRAPH-OWNER` |
| `graphCall.id` | Category selected by `call.kind` / categoria indicada por `call.kind` | `ATL-E-GRAPH-CALL` |
| `graphEdge.from`, `.to` | Nodes in this graph / nós deste grafo | `ATL-E-GRAPH-EDGE` |
| `graphNode.requirement_refs`, `graphEdge.requirement_refs` | RF catalog; own case RFs and reciprocal links for case graphs / RFs e reciprocidade do caso | `ATL-E-RF-GRAPH`, `ATL-E-RF-FLOW` |
| `figure.resource` | Resource catalog at every schema-valid rich-block location / recursos em todo local válido de blocos ricos | `ATL-E-REF` |
| `resource.derived_from_graph` | Graph; current fingerprint / grafo e impressão digital atual | `ATL-E-REF`, `ATL-E-FIGURE-STALE` |
| `assumption.affected`, `decision.refs`, `openIssue.refs` | Declared ID / ID declarado | `ATL-E-REF` |

`id` and `document_id` declarations share a unique namespace. `owner.id` and `call.id` are references, not new declarations. Opaque `extensions`, text `meta`, and entity-example `data` are neither scanned for declarations nor references. Free prose, type names, paths, URIs, revision strings and boundary input/result mapping labels are not ID-reference fields. `resourceVariant.derived_from` is a package path matched to the original resource path, not an ID. A list item's recursive children hold text; the grammar does not allow arbitrary figure blocks there. Nested contracts that do permit rich blocks are traversed.

Declarações `id` e `document_id` compartilham um namespace único. `owner.id` e `call.id` são referências. `extensions`, `meta` textual e `data` de exemplos de entidade são opacos: não se interpretam declarações ou referências internas. Prosa livre, nomes de tipos, caminhos, URIs, revisões e rótulos de mapeamento das boundaries não são campos de referência por ID. `resourceVariant.derived_from` é um caminho comparado ao recurso original. Filhos recursivos de listas contêm texto, não figuras arbitrárias. Contratos aninhados que permitem blocos ricos são percorridos.
