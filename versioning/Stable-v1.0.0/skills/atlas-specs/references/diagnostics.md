> Canonical English source: `DIAGNOSTICS.md`. This snapshot relocates links for standalone use. Follow SKILL.md for commands inside this bundle.

# Diagnostic codes / Códigos de diagnóstico

[Compatibility policy / Política](compatibility.md) · CLI (edition source: `translator/README.md`)

Codes below are the Stable public categories. Messages supply the specific violation and location; they are not stable machine-readable text. / Os códigos abaixo são categorias públicas Stable. Mensagens identificam a violação e localização, sem estabilidade textual para máquinas.

| Codes / Códigos | Meaning / Significado |
| --- | --- |
| `ATL-E-GENERAL` | General diagnosed Atlas operation failure / Falha geral diagnosticada da operação Atlas. |
| `ATL-E-ADAPTER`, `ATL-E-VERSION` | Unknown adapter or unsupported model/representation version / Adaptador desconhecido ou versão de modelo/representação não suportada. |
| `ATL-E-PROFILE-VERSION`, `ATL-E-FORMAT` | Unsupported payload profile or incompatible envelope / Perfil do payload não suportado ou envelope incompatível. |
| `ATL-E-UTF8`, `ATL-E-BOM` | Invalid UTF-8 or forbidden BOM / UTF-8 inválido ou BOM proibido. |
| `ATL-E-JSON`, `ATL-E-DUPLICATE-KEY`, `ATL-E-FLOAT` | Invalid JSON, duplicate key, or forbidden floating/nonfinite number / JSON inválido, chave duplicada ou número fracionário/não finito proibido. |
| `ATL-E-SCHEMA`, `ATL-E-ID`, `ATL-E-DUPLICATE-ID` | Schema or identity violation / Violação de schema ou identidade. |
| `ATL-E-REF` | Missing reference or wrong referenced category / Referência inexistente ou categoria incorreta. |
| `ATL-E-MARKDOWN`, `ATL-E-MARKDOWN-HEADER`, `ATL-E-LATEX`, `ATL-E-LATEX-HEADER` | Invalid controlled-profile syntax/header / Sintaxe/header inválido no perfil controlado. |
| `ATL-E-BLOCK`, `ATL-E-TEXT-TYPE` | Unsupported rich block or invalid text-record type / Bloco rico não suportado ou tipo de registro textual inválido. |
| `ATL-E-STRUCTURE-MISSING`, `ATL-E-STRUCTURE-DUPLICATE`, `ATL-E-PRESENTATION-DUPLICATE` | Missing/duplicate structural appendix or duplicate presentation region / Apêndice estrutural ausente/duplicado ou região de apresentação duplicada. |
| `ATL-E-SLOT`, `ATL-E-SLOT-DUPLICATE`, `ATL-E-SLOT-MISSING`, `ATL-E-SLOT-ORPHAN` | Invalid slot, duplicate/missing record, or unused authoritative text / Slot inválido, registro duplicado/ausente ou texto autoral sem uso. |
| `ATL-E-DERIVED-STALE`, `ATL-E-DERIVED-UNKNOWN` | Stale or unknown derived region / Região derivada desatualizada ou desconhecida. |
| `ATL-E-TIKZ-MISSING`, `ATL-E-TIKZ-STALE`, `ATL-E-TIKZ-UNKNOWN` | Missing, stale or unknown generated graph / Grafo gerado ausente, desatualizado ou desconhecido. |
| `ATL-E-DUPLICATE-NODE`, `ATL-E-GRAPH-EDGE`, `ATL-E-GRAPH-OWNER`, `ATL-E-GRAPH-CALL` | Duplicate graph node, invalid edge endpoints, ownership or call / Nó duplicado, extremidade de aresta, propriedade ou chamada inválida. |
| `ATL-E-SELF-CALL` | Forbidden direct self-call / Chamada direta a si mesmo proibida. |
| `ATL-E-RF-FLOW`, `ATL-E-RF-GRAPH` | Invalid or nonreciprocal RF/flow links / Vínculos RF/fluxo inválidos ou não recíprocos. |
| `ATL-E-BOUNDARY-RF` | Invalid boundary-to-requirement relationship / Relação inválida entre fronteira e requisito. |
| `ATL-E-RNF`, `ATL-E-RNF-CHAIN`, `ATL-E-RNF-LOCAL` | Invalid RNF references, reference chain or local scope / Referência de RNF, cadeia de referências ou escopo local inválido. |
| `ATL-E-RESOURCE-PATH`, `ATL-E-RESOURCE-MISSING`, `ATL-E-RESOURCE-SIZE`, `ATL-E-RESOURCE-HASH` | Unsafe/missing resource or size/hash mismatch / Caminho inseguro, recurso ausente ou tamanho/hash divergente. |
| `ATL-E-RESOURCE-TEXT`, `ATL-E-FIGURE-STALE`, `ATL-E-VARIANT` | Missing textual recovery, stale graph figure or invalid resource variant / Recuperação textual ausente, figura de grafo desatualizada ou variante inválida. |
| `ATL-E-LATEX-RESOURCE` | No usable LaTeX resource or variant / Recurso ou variante sem suporte na publicação LaTeX. |

One input can violate several rules. Fix the diagnosed source and revalidate; a code is not permission to discard unsupported content. / Uma entrada pode violar várias regras. Corrija a origem e revalide; um código não autoriza descartar conteúdo não suportado.
