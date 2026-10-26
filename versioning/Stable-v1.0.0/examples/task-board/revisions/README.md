# Task-board revisions / Revisões do quadro

Both [revision 2](revision-2.atlas.json) and [revision 3](revision-3.atlas.json) are valid instances of `Stable-v1.0.0`, with the same document and concept IDs. The [current JSON](../example.atlas.json) equals revision 3 byte-for-byte. Alpha → Stable migration is recorded separately in `HIST-MIGRATION-STABLE` and the [migration ledger](../../../verification/editorial-migration.json).

As duas revisões são instâncias válidas de `Stable-v1.0.0` com os mesmos IDs de documento e conceitos; o JSON corrente é idêntico em bytes à revisão 3. A migração Alpha → Stable está registrada separadamente.

| Change / Mudança | Before / Antes | After / Depois |
| --- | --- | --- |
| `AC-TASK-LIST-EMPTY` | Empty board returns empty success; unavailable store fails. / Quadro vazio retorna sucesso vazio; indisponibilidade falha. | Explicit consistent read with no change to task state/revision; failure never masquerades as empty success. / Leitura consistente explícita sem alterar estado/revisão; falha nunca disfarçada de sucesso vazio. |
| `verifies` | Snapshot and failure RFs. / RFs de snapshot e falha. | Same RFs plus `RNF-TASK-LIST-CONSISTENCY`. / Mesmos RFs, mais o RNF de consistência. |
| Revision/history / Revisão/histórico | Revision 2 / Revisão 2 | Revision 3 plus `HIST-TASK-BOARD-03`; earlier history retained. / Revisão 3 e nova entrada; histórico anterior preservado. |

Reason: expose an existing obligation from synthetic `SRC-TASK-BRIEF` revision 1, choices 7–8, in the empty-list acceptance criterion. No new domain behavior, renamed concept or invented reference replacement. Prepared by Codex under Douglas de Oliveira Alkimim's execution request; this is not stakeholder approval. Impact: regenerate the traceability matrix, Markdown, LaTeX and PDF. No downstream application artifacts exist to revalidate.

Motivo: explicitar obrigação existente das escolhas 7–8 da fonte sintética no aceite da lista vazia. Nenhum comportamento de domínio novo, conceito renomeado ou substituição fictícia de referência. Preparado por Codex sob o pedido de execução de Douglas de Oliveira Alkimim, sem alegar aprovação de stakeholders. Impacto: regenerar matriz, Markdown, LaTeX e PDF. Não existem artefatos de aplicação posteriores para revalidar.

`tests/test_stable_contract.py` validates both snapshots, verifies the exact intended delta and current-file equality, and constructs an invalid `ENT-UNKNOWN` reference only in temporary test storage. Rejected conversion leaves no output. The distributed examples remain valid.

O teste valida snapshots, delta intencional e igualdade do arquivo corrente; a referência inválida existe somente em temporário e sua conversão não produz saída. Os exemplos distribuídos permanecem válidos.
