# Stable-v1.0.0 — release verification / Verificação da release

**Verified local delivery on `main`; no GitHub publication. Douglas de Oliveira Alkimim is confirmed as responsible for review and traceability of the editorial migration. No stakeholder or example-requirement approval is asserted.**

**Entrega local verificada na `main`; sem publicação no GitHub. Douglas de Oliveira Alkimim foi confirmado como responsável pela revisão e rastreabilidade da migração editorial. Não se afirma aprovação dos requisitos dos exemplos ou de stakeholders.**

Model/profile `Stable-v1.0.0`, package `atlas-spec` 1.0.0. The separate working branch was merged and removed locally before these final adjustments. No push, tag, release or Todoist update was performed. The read-only release query returned no published releases: [captured state](evidence/final-publication-state.json).

Modelo/perfil e pacote mantêm suas identidades. A branch separada foi integrada e removida localmente antes desta rodada. Não houve push, tag, release ou alteração do Todoist.

## OAL repository URL update / Atualização do endereço OAL

The [current OAL repository](https://github.com/CodeVaultCommunity/OAL_OpenAnalysisLayers) replaces its former address in current root/edition documentation, baseline metadata and generated skill references. [Scoped evidence](evidence/oal-repository-url-update.json) records the repository and historical-source redirect checks, unchanged snapshot hashes and affected-file verification. The root inventory and final ZIP are regenerated. The OAL pin remains `ce225141686d4b6b3e46923866c97d84c031903f`.

Only documentation and location metadata changed after Atlas `4160eb23c853df9629e30ad32c5421eab433dcef`. Its 253-test runs remain prior implementation evidence; full tests and PDF rendering were not repeated for this URL-only change. Runtime, examples, historical revisions, fixtures, PDFs and normative snapshots retain their bytes. Current skill consistency, local links, inventory and archive/extraction checks are repeated; final package identities are in the external receipt.

A renomeação atualiza os links atuais e os hashes dos arquivos afetados, sem alterar o contrato nem os bytes normativos. URLs autorais históricas foram preservadas; o link antigo com commit fixado continua acessível por redirecionamento. Entrega somente local, sem push, tag ou release.

## Local preparation at 4160eb2 / Preparação local em 4160eb2

The [execution record for that preparation](evidence/local-release-checks.json) reports **253 tests on each of Python 3.11.15 and 3.12.14**: 220 edition tests plus 33 repository distribution tests. The previous nine inventory regressions moved from the edition into the root suite and retain ordering/mutation coverage; additional cases cover full Alpha/evidence/CI inclusion, malformed metadata, ZIP duplicates/prefixes/symlinks, clean extraction without Git or cache creation, indexed additions/deletions and real committed-archive creation. [Python 3.11 log](evidence/local-release-tests311.txt), [Python 3.12 log](evidence/local-release-tests312.txt).

The single root `CONTENT-SHA256.json` replaces the active per-edition `release-inputs.json` and its capture helper. It covers every indexed delivery file except itself, including this report and all completed evidence. Repository checks and packaging now live in `scripts/`; the OAL schema pattern is adapted with `atlas_edition` from `CITATION.cff`. Generation uses actual bytes and deterministic POSIX path order; checking accepts equivalent record order while rejecting duplicates and real content changes. Final inventory/ZIP identities and complete archive/extraction verification are recorded externally to avoid circular hashes.

`CLAUDE.md` only points to `AGENTS.md`. Agent guidance prioritizes the requested edition and document identities, otherwise selects the highest available Stable by numeric version components. The release procedure is maintained in [English](../../../docs/releasing.md) and [Portuguese](../../../docs/releasing.pt-br.md). CI now checks the root suite, complete inventory, ZIP and extraction in its Windows/Linux matrix; remote execution is not claimed.

The [24 conversions](evidence/local-release-examples.txt) and [27 generated skill files](evidence/local-release-skill.txt) pass. Current [local links](evidence/local-release-links.json) were checked. Runtime, representation contracts, examples, PDFs, OAL snapshots and all 98 Alpha files remain unchanged from `44e082cf922874b263617f394f28ce2e939368a7`; PDFs were not rebuilt. Existing visual evidence remains scoped to its original run. Historical checkpoint inventories and logs are retained, not regenerated.

Foram executados **253 testes em cada versão Python**, além das conversões, skill e links. O inventário único cobre toda a entrega, exceto a si mesmo; os inventários antigos são apenas registros históricos. A responsabilidade de Douglas pela revisão e rastreabilidade da migração foi confirmada explicitamente, sem declarar aprovação dos requisitos dos exemplos. Esta rodada termina em commit e pacote locais, sem push, tag ou release remota.

## Provenance and actual inputs / Proveniência e entradas reais

| Item | Evidence / Evidência |
| --- | --- |
| Technical scope / Escopo | [Original execution plan](https://chatgpt.com/space/page_3a58a158b920819186501003e9d6c132) and [final adjustments](https://chatgpt.com/space/page_c11382812bfc81919d33b73b8bc8a175). |
| Audited Alpha source | `ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04`; 98 files deliberately reused in the independent Stable edition. |
| Defect reproduction | `d3d485e66590add17cda50b391d657b53aeb127c`; regressions captured before changing edition identities. |
| Fixed checkpoint | `fd2e2a94e7673cde1bf879eda65281c219a09754`; [historical report](CHECKPOINT.md), 198 tests. |
| Previous Stable candidate | `e3552b4508a3cd84aee153cb3920ca7314e851c7`; 209 tests, 24 conversions, 27 skill files, 137 PDF pages. Its [155-record inventory](evidence/e3552b4-release-inputs.json) retains its historical scope and hashes. Its report is available in that Git commit. |
| Current inventory | Root [CONTENT-SHA256.json](../../../CONTENT-SHA256.json): every indexed delivery file except itself, with POSIX identities, exact byte sizes and SHA-256. Includes Alpha, reports, evidence, scripts and CI. The active per-edition inventory was removed. |
| Alpha preservation | [Final comparison](evidence/final-alpha-preservation.json): all **125** initial file/directory records equal, including **98 files**, sizes, bytes, attributes and Windows ACL SDDL. |
| Final OAL baseline | Local commit `ce225141686d4b6b3e46923866c97d84c031903f`, tree `dedf80b6ca53e43d5ee76c877471e9cfe041a86c`; canonical ZIP and Git blobs independently compared. [Identity and hashes](oal/baseline.json), [19-clause review](OAL-CORRESPONDENCE.md). |
| OAL English manual | `versioning/Stable-v1.0.0/README.md`, **63838 bytes**, SHA-256 `d6ad987008c200460af919eff3b03989dca5a3b0f7e14d7a9d5b4e67f598b2da`. Portuguese and canonical license hashes are in the baseline record. |
| Editorial cleanup | [Migration ledger](editorial-migration.json) keeps old migration hashes and adds six separate before/after records. [Exact JSON delta check](evidence/final-editorial-check.json) verifies only the declared history text fields changed. |

The complete OAL normative bodies, including 46 numbered rules in each language, are byte-identical to the prior Stable snapshot. The ten UCS and nine cross-layer assessments were reconfirmed. The delta is editorial/operational; launcher changes do not change the normative contract. `SRC-TASK-OAL` remains historical Alpha provenance. Public availability of either final local commit is not asserted.

Os corpos normativos OAL permanecem idênticos; as 19 cláusulas aplicáveis foram reconfirmadas. A referência histórica dos exemplos foi preservada. A identidade final Atlas e o SHA-256 do ZIP efetivo são entregues fora do próprio commit, no recibo e no chat, evitando hashes circulares.

## OAL reference refresh / Atualização da referência OAL

On 2026-10-26, the OAL pin was refreshed from `bdea8a4269e2788f25b68d2925c125d7e62c04ed` to `ce225141686d4b6b3e46923866c97d84c031903f`. The [new comparison](evidence/oal-ce225141-reference-update.json) records exact Git/archive/extraction equality, both introductory diffs and unchanged normative bodies. The previous reference update remains in the [baseline history](oal/baseline.json) and [original evidence](evidence/final-oal-reference.json).

Only OAL snapshots, provenance, generated skill references, the release documentation and then-current covered-input inventory changed relative to Atlas `c084786d2298be784cf0a713fdbfa7d5c6d5bdf0`. The runtime, schema, profiles, examples, PDFs and Alpha content are unchanged. The 229-test runs on each Python version and the 123-page visual review below belong to that predecessor; they were not rerun for this document-only refresh. That OAL reference refresh repeated the 24 directed conversions, 27-file skill consistency, local links and then-current 163-input inventory; their actual outputs are recorded in [refresh verification](evidence/oal-ce225141-checks.json). The new ZIP is checked against its commit and again after extraction, with results in its external receipt.

Em 2026-10-26, os snapshots, o pin, a skill e o inventário foram sincronizados com a nova revisão OAL. Apenas dois parágrafos introdutórios mudaram em cada idioma. As 46 regras por idioma, as 19 correspondências aplicáveis e a licença continuam iguais. Os testes completos e a inspeção dos PDFs são evidências preservadas do commit Atlas anterior; esta atualização documental repete as verificações afetadas e registra o novo pacote separadamente.

## Final adjustments / Ajustes finais

The release checker now sorts relative POSIX strings and compares records by path, rejecting duplicates before indexing. Missing/added paths, sizes and hashes have separate diagnostics. Nine regressions cover Windows/POSIX/shuffled order and real mutations; [before-fix output](evidence/final-inventory-before.txt) records eight failures and one pass. CI retains Windows/Ubuntu and Python 3.11/3.12 and now checks the inventory. The traceability generator writes LF explicitly so Git checkout does not change its captured bytes.

O manifesto passou a comparar identidade e conteúdo, sem depender da ordem de enumeração. O gerador da matriz usa LF explícito. O [empacotador atual](../../../scripts/build_distribution.py) arquiva arquivos commitados e recusa temporários versionados. A [reprodução da distribuição](DISTRIBUTION.md) funciona sem `.git` no ZIP extraído.

Editorial production/request credits were removed from canonical starter/examples and both task-board revisions, then regenerated into MD/TeX/PDF and the portable skill. IDs, dates, revisions, technical reasons, historical source identities and approval limits remain. The task-board current JSON is byte-identical to revision 3; the exact revision 2→3 teaching delta still passes. Equivalent credits were removed from current reports and refreshed OAL snapshots; human authors, licenses, conceptual AI references and functional agent guidance remain.

O ledger agora registra `responsibility_status: confirmed` e `responsible_person: Douglas de Oliveira Alkimim`, após confirmação explícita do usuário em 2026-10-26. O escopo é revisão e rastreabilidade da migração editorial. `human_approval_asserted: false` continua indicando que não se declarou aprovação dos requisitos dos exemplos ou de stakeholders; a autoria, isoladamente, não foi usada para inferir responsabilidade.

The shared presenter automatically applies compact metadata pairs and catalogs, three-column entity fields, full-width long contracts and oversized table rows, repeated table headings, and main-section page breaks. The first section can share the document metadata page. All 16 graphs occur once beside their explicit owners; shared validations link to their canonical definitions. The technical index preserves authoritative nodes/edges and links to owners/figures. The renderer measures the actual diagram height and uses 9.5 pt node text / 8.5 pt edge keys; all reference graphs render at scale 1.0000.

A apresentação é automática, sem campos novos no payload ou edição manual dos exemplos. Tabelas longas quebram entre linhas; uma linha excessiva vira detalhe de largura completa. Os slots autoritativos aparecem uma única vez. Os fixtures Stable anteriores, saneados com o runtime antigo antes da mudança visual, continuam aceitos; somente as formas TikZ legada e atual exatamente regeneradas são válidas.

## Four defects and additional boundary case / Defeitos corrigidos

Before fixes, the new regression suite recorded **50 failures and 28 passes**, while identities were still Alpha: [raw output](evidence/regressions-before.txt). This avoids confusing unsupported-version rejection with reproduction. The original Alpha examples already passed their conversion checks; those successes did not cover these defects.

Antes das correções, as regressões registraram **50 falhas e 28 aprovações**, ainda com identidades Alpha. Os exemplos Alpha já passavam, sem cobrir esses defeitos.

| Defect / Defeito | Corrected behavior and evidence / Comportamento e evidência |
| --- | --- |
| A — Optional entity records / Registros opcionais | Absent `assumptions`/`open_issues` no longer raise `KeyError` or insert `[]`; invalid `null` receives Atlas diagnostics. API and CLI tests preserve absence in six directions. / Ausência preservada, `null` inválido diagnosticado. |
| B — Typed references / Referências tipadas | Figures at all supported rich-block depths resolve against resources; sources/assumptions/issues resolve against their catalogs, without prefix heuristics. Invalid input cannot create/overwrite output. Opaque data and boundary mapping labels remain data. [Field inventory](reference-inventory.md). / Resolução por categoria e ausência de escrita em falha, preservando dados opacos. |
| C — LaTeX line endings / Quebras LaTeX | Distinct CRLF/CR/LF reversible macros, canonical style support, tabs/spaces/Unicode/literal macro text retained. Default verified CLI succeeds. Compiled [smoke evidence](CHECKPOINT.md#latex-smoke-publication--publicação-latex-de-verificação). / Escapes distintos, preservação e compilação. |
| D — Unicode separators / Separadores Unicode | Structural lines split only on physical CR/LF/CRLF; U+0085/U+2028/U+2029 remain literal data in text and opaque containers. Generated LaTeX decodes and compares exactly. / Separadores preservados em prosa e dados opacos. |
| Final CR boundary / CR final | Prevented authored final CR from merging with structural LF; four public roundtrip cases cover paragraph, heading, list and code. / Quatro casos cobrem a fronteira adicional. |

The earlier Stable checkpoint added 11 tests for incompatible versions, unchanged producer/history and the exact revision delta. All original 116 tests remain, plus 82 regression cases: **209 at the previous candidate**; the publication adjustment added 20 focused tests, for **229 total at c084786**. The current suite has 220 edition tests and 33 root distribution tests, retaining and extending the nine relocated inventory cases. The [compatibility policy](../COMPATIBILITY.md) separates correcting acceptance of already-invalid input from introducing a new semantic restriction. No generic migration, arbitrary LaTeX parser, PDF importer or business application was added.

A política distingue corrigir aceitação de entrada já inválida de introduzir restrição nova. Não foram acrescentados migrador genérico, parser LaTeX arbitrário, importador PDF ou aplicação de negócio.

## Earlier implementation checks / Verificações anteriores da implementação

The following implementation evidence belongs to Atlas `c084786d2298be784cf0a713fdbfa7d5c6d5bdf0`; current execution is recorded above. Fresh external environments on Windows, Python **3.11.15** and **3.12.14**. Dependency installation used `uv pip install -e ".[test,assets]"`; [exact versions](evidence/final-environments.json) are recorded. No supplied `.venv` was used. Python 3.11 ran against a controlled archive opened and extracted without Git, caches or environments. [Preparation receipt](evidence/final-clean-preparation.json), [pre-regeneration manifest check](evidence/final-clean-manifest.txt).

Ambientes novos fora da distribuição; a cópia Python 3.11 foi extraída de um ZIP controlado. A sequência executada foi skill → exemplos/PDF → pytest → exemplos/check → skill/check. Depois do ajuste LF do helper, as conversões e suítes completas foram repetidas nos dois ambientes. O ZIP definitivo é produzido do commit final; seu recibo externo registra a inspeção, extração, instalação e manifesto dos bytes efetivamente entregues.

| Check / Verificação | Observed result / Resultado observado |
| --- | --- |
| Python 3.12 full suite | **229 passed**; [raw log](evidence/final-tests312.txt). |
| Python 3.11 full suite, clean copy | **229 passed**; [raw log](evidence/final-tests311.txt). Includes wheel/editable installation and independent portable skill. |
| `python examples/build.py --check` | **24 directed conversions**; all complete payloads equal, including starter and revision matrix. [Source checkout](evidence/final-examples.txt), [clean copy](evidence/final-clean-examples.txt). |
| `python skills/build.py --check` | **27 generated files** consistent. [Source checkout](evidence/final-skill.txt), [clean copy](evidence/final-clean-skill.txt). |
| `python examples/build.py --pdf` | Three PDFs, two successful passes each, source checkout and clean distribution. [Source build](evidence/final-publication.txt), [clean build](evidence/final-clean-publication.txt). |
| New publication regressions | Eleven tests: three full legacy/current payload comparisons, long/special table content, stale TikZ in both forms, missing/duplicate/orphan/malformed slots and valid cell editing. Principal/subflow and shared-validation examples included. |
| Long publication smoke | 90-row repeated-header table, oversized row, long field and special characters/whitespace; exact payload roundtrip, two PDF passes, **30 pages** rendered and inspected. [Compiler output](evidence/final-smoke-pdflatex.txt), hashes in publication review. |
| Inventory | **163** covered inputs; portable order-independent comparison and mutation/duplicate diagnostics. Final check runs after capture; output ZIP is checked again after extraction. |
| Local links | **674** targets, including **260** fragments across 50 current Markdown files; no unresolved links. [Scan](evidence/final-links.json). |
| Whitespace check | Authored changes pass `git diff --check`. Raw evidence and legacy fixtures are excluded: two fixture text records deliberately contain spaces, preserved for exact import rather than trimmed as code whitespace. |
| Editorial/OAL/Alpha | Six declared JSON deltas, current task-board equals revision 3, both OAL manuals equal pinned blobs, all 46 rules unchanged, 125 Alpha records preserved. |

### Publication review / Revisão da publicação

MiKTeX-pdfTeX 4.23 / MiKTeX 25.12, shell escape disabled. **All 123 example pages** were rendered and visually inspected, plus all 30 smoke pages. Detailed inspection covered metadata, fields, tools, case/section starts, the semantic image, technical tables, small/large diagrams, histories and special characters. The final PDFs contain no identified clipping, overlaps, missing glyphs or orphan use-case titles. All **86 internal links** resolve to pages containing their target IDs. No bookmarks were added. No overfull boxes or missing glyphs appear in final compiler logs. Underfull alignment warnings remain in sparse tables; their rendered cells were checked and retained. The shell-escape/MiKTeX update notices do not indicate compilation failure.

| Example | Previous pages | Final pages | Graphs |
| --- | ---: | ---: | ---: |
| Minimal | 28 | 25 | 3 |
| Composition | 54 | 49 | 7 |
| Task board | 55 | 49 | 6 |

Fields previously stacked over several pages are now compact tables; long text remains wide. Graphs moved from a separate illustrated appendix to their owners, with a compact technical index retained. The task-list case title is accompanied by content. Main semantic sections start on new pages. Natural end-of-section whitespace remains; page count is an observation, not an optimization target. PDF is publication only, not an import format or a full payload-equality proof.

As 123 páginas finais e 30 páginas de teste foram inspecionadas. Campos curtos ficaram compactos e textos extensos preservaram largura. Grafos e links foram conferidos; os logs registram avisos de alinhamento sem cortes observados. Espaço natural ao final das seções foi preservado. A fidelidade integral é demonstrada em JSON/MD/LaTeX, enquanto o PDF recebe revisão visual de publicação.

[Hashes, links, fonts and review scope](evidence/final-publication-review.json) · [minimal compiler log](evidence/final-minimal-pdflatex.txt) · [composition log](evidence/final-composition-pdflatex.txt) · [task-board log](evidence/final-task-board-pdflatex.txt).

Historical evidence files retain their original bytes and refer to their checkpoints. New outputs use the `final-` prefix; `.gitattributes` preserves raw evidence without line-ending conversion. Rendered contact sheets, original comparison PDFs and temporary environments stay outside the distribution.

## S01-D01–D07 evidence matrix / Matriz de evidências

| Item | Real evidence / Evidência real | Human review needed / Revisão humana necessária | Result and pending scope / Resultado e pendência |
| --- | --- | --- | --- |
| D01 | [Material inventory](SEMANTIC-REVIEW.md), source hashes, root/edition maps, labeled synthetic briefs. / Inventário, hashes e fontes sintéticas identificadas. | Confirm intended release scope / Confirmar escopo da release. | Delivered; no missing required source / Entregue; nenhuma fonte obrigatória ausente. |
| D02 | Valid Stable revisions 2/3, exact delta test, preserved IDs/history and invalid temporary reference rejection. / Revisões, delta, IDs e rejeição. | Review reason/impact / Revisar motivo e impacto. | Delivered; current JSON equals revision 3 / Entregue; JSON corrente igual à revisão 3. |
| D03 | Three cases reviewed against inputs/results/auth/persistence in [semantic review](SEMANTIC-REVIEW.md). | Approve real project requirements only if adopting the teaching example / Aprovar requisitos reais apenas em adoção. | Consistent didactic scope; application behavior not claimed / Escopo didático consistente; aplicação não alegada. |
| D04 | Canonical entity rules, ready-entity tool contracts, contextual atomic checks and known/unknown failure distinction. | Review implementation feasibility when selecting a store / Revisar viabilidade ao escolher armazenamento. | Delivered as contracts; implementation outside scope / Contratos entregues; implementação fora do escopo. |
| D05 | RNF owner/scope/origin/criterion matrix and existing open target issue; no invented SLA. | Confirm teaching assumptions and response targets before production / Confirmar premissas/metas antes de produção. | Delivered; didactic applicability limits explicit / Entregue; limites didáticos explícitos. |
| D06 | JSON retained, 24 conversions, resource hashes, three rebuilt/inspected PDFs and defect comparison above. | Publication review remains available / Revisão de publicação disponível. | Delivered; Alpha passes distinguished from new regressions / Entregue; regressões diferenciadas dos passes Alpha. |
| D07 | Pinned/reviewed OAL, 253 actual tests on each of Python 3.11 and 3.12, preservation, complete root inventory/logs and explicit limits. | Final release decision / Decisão final de release. | Local delivery verified; migration responsibility confirmed / Entrega local verificada; responsável pela migração confirmado. |

## Remaining limits and reproduction / Limites e reprodução

Douglas de Oliveira Alkimim is **confirmed** as accountable for review and traceability of the editorial migration. This does not establish approval of the example requirements. The user explicitly requested a local commit without GitHub publication. Linux and GitHub Actions are configured but were not executed in this local run. Only Windows, Python 3.11/3.12 and pdfLaTeX have execution evidence here; XeLaTeX/LuaLaTeX and business application behavior are not claimed. Unusually large external graphs still require publication review.

O responsável pela migração está confirmado; a entrega foi explicitamente limitada a commit local, sem publicação. Linux/Actions e outros engines não foram executados nesta rodada. Não há evidência alegada de aplicação real ou de camadas L2–L4; as entregas didáticas D01–D07 continuam distintas de aprovação humana e do estado administrativo no Todoist.

Use the [root release procedure](../../../docs/releasing.md) for packaging, extraction and installation. From the repository root, run `python scripts/content_inventory.py --check`; against a delivered ZIP or extracted repository, run `python scripts/check_archive.py PATH` **before** regeneration. Rebuilding a PDF may change its timestamps and hash; a rebuilt candidate requires another inventory. Preserve historical checkpoint manifests. The final Atlas commit and actual ZIP SHA-256 belong in the external delivery receipt, not inside their own hashed inputs.
