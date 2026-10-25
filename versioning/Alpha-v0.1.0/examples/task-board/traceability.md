# Task-board traceability / Rastreabilidade do quadro

[English guide](README.md) · [Guia em português](README.pt-br.md) · [JSON](example.atlas.json)

Generated from the JSON instance by `examples/build.py`. IDs are exact; this matrix records specification links and does not claim execution of a business application.

Gerada a partir da instância JSON por `examples/build.py`. Os IDs são exatos; a matriz registra vínculos da especificação e não afirma execução de uma aplicação de negócio.

**Origin / Origem:** `SRC-TASK-BRIEF`, revision / revisão 1 (synthetic / sintética).

## UC-TASK-CREATE

**Create task**

| Obligation / Obrigação | Graph elements / Elementos do grafo | Acceptance / Aceite | Canonical rules or operations / Regras ou operações |
| --- | --- | --- | --- |
| `RF-TASK-CREATE-AUTH` | `N-TASK-CREATE-AUTH`<br>`N-TASK-CREATE-DENIED`<br>`E-TASK-CREATE-DENIED`<br>`E-TASK-CREATE-ALLOWED` | `AC-TASK-CREATE-AUTH` | — |
| `RF-TASK-CREATE-DATA` | `N-TASK-CREATE-VALIDATE`<br>`N-TASK-CREATE-VALID`<br>`N-TASK-CREATE-INVALID`<br>`E-TASK-CREATE-2` | `AC-TASK-CREATE-SUCCESS`<br>`AC-TASK-CREATE-INVALID` | `VLD-TASK-NEW` |
| `RF-TASK-CREATE-RETAIN` | `N-TASK-CREATE-STORE`<br>`N-TASK-CREATE-CREATED`<br>`E-TASK-CREATE-3`<br>`E-TASK-CREATE-6` | `AC-TASK-CREATE-SUCCESS` | `OP-TASK-CREATE` |
| `RF-TASK-CREATE-DUPLICATE` | `N-TASK-CREATE-DUPLICATE`<br>`E-TASK-CREATE-4` | `AC-TASK-CREATE-DUPLICATE` | — |
| `RF-TASK-CREATE-FAILURE` | `N-TASK-CREATE-UNAVAILABLE`<br>`E-TASK-CREATE-5` | `AC-TASK-CREATE-UNKNOWN` | — |

| Quality obligation / Obrigação de qualidade | Scope and targets / Escopo e alvos | Canonical definition / Definição canônica | Acceptance / Aceite |
| --- | --- | --- | --- |
| `RNF-TASK-CREATE-RETENTION` | system: `UC-TASK-CREATE`<br>`OP-TASK-CREATE`<br>`UC-TASK-LIST` | `RNF-TASK-CREATE-RETENTION` | `AC-TASK-CREATE-SUCCESS` |

## UC-TASK-COMPLETE

**Complete task**

| Obligation / Obrigação | Graph elements / Elementos do grafo | Acceptance / Aceite | Canonical rules or operations / Regras ou operações |
| --- | --- | --- | --- |
| `RF-TASK-COMPLETE-AUTH` | `N-TASK-COMPLETE-AUTH`<br>`N-TASK-COMPLETE-DENIED`<br>`E-TASK-COMPLETE-DENIED`<br>`E-TASK-COMPLETE-ALLOWED` | `AC-TASK-COMPLETE-AUTH` | — |
| `RF-TASK-COMPLETE-ID` | `N-TASK-COMPLETE-ID`<br>`N-TASK-COMPLETE-VALID`<br>`N-TASK-COMPLETE-INVALID`<br>`E-TASK-COMPLETE-2` | `AC-TASK-COMPLETE-INVALID` | `VLD-TASK-ID` |
| `RF-TASK-COMPLETE-LOAD` | `N-TASK-COMPLETE-LOAD`<br>`N-TASK-COMPLETE-MISSING`<br>`E-TASK-COMPLETE-3`<br>`E-TASK-COMPLETE-4` | `AC-TASK-COMPLETE-MISSING` | `OP-TASK-LOAD` |
| `RF-TASK-COMPLETE-TRANSITION` | `N-TASK-COMPLETE-TRANSITION`<br>`N-TASK-COMPLETE-ALLOWED`<br>`N-TASK-COMPLETE-ALREADY`<br>`E-TASK-COMPLETE-6`<br>`E-TASK-COMPLETE-8` | `AC-TASK-COMPLETE-SUCCESS`<br>`AC-TASK-COMPLETE-ALREADY` | `VLD-TASK-COMPLETE` |
| `RF-TASK-COMPLETE-WRITE` | `N-TASK-COMPLETE-MISSING`<br>`N-TASK-COMPLETE-STORE`<br>`N-TASK-COMPLETE-CONFLICT`<br>`N-TASK-COMPLETE-DONE`<br>`E-TASK-COMPLETE-9`<br>`E-TASK-COMPLETE-10`<br>`E-TASK-COMPLETE-11`<br>`E-TASK-COMPLETE-13` | `AC-TASK-COMPLETE-SUCCESS`<br>`AC-TASK-COMPLETE-CONFLICT` | `OP-TASK-COMPLETE` |
| `RF-TASK-COMPLETE-FAILURE` | `N-TASK-COMPLETE-ERROR`<br>`E-TASK-COMPLETE-5`<br>`E-TASK-COMPLETE-12` | `AC-TASK-COMPLETE-UNKNOWN` | — |

| Quality obligation / Obrigação de qualidade | Scope and targets / Escopo e alvos | Canonical definition / Definição canônica | Acceptance / Aceite |
| --- | --- | --- | --- |
| `RNF-TASK-COMPLETE-ATOMICITY` | operation: `UC-TASK-COMPLETE`<br>`OP-TASK-COMPLETE` | `RNF-TASK-COMPLETE-ATOMICITY` | `AC-TASK-COMPLETE-CONFLICT` |

## UC-TASK-LIST

**List tasks**

| Obligation / Obrigação | Graph elements / Elementos do grafo | Acceptance / Aceite | Canonical rules or operations / Regras ou operações |
| --- | --- | --- | --- |
| `RF-TASK-LIST-AUTH` | `N-TASK-LIST-AUTH`<br>`N-TASK-LIST-DENIED`<br>`E-TASK-LIST-DENIED`<br>`E-TASK-LIST-ALLOWED` | `AC-TASK-LIST-AUTH` | — |
| `RF-TASK-LIST-SNAPSHOT` | `N-TASK-LIST-READ`<br>`N-TASK-LIST-RETURN`<br>`E-TASK-LIST-2` | `AC-TASK-LIST-CONTENT`<br>`AC-TASK-LIST-EMPTY` | `OP-TASK-LIST` |
| `RF-TASK-LIST-FAILURE` | `N-TASK-LIST-FAIL`<br>`E-TASK-LIST-1` | `AC-TASK-LIST-EMPTY`<br>`AC-TASK-LIST-INTEGRITY` | — |

| Quality obligation / Obrigação de qualidade | Scope and targets / Escopo e alvos | Canonical definition / Definição canônica | Acceptance / Aceite |
| --- | --- | --- | --- |
| `RNF-TASK-LIST-CONSISTENCY` | operation: `UC-TASK-LIST`<br>`OP-TASK-LIST` | `RNF-TASK-LIST-CONSISTENCY` | `AC-TASK-LIST-CONTENT` |
| `RNF-TASK-LIST-RETENTION` | system: `UC-TASK-LIST`<br>`OP-TASK-LIST` | `RNF-TASK-CREATE-RETENTION` | `AC-TASK-CREATE-SUCCESS` |

## Interpretation / Interpretação

- RF links are reciprocal: each referenced node or edge names the RF, and the RF lists those elements.
- Os vínculos de RF são recíprocos: cada nó ou aresta referencia o RF, e o RF lista esses elementos.
- RNFs retain their scope and origin; references point to a canonical definition.
- RNFs preservam escopo e origem; referências apontam para uma definição canônica.
- Acceptance descriptions are future implementation obligations. Translator tests check document consistency and preservation.
- Critérios de aceite são obrigações da implementação futura. Testes do tradutor conferem consistência e preservação documental.
