# Stable preparation checkpoint / Checkpoint de preparação da Stable

> Historical evidence at commit `fd2e2a94e7673cde1bf879eda65281c219a09754`, retained without rewriting its results. The OAL dependency was subsequently delivered; see [the release verification](RELEASE.md). Run the checkpoint capture/check command only at that checkpoint; use `capture_release.py` for current inputs. / Evidência histórica preservada; dependência OAL posteriormente entregue. Use o verificador do checkpoint naquele commit e `capture_release.py` nas entradas atuais.

**2026-10-25, America/Sao_Paulo — paused at the user's request pending finalized OAL content. This is not an approved Stable release or release candidate.**

**25/10/2026, America/Sao_Paulo — pausado a pedido do usuário, aguardando conteúdo final do OAL. Não é uma release Stable aprovada nem um candidato à release.**

The four audited defects have been corrected in the working copy under `versioning/Stable-v1.0.0/`. Model/profile identities remain `Alpha-v0.1.0`, and package/producer identifiers remain `0.1.0` at this checkpoint. This is deliberate: reproduction preceded any version change, and the user then requested a pause when OAL content became necessary. Do not distribute this working copy as either the historical Alpha implementation or a finalized Stable profile.

Os quatro defeitos auditados foram corrigidos na cópia de trabalho em `versioning/Stable-v1.0.0/`. As identidades de modelo/perfil continuam `Alpha-v0.1.0` e as de pacote/produtor continuam `0.1.0`. Isso é intencional: as regressões foram reproduzidas antes de mudar versões e o usuário pediu uma pausa quando o conteúdo OAL fosse necessário. Não distribuir esta cópia como a implementação Alpha histórica nem como um perfil Stable finalizado.

## Sources and preservation / Fontes e preservação

| Item | Evidence / Evidência |
| --- | --- |
| Execution request / Pedido | [Plano de execução do Atlas para Stable-v1.0.0](https://chatgpt.com/space/page_3a58a158b920819186501003e9d6c132), sequence 1 read during this work / sequência 1 lida neste trabalho |
| Audited source / Origem auditada | `ee8a3292b42c44abe3cd1e8cf0c1e8a176df6a04`, clean `main` matched exactly / `main` limpa e correspondente |
| Local branch / Branch local | `codex/atlas-stable-v1.0.0` |
| Reproduction checkpoint / Checkpoint de reprodução | `d3d485e66590add17cda50b391d657b53aeb127c`: 98 tracked Alpha files copied plus the initial 78 regression cases / 98 arquivos Alpha copiados e 78 casos iniciais |
| Alpha initial manifest / Manifesto inicial Alpha | [alpha-initial.json](evidence/alpha-initial.json); originally captured outside the repository before copying or editing / originalmente capturado fora do repositório antes da cópia ou edição |
| Preservation result / Preservação | [alpha-final.json](evidence/alpha-final.json): all 125 child file/directory records equal, including file bytes/hashes, attributes and Windows ACL SDDL / 125 registros de arquivos/diretórios iguais, incluindo bytes/hashes, atributos e ACL SDDL |
| Inputs tested / Entradas verificadas | [checkpoint-inputs.json](checkpoint-inputs.json): 101 files, byte sizes and SHA-256, captured before this report / 101 arquivos, tamanhos e SHA-256, capturados antes deste relatório |

The initial manifest lives outside the repository at `C:/Users/Douglas/.codex/visualizations/2026/10/26/01a175b9-95a3-7500-b462-6db470cefc5f/atlas-stable-evidence/alpha-initial.json`. A copy is retained above for audit. Only tracked files were copied into the new edition: no virtual environment, cache or temporary directory was inherited. The new local `.venv` is ignored and is excluded from portable distribution tests. The root introductions, assets, citation and edition navigation remain unchanged while finalization is paused.

O manifesto inicial está fora do repositório no caminho acima; sua cópia está preservada para auditoria. Somente arquivos versionados foram copiados: nenhum ambiente virtual, cache ou temporário foi herdado. A nova `.venv` local é ignorada e excluída dos testes de distribuição portátil. Introduções, assets, citação e navegação da raiz permanecem inalterados durante a pausa.

The input manifest excludes this report, itself, evidence outputs, local environments and caches; its complete exclusion list is recorded in JSON. Consequently it has no self-referential hash. The final commit SHA is reported in chat rather than embedded in a file belonging to that commit. No normative source was edited after capture.

O manifesto exclui este relatório, ele próprio, saídas de evidência, ambientes locais e caches; a lista completa consta no JSON. Não há hash autorreferente. O SHA do commit final é entregue no chat, fora dos arquivos do próprio commit. Nenhuma fonte normativa foi editada após a captura.

## Corrections and regression evidence / Correções e regressões

| Defect / Defeito | Change and acceptance evidence / Alteração e evidência de aceite |
| --- | --- |
| A — Optional entity records / Registros opcionais de entidade | Missing `assumptions` or `open_issues`, separately and together, pass CLI validation and six conversion directions without inserting `[]`. `null` remains `ATL-E-SCHEMA`, CLI code 2, without traceback. Presenters were reviewed and required no default insertion. / Ausências passam na CLI e nas seis direções, sem inserir listas; `null` permanece inválido. |
| B — Typed references / Referências tipadas | Figures resolve against the resource catalog at every rich-block depth; source/assumption/issue lists resolve against their own catalogs, without ID-prefix heuristics. Wrong-category and missing references are `ATL-E-REF`. Rejected CLI conversions neither create nor overwrite output. Opaque content is excluded. / Figuras e listas de registros resolvem pelos respectivos catálogos; dados opacos ficam excluídos. |
| C — LaTeX cell endings / Quebras nas células LaTeX | CRLF, CR and LF have distinct reversible source macros, implemented in canonical `atlas.sty`. Tests cover mixtures, final endings, tabs, spaces, Unicode and literal macro-like text. Default verified CLI conversion succeeds. / Macros distintas preservam sequências mistas e texto literal; CLI com verificação passa. |
| D — Opaque Unicode separators / Separadores Unicode opacos | Writer comments only JSON layout LF lines; reader splits only physical CR/LF/CRLF lines. U+0085/U+2028/U+2029 survive in `extensions`, `meta`, example `data` and prose, including literal `text`, `@text`, `id` and reference-like keys. / Escritor e leitor preservam separadores Unicode em conteúdo opaco e prosa. |
| Additional boundary case / Caso adicional de borda | A final authored CR could merge with the structural LF in both Markdown records and LaTeX environments. The encoder now follows that CR with structural CRLF. Four additional public roundtrip tests cover paragraph, heading, list and code. / CR autoral final agora é seguido de CRLF estrutural, com regressões em quatro tipos de texto. |

The [reference inventory](reference-inventory.md) covers all schema-declared ID-reference fields. Generic trace/acceptance/RNF links remain generic; boundary mapping labels, prose and opaque dictionaries are not interpreted as model references. The implementation enforces existing reference validity rather than adding a new business restriction. The new LaTeX spellings will become part of the forthcoming Stable profile, which still requires explicit identity migration.

O [inventário](reference-inventory.md) cobre todos os campos de referência por ID do schema. Vínculos genéricos continuam genéricos; rótulos de mapeamento, prosa e dicionários opacos não são referências do modelo. A implementação aplica a validade já exigida, sem criar uma nova restrição de negócio. Os novos escapes integrarão o futuro perfil Stable, cuja migração explícita de identidade está pendente.

## Executed verification / Verificação executada

Environment: Python **3.12.14**, Windows, isolated edition `.venv`, editable package installed with test and asset extras. Actual versions are in [environment.json](evidence/environment.json), including pytest **9.1.1**, jsonschema **4.26.0**, setuptools **84.2.1** and wheel **0.48.0**. Python 3.11 was not executed in this checkpoint.

Ambiente: Python **3.12.14**, Windows, `.venv` isolada da edição, pacote editável com extras de testes e assets. Versões reais no [registro do ambiente](evidence/environment.json). Python 3.11 não foi executado neste checkpoint.

| Command from edition / Comando na edição | Observed result / Resultado observado |
| --- | --- |
| `python -m pytest tests/test_stable_regressions.py --tb=short -q` before runtime changes / antes das correções | **50 failed, 28 passed** in 37.05s; [captured log](evidence/regressions-before.txt). All four defects reproduced under the original identifiers. / Quatro defeitos reproduzidos sob as identidades originais. |
| `python skills/build.py` after canonical edits / após alterações canônicas | **25 generated files**, also synchronizing packaged schema/style / 25 arquivos gerados e schema/estilo empacotados sincronizados |
| `python -m pytest tests --tb=short -q` after fixes / após correções | **198 passed** in 214.21s; [captured log](evidence/tests-after.txt). Includes original 116 plus 82 new cases, wheel/editable installation, independent edition/skill copies, resources and all six directions. / Inclui instalação, portabilidade, recursos e seis direções. |
| `python examples/build.py --check` | **24 directed conversions**, four document sets and task-board matrix verified / 24 conversões, quatro conjuntos documentais e matriz conferidos |
| `python skills/build.py --check` | **25 generated files verified**, no drift / 25 arquivos verificados, sem divergência |
| `git diff --check` | Passed / passou |
| Local Markdown file-link target scan / inspeção de destinos de links Markdown locais | **700 existing targets**, including historical and working-edition documentation; fragment anchors were not part of this scan / 700 destinos existentes, sem validar fragmentos de âncora |
| `python verification/capture_inputs.py --check` | **101 input files verified** against captured bytes / 101 arquivos conferidos contra os bytes capturados |
| Initial vs final Alpha manifest / comparação dos manifestos Alpha | **125 equal records**, no differences / 125 registros iguais, sem diferenças |

Logs for the pre-fix suite and full post-fix suite were captured from the processes, not reconstructed from intended behavior. The 24-conversion and 25-file results were observed in terminal output. Existing Alpha examples already passed the audited conversions; those passes alone do not exercise the newly corrected cases.

Evidence-local Git attributes retain captured log/manifest bytes; pytest's intentional trailing whitespace in raw logs is exempt from code whitespace checks.

Os logs das regressões anteriores e da suíte posterior foram capturados dos processos. Os resultados de 24 conversões e 25 arquivos foram observados no terminal. Os exemplos Alpha já passavam na auditoria; isso isoladamente não cobre os novos casos corrigidos.

Atributos Git locais às evidências preservam os bytes capturados; espaços finais intencionais dos logs brutos de pytest ficam fora da verificação de espaços do código.

### LaTeX smoke publication / Publicação LaTeX de verificação

A temporary starter copy containing a table with CRLF, CR, LF, mixed/final endings, tabs, Portuguese accents and literal macro names was generated through `AdapterRegistry.convert_file` with exact decoding comparison. **MiKTeX-pdfTeX 4.23 (MiKTeX 25.12)** compiled it in two successful passes with shell escape disabled. Missing declared style dependencies and the transitive `pdfcol` dependency were installed. See [engine identification](evidence/tex-engine.txt) and [second-pass output](evidence/latex-second-pass.txt).

Uma cópia temporária do starter com essas sequências foi gerada pelo conversor e comparada após decodificação. **MiKTeX-pdfTeX 4.23 (MiKTeX 25.12)** compilou duas passagens com shell escape desativado. Foram instaladas dependências faltantes do estilo e a dependência transitiva `pdfcol`. A identificação e o log estão nos links acima.

All three rendered pages were visually inspected at 90 dpi: cover, headers, table cells, literal macros and appendix had no observed clipping, overlap or missing glyphs. This is manual inspection, not an automated layout test. No XeLaTeX/LuaLaTeX coverage is claimed. The smoke artifact remains outside the repository under the initial manifest's directory, in `latex-regression/`. It retains Alpha identifiers and is **not** a Stable example publication. The three copied example PDFs have not been rebuilt as Stable and cannot support Stable release approval.

As três páginas renderizadas foram inspecionadas visualmente a 90 dpi: sem cortes, sobreposição ou glifos ausentes observados na capa, cabeçalhos, tabela, macros literais e apêndice. Trata-se de inspeção manual. Não há alegação de cobertura XeLaTeX/LuaLaTeX. A amostra externa em `latex-regression/` mantém identificadores Alpha e **não** é publicação Stable. Os três PDFs copiados dos exemplos ainda não foram recompilados como Stable e não sustentam aprovação de release.

## OAL dependency and remaining work / Dependência OAL e trabalho pendente

The local OAL checkout inspected was clean at `5755a4e4a5b31a9614da5d409d03d1db9cf1e20c`, containing only Alpha directories. The user confirmed that OAL is still being modified and instructed a pause when its content is needed. No OAL Stable commit, manual path or byte hash has been asserted. The inherited manual's mapping to OAL Alpha remains historical context only. Final OAL correspondence, semantic approval and Stable release approval are pending.

O checkout OAL inspecionado estava limpo em `5755a4e4a5b31a9614da5d409d03d1db9cf1e20c`, somente com diretórios Alpha. O usuário confirmou que o OAL está em modificação e pediu a pausa. Nenhum commit, caminho de manual ou hash de OAL Stable foi inventado. O mapeamento Alpha herdado é apenas contexto histórico. Correspondência OAL final, aprovação semântica e aprovação da release Stable estão pendentes.

| Historical item / Item histórico | Real evidence now / Evidência atual | Remaining review or deliverable / Pendência |
| --- | --- | --- |
| S01-D01 | Copied source inventory and byte manifest; existing file map and synthetic `needs.md` retained / inventário, manifesto e fontes sintéticas preservadas | Final Stable scope/material acceptance inventory after OAL review / inventário final após revisão OAL |
| S01-D02 | Stable IDs and rejected references exercised mechanically / IDs e recusa de referências testados | Two valid Stable document-revision snapshots, explicit delta, current JSON equality and dedicated test / dois snapshots Stable e teste de delta |
| S01-D03 | Existing task-board create/complete/list contracts preserved and mechanically valid / contratos preservados e válidos mecanicamente | Semantic review against finalized OAL; no business application is requested / revisão semântica, sem aplicação executável |
| S01-D04 | Existing canonical entity rules and known/unknown write outcomes retained / regras canônicas e efeitos conhecidos/desconhecidos preservados | Final semantic consistency review / revisão semântica final |
| S01-D05 | Existing RNF scopes, origins, criteria and didactic status retained / RNFs preservados | Final RNF trace/ownership review; no invented SLA / revisão final, sem inventar SLA |
| S01-D06 | JSON/text examples agree, 24 conversions; corrected escapes compiled in smoke artifact / equivalência e amostra compilada | Explicit Alpha-to-Stable editorial migration, regenerated examples and three Stable PDFs visually checked / migração editorial e três PDFs Stable revisados |
| S01-D07 | 198 passing tests, reference inventory, hashes and captured logs / testes, inventário e evidências | OAL baseline and clause review, 3.11 verification/CI, versioned compatibility policy, release notes, root EN/PT/assets/navigation/citation updates / fechamento normativo e editorial |

After receiving finalized OAL content: pin its full commit, normative manual path and SHA-256; review each applicable clause; finalize Stable model/profile/schema/API/CLI/diagnostic policy; record the examples' editorial migration and revisions; synchronize the skill **before** generating examples/matrix/PDFs; execute release checks and update manifests before writing the final report. The proposed edition identity remains `Stable-v1.0.0`, with package and new-document producer `1.0.0`. A tag/release proposal is deferred until all criteria pass.

Após receber OAL finalizado: fixar commit completo, caminho normativo e SHA-256; revisar cláusulas; finalizar contrato Stable, compatibilidade e diagnósticos; registrar migração editorial e revisões; sincronizar a skill **antes** dos exemplos/matriz/PDFs; executar verificações e atualizar manifestos antes do relatório final. A identidade prevista continua `Stable-v1.0.0`, pacote/produtor `1.0.0`. Proposta de tag/release fica para quando os critérios forem satisfeitos.

## Reproduce this checkpoint / Reproduzir este checkpoint

Run with Python 3.11+ from this edition; only 3.12.14 was actually exercised here. On Windows, activate the `.venv` first so `python` resolves to its interpreter. If sandbox temporary storage is unavailable, set `TEMP` and `TMP` to an existing writable temporary directory outside the portable source copy.

Execute na edição com Python 3.11+; nesta execução foi usado apenas 3.12.14. No Windows, ative `.venv` antes. Se o temporário do sandbox não for acessível, configure `TEMP`/`TMP` para um diretório temporário gravável fora da cópia portátil.

```bash
python -m venv .venv
python -m pip install -e ".[test]"
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
python verification/capture_inputs.py --check
```

To reproduce the red regressions, use a separate checkout of the reproduction commit above, install its package and run `tests/test_stable_regressions.py`. Do not reset this branch or edit the historical Alpha tree. This checkpoint was committed locally only; no push, remote tag, release publication or Todoist mutation was performed.

Para reproduzir as regressões vermelhas, use checkout separado do commit de reprodução, instale o pacote e execute aquele arquivo de testes. Não resete esta branch nem edite a Alpha histórica. Este checkpoint foi commitado apenas localmente; não houve push, tag remota, publicação ou alteração no Todoist.
