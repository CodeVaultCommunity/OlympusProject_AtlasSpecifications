# Semantic review and material inventory / Revisão semântica e inventário

Document-level semantic assessment, separate from automated validation and human release approval. / Avaliação semântica documental, distinta da validação automatizada e da aprovação humana da release.

## Materials and acceptance / Materiais e aceite

| Material / Material | Origin/version and use / Origem, versão e uso | Limits and acceptance / Limites e aceite |
| --- | --- | --- |
| Atlas manual, profiles, schema, runtime, tests | Actual repository baseline `ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04`, Alpha-v0.1.0; deliberately reused in the new independent edition. / Baseline real, reaproveitada deliberadamente. | Alpha preserved; defects reproduced before identity changes; Stable tests and generated correspondence required. / Preservação, reprodução prévia e verificações exigidas. |
| OAL Stable manual EN/PT | Actual delivered bytes, commit/hash in [baseline](oal/baseline.json); [19-clause review](OAL-CORRESPONDENCE.md). / Bytes reais e revisão de 19 cláusulas. | Local provenance, no public commit URL claimed; L2–L4/engines excluded. / Proveniência local; exclusão de camadas posteriores e engines. |
| Starter | Draft, empty domain collections, unknown scope; editorial revision 2. / Rascunho sem requisitos de produto preenchidos. | Structurally valid, intentionally incomplete. / Válido estruturalmente e incompleto intencionalmente. |
| Minimal request | `SRC-REQUEST-BRIEF` revision 2; synthetic teaching example; migrated document revision 2. / Exemplo didático sintético. | Two local originals and PNG variants, exact resource hashes; 2-second target remains proposed with `OI-REQUEST-LATENCY` open. / Recursos conferidos e meta proposta pendente. |
| Composition | `SRC-BOOKING-BRIEF` revision 2; synthetic booking desk; migrated document revision 2. / Balcão sintético. | Three cases, shared rules and quality target; no stakeholder evidence or application result. / Três casos e regras compartilhadas, sem evidência de stakeholders/aplicação. |
| Task board | [Synthetic brief](../examples/task-board/needs.md) `SRC-TASK-BRIEF` revision 1; document revisions 2 and 3. / Fonte sintética e revisões documentais. | Three bounded cases; no numerical SLA; [actual delta](../examples/task-board/revisions/README.md). / Três casos delimitados, sem SLA numérico, delta real. |
| `SRC-TASK-OAL` in examples | Historical Alpha OAL source retained as authored provenance. / Origem Alpha preservada como proveniência autoral. | Not relabeled; current model claim separately uses reviewed Stable bytes. / Não relabelada; alegação atual usa Stable revisada separadamente. |
| Root artwork | Existing authored generator plus original illustrations; edition label updated. / Gerador e ilustrações existentes, rótulo atualizado. | Decorative, outside semantic resource catalogs. Unchanged diagrams/icons retained. / Decorativo; diagramas/ícones inalterados. |
| Translator, skill and publications | Package 1.0.0, Stable profile, canonical build helpers. / Pacote, perfil e auxiliares canônicos. | Codec/resource checks, isolated installation and visual PDF review; no arbitrary importer or business implementation. / Verificação e revisão visual, sem importador arbitrário ou aplicação. |

## Task-board contracts / Contratos do quadro

Reviewed inputs, outcomes, contexts, RFs, acceptance criteria, entity definitions and operation contracts in the JSON source against the brief. / Revisados esses elementos na fonte JSON contra o brief.

| Case / Caso | Review conclusion / Conclusão |
| --- | --- |
| `UC-TASK-CREATE` | Exact ID/title → canonical `VLD-TASK-NEW` → atomic uniqueness and one retained open task at revision zero. Invalid, denied and duplicate cases do not write; lost write confirmation remains `unknown`. / ID/título exatos, validação canônica, unicidade atômica e criação; recusa não grava, confirmação perdida permanece desconhecida. |
| `UC-TASK-COMPLETE` | ID validation → load ready entity/revision → canonical transition → conditional atomic update. Absence, already complete and version conflict preserve existing state; write failures retain uncertainty. / Validação, leitura, transição e atualização condicional; recusas preservam estado e falhas preservam incerteza. |
| `UC-TASK-LIST` | No business input; trusted board context → complete ordered consistent snapshot. Empty success requires confirmed emptiness; unavailable/malformed storage is failure, no partial success or write. / Sem entrada de negócio; snapshot ordenado completo; vazio confirmado, erro distinto e nenhuma escrita. |

All cases require a resolved authenticated caller, the selected board and their own permission. Request role labels cannot grant access; missing, unresolved, expired or insufficient contexts are denied before entity/tool work. `ASM-TASK-IDENTITY` records the unimplemented trust authority, and `ASM-TASK-SINGLE-BOARD` the teaching scope. `ENT-TASK` owns intrinsic validity; operation-level uniqueness, existence and revision checks remain contextual. Hydration validates raw records once, while tools consume ready entities. No database, protocol, route, executable application or later-layer verification is inferred.

Todos os casos exigem chamador autenticado resolvido, quadro e permissão específica. Rótulos de papéis não autorizam; contexto ausente/não resolvido/expirado/insuficiente é recusado antes de entidades/ferramentas. As premissas registram autoridade não implementada e escopo didático. A entidade é dona da validade intrínseca; unicidade, existência e revisão são contextuais. Hidratação valida registros brutos uma vez; ferramentas recebem entidades prontas. Não se infere banco, protocolo, rota, aplicação ou verificação posterior.

## RNF responsibility, origin and pending review / RNFs

| RNF | Owner and scope / Responsável e escopo | Observable acceptance / Aceite observável | Origin / Origem |
| --- | --- | --- | --- |
| `RNF-TASK-CREATE-RETENTION` | Create case, system scope; create/store/list. / Caso criar, escopo sistema. | Confirm create, normal restart, successful list contains exact task once. Shared list reference avoids duplicate definition. / Criação confirmada, reinício normal e leitura exata única; referência compartilhada. | Synthetic brief 1, choice 8 / Brief sintético 1, escolha 8. |
| `RNF-TASK-COMPLETE-ATOMICITY` | Complete case and store operation / Caso concluir e operação. | Same observed revision yields at most one confirmed write; other attempt conflicts or accurately fails. / Mesma revisão permite no máximo uma escrita confirmada. | Synthetic choice 6 / Escolha sintética 6. |
| `RNF-TASK-LIST-CONSISTENCY` | List case and store operation / Caso listar e operação. | One authorized snapshot, once per task, mutually consistent fields, no write; empty criterion now links explicitly. / Snapshot único autorizado e consistente, sem escrita; vínculo do aceite vazio explícito. | Synthetic choices 7–8 / Escolhas sintéticas 7–8. |
| `RNF-TASK-LIST-RETENTION` | List scope referencing create retention / Referência à retenção canônica. | Same canonical retention criterion / Mesmo critério canônico. | Synthetic choice 8 / Escolha sintética 8. |
| Minimal/composition response targets | Case interaction scope and explicit case references / Escopo de interação e referências aos casos. | Existing 2-second examples, defined stimulus/result interval and didactic configuration / Exemplos existentes de 2 segundos, intervalo e configuração definidos. | Explicit synthetic source; minimal has an open confirmation issue. Neither is a production SLA. / Fonte sintética; confirmação pendente no mínimo; nenhum é SLA de produção. |

Result: no blocking semantic contradiction found for these didactic specifications. Human review must confirm real stakeholder needs, trust assumptions, quantitative targets and production acceptance before adopting an example as a project specification. These are applicability limits, not unfinished requirements for a synthetic release fixture. No new SLA was introduced.

Resultado: nenhuma contradição semântica bloqueadora identificada no escopo didático. Adoção em projeto real exige revisão humana das necessidades, premissas de confiança, metas e aceite. São limites de aplicabilidade, não requisitos pendentes do fixture sintético. Nenhum SLA novo foi introduzido.
