# Stable-v1.0.0 — release verification / Verificação da release

**Prepared for human review as a concrete release candidate. Publication pending. / Preparada para revisão humana como candidata concreta. Publicação pendente.**

Atlas model/profile `Stable-v1.0.0`, package `atlas-spec` 1.0.0, branch `codex/atlas-stable-v1.0.0`. The authorized work prepares a local candidate; it does not publish, tag, push or close Todoist tasks. Review performed by Codex under Douglas de Oliveira Alkimim's execution request, 2026-10-25, America/Sao_Paulo. No stakeholder approval is asserted.

O trabalho autorizado prepara uma candidata local, sem publicação, tag, push ou encerramento de tarefas. A revisão por agente não constitui aprovação de stakeholders.

## Provenance and actual inputs / Proveniência e entradas reais

| Item | Evidence / Evidência |
| --- | --- |
| Execution request / Pedido | [Atlas execution plan](https://chatgpt.com/space/page_3a58a158b920819186501003e9d6c132), sequence 1. |
| Audited source / Origem auditada | `ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04`; initially clean `main`. |
| Reproduction commit / Reprodução | `d3d485e66590add17cda50b391d657b53aeb127c`: copied 98 tracked Alpha files and added regressions before changing identities. / Cópia dos 98 arquivos Alpha e regressões anteriores à mudança de identidade. |
| Fixed checkpoint / Correções | `fd2e2a94e7673cde1bf879eda65281c219a09754`; [historical report](CHECKPOINT.md), 198 passing tests, followed by the requested OAL pause. / Relatório histórico com 198 testes e pausa solicitada. |
| Current inputs / Entradas atuais | [release-inputs.json](release-inputs.json): **155 files** with bytes/SHA-256, captured before this report. Includes Stable sources/derivatives, root navigation/artwork and CI. / Capturados antes do relatório, incluindo fontes/derivados, raiz e CI. |
| Exclusions / Exclusões | Report, release description, manifest itself, evidence outputs, caches, environments/build intermediates, and historical Alpha (separate preservation inventory). All exclusions are explicit in the manifest. / Exclusões explícitas, sem hash autorreferente. |
| Alpha preservation / Preservação | [Initial manifest](evidence/alpha-initial.json) was captured outside the repository before edits. [Final check](evidence/stable-alpha-preservation.txt): **125 equal file/directory records**, including bytes, sizes, attributes and Windows ACL SDDL. / Registros iguais, incluindo permissões. |
| OAL baseline / Baseline OAL | `a02bf8eecf222e7e0a7a34977fff49a25b5af6aa`; normative `versioning/Stable-v1.0.0/README.md`, SHA-256 `8e3d82be109b1e8baf1deab32b338b568aa7c98d407858456620336c76ce499e`. [Exact local provenance and EN/PT hashes](oal/baseline.json), [19-clause review](OAL-CORRESPONDENCE.md). / Proveniência local verificada, sem afirmar commit publicado. |
| Editorial changes / Mudanças editoriais | [Migration ledger](editorial-migration.json) and [two valid task-board revisions](../examples/task-board/revisions/README.md). All source and result hashes checked. / Hashes de origem e resultado conferidos. |

The final Atlas commit SHA is supplied outside the files belonging to that commit, in the delivery message. The manifest covers working bytes actually checked; historical checkpoint hashes apply only at their recorded commit. No normative input was changed after final capture.

O SHA final Atlas é entregue no chat, fora dos arquivos do próprio commit. O manifesto cobre bytes reais verificados; hashes do checkpoint histórico aplicam-se ao commit registrado. Nenhuma entrada normativa mudou após a captura final.

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

The Stable release adds 11 tests for incompatible versions, unchanged producer/history and the exact revision delta. All original 116 tests remain, plus 82 regression cases: **209 total**. The [compatibility policy](../COMPATIBILITY.md) separates correcting acceptance of already-invalid input from introducing a new semantic restriction. No generic migration, arbitrary LaTeX parser, PDF importer or business application was added.

A política distingue corrigir aceitação de entrada já inválida de introduzir restrição nova. Não foram acrescentados migrador genérico, parser LaTeX arbitrário, importador PDF ou aplicação de negócio.

## Executed checks / Verificações executadas

Windows 11, Python **3.12.14**, isolated `.venv`, package 1.0.0 installed with test/asset dependencies. [Exact dependency versions](evidence/stable-environment.json), including pytest 9.1.1, jsonschema 4.26.0 and CairoSVG 2.9.1. Commands run from the edition unless indicated. Logs are process output, not reconstructed test results.

Ambiente e versões exatas estão registrados; logs são saídas reais dos processos. A ordem foi fontes canônicas → skill/schema/estilo empacotados → exemplos/matriz/PDF → checks.

| Command / Comando | Observed result / Resultado observado |
| --- | --- |
| `python -m pip install --no-build-isolation --no-deps -e .` | Installed 1.0.0 using already installed test/asset extras. / Instalou 1.0.0 com dependências presentes. |
| `python skills/build.py` | **27 generated files**, including new compatibility policy and diagnostic catalog; runtime schema/style synchronized first. / Gerados e sincronizados antes dos exemplos. |
| `python examples/build.py --pdf --keep-intermediates` | Four JSON sources → Markdown/LaTeX; task-board matrix; **three PDFs, two successful passes each**. [Build output](evidence/stable-publication.txt). |
| `python -m pytest tests --tb=short -q` | **209 passed, 229.81 s**. [Full log](evidence/stable-tests.txt). Includes wheel/editable installation, copied edition/skill, resources, six directions and new contract tests. |
| `python examples/build.py --check` | **24 directed conversions**; three examples plus starter and matrix consistent. [Log](evidence/stable-examples.txt). |
| `python skills/build.py --check` | **27 files verified**, no drift. [Log](evidence/stable-skill.txt). |
| `python verification/capture_release.py --check` | **155 inputs** match captured bytes. / Entradas correspondem aos bytes capturados. |
| Local link scan / Inspeção de links locais | Markdown/HTML file targets and Markdown fragments checked, excluding code examples/caches. [Counts and findings](evidence/stable-links.json); no unresolved local links at delivery. / Sem links locais pendentes na entrega. |
| `git diff --check` and staged equivalent / equivalente staged | No whitespace errors in authored changes; raw logs retain intentional original whitespace. / Sem erros autorais; logs preservados. |

### Publication review / Revisão da publicação

**MiKTeX-pdfTeX 4.23 / MiKTeX 25.12**, shell escape disabled. Recompiled minimal (**28 pages**), composition (**54**) and task board (**55**). All **137 pages** were rendered and visually inspected through contact sheets; detailed views checked the semantic image, complex graphs/edge legends and both versioned banners. The earlier compiled regression fixture covers table cells, whitespace, accents and reversible macros. No clipped/overlapping content or missing glyphs was observed; TeX logs have no overfull/underfull boxes. The `epstopdf` shell-escape warning is expected; existing PNG variants were used.

As 137 páginas recompiladas foram renderizadas e inspecionadas, com vistas detalhadas de imagem, grafos/legendas e banners. Não foram observados cortes, sobreposições ou glifos ausentes. O aviso de shell escape é esperado; variantes PNG existentes foram usadas. A inspeção visual é revisão por agente, não teste automatizado.

[PDF hashes and review scope](evidence/stable-publication-review.json) · [minimal log](evidence/minimal-pdflatex.txt) · [composition log](evidence/composition-pdflatex.txt) · [task-board log](evidence/task-board-pdflatex.txt).

Only banner labels changed in root artwork; unchanged diagrams/icons were retained after running the canonical generator. Contact sheets and temporary renders remain outside the repository in the task's `atlas-stable-evidence/stable-pdfs` directory. The portable skill/wheel has no environments or caches; generated runtime/source correspondence is checked.

Somente rótulos dos banners mudaram; diagramas e ícones foram preservados. Temporários ficam fora do repositório; skill/wheel não contêm ambientes ou caches.

## S01-D01–D07 evidence matrix / Matriz de evidências

| Item | Real evidence / Evidência real | Human review needed / Revisão humana necessária | Result and pending scope / Resultado e pendência |
| --- | --- | --- | --- |
| D01 | [Material inventory](SEMANTIC-REVIEW.md), source hashes, root/edition maps, labeled synthetic briefs. / Inventário, hashes e fontes sintéticas identificadas. | Confirm intended release scope / Confirmar escopo da release. | Delivered; no missing required source / Entregue; nenhuma fonte obrigatória ausente. |
| D02 | Valid Stable revisions 2/3, exact delta test, preserved IDs/history and invalid temporary reference rejection. / Revisões, delta, IDs e rejeição. | Review reason/impact / Revisar motivo e impacto. | Delivered; current JSON equals revision 3 / Entregue; JSON corrente igual à revisão 3. |
| D03 | Three cases reviewed against inputs/results/auth/persistence in [semantic review](SEMANTIC-REVIEW.md). | Approve real project requirements only if adopting the teaching example / Aprovar requisitos reais apenas em adoção. | Consistent didactic scope; application behavior not claimed / Escopo didático consistente; aplicação não alegada. |
| D04 | Canonical entity rules, ready-entity tool contracts, contextual atomic checks and known/unknown failure distinction. | Review implementation feasibility when selecting a store / Revisar viabilidade ao escolher armazenamento. | Delivered as contracts; implementation outside scope / Contratos entregues; implementação fora do escopo. |
| D05 | RNF owner/scope/origin/criterion matrix and existing open target issue; no invented SLA. | Confirm teaching assumptions and response targets before production / Confirmar premissas/metas antes de produção. | Delivered; didactic applicability limits explicit / Entregue; limites didáticos explícitos. |
| D06 | JSON retained, 24 conversions, resource hashes, three rebuilt/inspected PDFs and defect comparison above. | Publication review remains available / Revisão de publicação disponível. | Delivered; Alpha passes distinguished from new regressions / Entregue; regressões diferenciadas dos passes Alpha. |
| D07 | Pinned/reviewed OAL, 209 actual tests, preservation, manifests/logs and explicit limits. | Final release decision / Decisão final de release. | Candidate ready for review; no known technical blocker / Candidata pronta para revisão; sem bloqueador técnico conhecido. |

## Remaining limits and reproduction / Limites e reprodução

Python **3.11**, Linux and remote GitHub Actions were **configured, not executed locally**. CI covers 3.11/3.12 on Ubuntu/Windows, plus an Ubuntu 24.04 TeX publication job; configuration is not a CI result. Only Windows Python 3.12 and pdfLaTeX were verified here; XeLaTeX/LuaLaTeX were not. Real application behavior and stakeholder approval remain outside this didactic edition's evidence. Future broader platform/engine testing is an improvement, not a substituted result.

Python 3.11, Linux e Actions remotas foram configurados, não executados localmente. Somente Windows/Python 3.12/pdfLaTeX possuem evidência desta execução; outros engines e comportamento de aplicação não foram alegados.

To reproduce in a fresh environment, install Python 3.11+ and pdfLaTeX with the packages declared by the LaTeX guide, then run from this edition:

```bash
python -m venv .venv
# Activate the environment for your shell.
python -m pip install -e ".[test,assets]"
python skills/build.py
python examples/build.py --pdf
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

`capture_release.py --check` checks the delivered bytes before regeneration; rebuilding PDFs may change engine timestamps/bytes and requires a new manifest for that run. Preserve the historical checkpoint and Alpha manifests. Use the [proposed release description](RELEASE-DESCRIPTION.md) for the review decision; no remote action is implied.

O verificador confere bytes entregues antes de regenerar; PDFs recompilados podem mudar timestamps/bytes e exigem novo manifesto da execução. Preserve os manifestos históricos. A descrição proposta serve à decisão de revisão, sem ação remota implícita.
