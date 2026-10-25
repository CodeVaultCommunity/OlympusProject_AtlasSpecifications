# Composição de reservas

[English](README.md) · [Exemplos](../README.pt-br.md)

Especificação sintética com três casos que demonstra reutilização preservando o contrato chamado: cancelar invoca localizar com o mesmo contexto confiável e também precisa satisfazer sua autorização. Cada caso recusa contexto ausente, não resolvido ou insuficiente antes de chamar colaboradores.

| Caso | Obrigação principal | Elementos compartilhados |
| --- | --- | --- |
| `UC-BOOKING-LOOKUP` | Validar código, carregar Booking pronta e distinguir ausência confirmada de falha. | `ENT-BOOKING`, `VLD-BOOKING-CODE`, `OP-BOOKING-LOAD` |
| `UC-BOOKING-CREATE` | Validar código e título, criar Booking ativa e inserir atomicamente com versão esperada zero. | `ENT-BOOKING`, `VLD-BOOKING-CODE`, `VLD-BOOKING-TITLE`, `OP-BOOKING-SAVE` |
| `UC-BOOKING-CANCEL` | Preservar resultados da localização, aplicar transição canônica e salvar condicionalmente com a revisão observada. | `UC-BOOKING-LOOKUP`, `VLD-BOOKING-CANCEL`, `OP-BOOKING-SAVE` |

Consulte [JSON](example.atlas.json), [Markdown](example.atlas.md), [LaTeX](example.atlas.tex) ou [PDF](example.atlas.pdf) derivado. A fronteira de linha de comando é uma proposta ilustrativa, não uma escolha obrigatória de L1.

`BOOK001` é o identificador válido: a regra canônica admite somente letras maiúsculas e dígitos, entre 1 e 12 caracteres. Um valor como `BOOK-001` viola essa regra. Exemplos com minúsculas e pontuação permanecem explicitamente inválidos.

`SRC-BOOKING-BRIEF`, revisão 2, registra a origem sintética. A condição compartilhada de dois segundos e o cenário de 30 solicitações demonstram definição canônica e referência; são hipóteses ilustrativas, não SLA aprovado ou medição executada.

O contrato compartilhado de salvar distingue versão zero (inserir se ausente) de versão positiva observada (substituir condicionalmente). Um conflito garante que esta chamada não alterou o registro; outra chamada pode tê-lo alterado. Perda de confirmação preserva `unknown`, sem repetição automática.

## Autoria

Douglas de Oliveira Alkimim.
