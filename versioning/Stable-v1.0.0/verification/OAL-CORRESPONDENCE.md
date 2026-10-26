# OAL Stable correspondence review / Revisão da correspondência

Document-level clause comparison, separate from stakeholder approval and application execution. / Comparação documental por cláusula, distinta da aprovação de stakeholders e da execução da aplicação.

## Exact input / Entrada exata

The [baseline record](oal/baseline.json) identifies local commit `bdea8a4269e2788f25b68d2925c125d7e62c04ed`, a verified canonical archive and accessible local Git tree and byte-exact EN/PT snapshots. Normative source: `versioning/Stable-v1.0.0/README.md`; SHA-256 `70f6f8d8d4fcb626e3d4ee84259919bc5c62e149a6d6dc4a2af81ef7ff806f84`. The [English snapshot](oal/README.md.txt) is the authority; [Portuguese](oal/README.pt-br.md.txt) is the translation. Original license is retained. Remote availability of this commit was not asserted or required.

O registro identifica commit local, checkout limpo e snapshots exatos EN/PT. O snapshot inglês é normativo e o português é tradução; a licença original foi preservada. Não se afirma disponibilidade pública do commit.

The final reference update on 2026-10-26 compares the canonical archive with the
Git blobs of `bdea8a4269e2788f25b68d2925c125d7e62c04ed` (tree
`5baee0a40771711981397ff332532d4d54e798fe`). Both match exactly. Relative to
`a02bf8eecf222e7e0a7a34977fff49a25b5af6aa`, only the manuals' introductory
editorial/operational notices changed. The complete normative bodies beginning
at `oal-layers`, including all 46 numbered rules in each language, remain
byte-identical. The ten UCS and nine cross-layer assessments below therefore
retain the same obligations and were reconfirmed against the current Atlas
manual. The source update does not turn launcher changes into normative changes.

A atualização final compara os bytes do ZIP canônico com os blobs do commit
local e registra a igualdade em `oal/baseline.json`. As dez cláusulas UCS e nove
transversais continuam correspondentes. A validade de domínio pode ficar na
entidade ou no caso consumidor; ferramentas que recebem entidade pronta não
repetem sua coerência intrínseca. `SRC-TASK-OAL` permanece a referência Alpha
histórica dos exemplos, sem ser relabelada como origem Stable.

All 46 numbered normative rules in both languages compare exactly with the preserved Alpha-v0.2.0-Alkimim normative blocks. Release/version prose differs. This comparison establishes continuity of those bytes, not Atlas conformance: each of the relevant 19 clauses was also read against Atlas's actual obligations and scope below. The other 27 L2–L4 rules are outside the claim.

As 46 regras numeradas de ambos os idiomas são idênticas às da Alpha preservada; prosa de release/versionamento difere. A igualdade prova continuidade desses bytes, não conformidade Atlas. As 19 cláusulas relevantes também foram revisadas contra obrigações e escopo reais; as outras 27 de L2–L4 estão fora da alegação.

## Clause assessment / Avaliação por cláusula

Detailed normative mappings remain in the [English manual](../README.md#oal-conformance) and [Portuguese translation](../README.pt-br.md#oal-conformance). The following records what was assessed, beyond matching edition names. / Os mapeamentos detalhados ficam nos manuais; abaixo se registra o conteúdo avaliado além dos nomes de edição.

| Clause / Cláusula | Reviewed result and boundary / Resultado revisado e limite |
| --- | --- |
| UCS 1 | Scope/objectives/participants required by §§1–4,14; sections are editorial, not code modules. / Escopo, objetivos e participantes exigidos; seções não são módulos de código. |
| UCS 2 | §10 distinguishes case ID, actor, trusted caller context and permission; denial precedes protected effects. / Distingue ID, ator, contexto confiável e permissão; recusa anterior aos efeitos. |
| UCS 3 | §§9–11 require inputs/results, conditions, guarantees, alternatives/failures; channel choices retain origin and responsibility. / Contratos completos e origem/responsabilidade de canais. |
| UCS 4 | §§7–8 canonical entity validity versus contextual operation checks; no duplicated intrinsic rule ownership. / Validade canônica versus condições contextuais, sem duplicar propriedade. |
| UCS 5 | §§7,9–10 state dependencies and abstract capabilities without selecting persistence/protocol. / Dependências e capacidades abstratas sem escolher persistência/protocolo. |
| UCS 6 | §10.2 requires individual origin, scope, applicability and verifiable criterion; didactic targets are labeled. / Origem, escopo, aplicabilidade e critério por obrigação; metas didáticas identificadas. |
| UCS 7 | §§6,10 link case criteria and shared criteria without duplicating a canonical obligation. Later layers absent. / Critérios por caso e compartilhados sem duplicação; camadas posteriores ausentes. |
| UCS 8 | §§3,5–6,15–17 preserve identity, history and nature/status distinctions. Revision demonstration is actual. / Preservação de identidade, histórico e distinções de natureza/status; demonstração real de revisão. |
| UCS 9 | §14 permits domain organization without inventing a mandatory domain object. / Organização por domínios permitida, sem objeto obrigatório inventado. |
| UCS 10 | §§8,12–13 subordinate examples to rules; fixtures do not substitute for ADVS. / Exemplos subordinados às regras; não substituem ADVS. |
| Cross 1 / Transversal 1 | Model, implementing model, representation, artifact and publication distinguished in §2. / Conceitos distinguidos no §2. |
| Cross 2 / Transversal 2 | §16 requires named accountable person and source/destination baselines when claiming a derivation. Synthetic briefs and editorial migration do not claim that derivation. / Proveniência e responsável exigidos quando há derivação; não alegada aqui. |
| Cross 3 / Transversal 3 | Case IDs retained for downstream mapping; one-to-one ADPM/ADVS/ADI evidence is not fabricated. / IDs preservados; correspondências posteriores não inventadas. |
| Cross 4 / Transversal 4 | Changes require impact records; snapshots identify actual acceptance reference and generated outputs affected. / Mudanças têm impacto; snapshots identificam referência e derivados afetados. |
| Cross 5 / Transversal 5 | Actor, caller, trust authority and accountable human remain distinct; no technology prescribed. / Ator, chamador, autoridade e responsável distintos, sem tecnologia prescrita. |
| Cross 6 / Transversal 6 | Claim names edition, model and L1 scope; validity, semantic review and application evidence are separate. / Alegação identifica edição/modelo/escopo e distingue validade, revisão e aplicação. |
| Cross 7 / Transversal 7 | No derivation engine or transformer construction/execution claimed. / Nenhuma alegação de engine ou construção/execução de transformador. |
| Cross 8 / Transversal 8 | Exact same-model conversion differs from model translation and cross-layer derivation; loss report is not full preservation. / Conversão exata difere de tradução e derivação; relatório de perda não é preservação plena. |
| Cross 9 / Transversal 9 | Co-located illustrations/representations are not evidence of an engine. / Ilustrações e representações reunidas não demonstram engine. |

Result: the Atlas model establishes the relevant OAL Stable L1 responsibilities for its declared scope. No blocking mismatch was identified in this review. This does not approve every Atlas instance, validate stakeholder needs, prove behavior of a future application, or claim complete OAL coverage. Human release review remains distinct.

Resultado: o modelo Atlas estabelece as responsabilidades L1 relevantes do OAL Stable no escopo declarado; a revisão não identificou incompatibilidade bloqueadora. Não aprova toda instância, valida necessidades de stakeholders, prova comportamento de aplicação futura ou alega cobertura OAL completa. A revisão humana da release permanece distinta.
