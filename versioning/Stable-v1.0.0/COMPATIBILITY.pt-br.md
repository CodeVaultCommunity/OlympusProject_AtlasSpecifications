# Superfície estável e compatibilidade

[English](COMPATIBILITY.md) · [Manual normativo](README.md#versioning)

O inglês é normativo. Stable identifica um contrato, não publicação ou aprovação de stakeholders.

| Identidade / operação | Contrato |
| --- | --- |
| Modelo / perfil | Ambos exatamente `Stable-v1.0.0`. |
| Declaração de representação | `atlas-json/Stable-v1.0.0`; headers Markdown/LaTeX declaram `representation=Stable-v1.0.0`. |
| Implementação / novo produtor | Pacote `atlas-spec` e produtor de novos documentos: `1.0.0`. |
| Produtor existente / revisão / histórico | Dados autorais, preservados exatamente na conversão mesmo quando o produtor difere do pacote em execução. |
| Entrada Stable → representação Stable | Seis direções suportadas, conforme o contrato de preservação/recursos. |
| Entrada Alpha → runtime Stable | Rejeitada com diagnóstico explícito de versão. Use a edição Alpha preservada e seu runtime para documentos Alpha. |
| Conteúdo Alpha → Stable | Migração editorial separada com origem, destino, pessoa responsável, mudanças intencionais e revisão. Não há migrador genérico. |
| Outro modelo/perfil ou versão futura | Não suportado sem implementação e documentação explícitas. Não se promete interoperabilidade com outra major. |
| PDF | Somente publicação; sem importação reversa ou alegação de igualdade de payload. |

## Superfície pública estável

O [manual](README.md#abstract-model), as três [gramáticas](README.pt-br.md#implementations), o JSON Schema e as macros LaTeX canônicas definem obrigações de modelo e representação, incluindo texto exato, distinção ausente/null/vazio, dados opacos e preservação de recursos.

São públicos os comandos `formats`, `validate`, `convert` e `package`, seus argumentos/opções documentados e significados dos códigos de saída. Veja o [guia CLI](translator/README.pt-br.md). Sucesso retorna 0; erros Atlas diagnosticados e uso inválido retornam 2. Mensagens legíveis e progresso não são protocolos de máquina.

As exportações Python públicas são `ALL_FORMATS`, `FUNDAMENTAL`, `SUPPORTED_PROFILE_VERSION`, `SUPPORTED_SPEC_VERSION`, `Adapter`, `AdapterRegistry`, `AtlasError`, `AtlasParseError`, `AtlasValidationError`, `AtlasVersionError`, `DecodeOptions`, `Diagnostic`, `EncodeOptions`, `JsonAdapter`, `LatexAdapter`, `MarkdownAdapter`, `Validator`, `default_registry`, `validate_document` e `atlas_content_equal`, além de `__version__`. Suas assinaturas, opções e comportamento documentados constituem o contrato API. Auxiliares privados e organização interna não são contratos de extensão. O [catálogo de diagnósticos](DIAGNOSTICS.md) identifica códigos estáveis e significados; ordem e localização precisa podem melhorar sem alterar o significado.

## Política de evolução

Semântica incompatível, mudanças na linguagem que rejeitem conteúdo anteriormente válido, remoção de comandos/opções/APIs, assinaturas incompatíveis ou mudança de significado de códigos exigem versão major e política explícita de migração. Novas restrições semânticas obrigatórias são incompatíveis, mesmo quando implementadas no validador.

Adições opcionais compatíveis exigem minor e capacidade/perfil declarado quando afetam representações. Um runtime antigo não precisa reconhecer um novo perfil selecionado. Patches corrigem implementações sem mudar o contrato. Rejeitar referência já inválida pelas regras publicadas é correção; inventar restrição de domínio não é. As novas grafias reversíveis desta edição pertencem ao novo perfil Stable e não são acrescentadas retroativamente à Alpha.

Versões do pacote descrevem a implementação. Identidades de modelo/perfil selecionam contratos independentemente; atualizações não devem relabelar payloads. A revisão documental registra mudanças autorais, não execuções do codec. Versões históricas continuam acessíveis em seus diretórios.

Starter e três exemplos registram a migração explícita Alpha revisão 1 → Stable revisão 2 em `HIST-MIGRATION-STABLE`. O [registro](verification/editorial-migration.json) preserva hashes e responsabilidade; a [demonstração do quadro](examples/task-board/revisions/README.md) é uma mudança separada da revisão 2 para 3.

Antes do aceite formal da migração, identifique a pessoa responsável; solicitante ou ferramenta não equivalem automaticamente a essa pessoa. A candidata sem confirmação registra `responsibility_status: pending_confirmation`, `responsible_person: null` e ausência de aprovação humana. A evolução visual aceita a forma TikZ Stable original e a forma compacta atual, ambas regeneradas exatamente do grafo; alterações arbitrárias continuam rejeitadas.
