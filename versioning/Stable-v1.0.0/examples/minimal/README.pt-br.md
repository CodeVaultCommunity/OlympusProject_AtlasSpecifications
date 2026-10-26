# Registro de solicitações

[English](README.md) · [Exemplos](../README.pt-br.md)

Especificação sintética menor, centrada em `UC-REQUEST-SUBMIT`: resolver autorização, validar código e quantidade e solicitar uma escrita atômica. Distingue dados inválidos, falta de autorização, duplicidade e incerteza de armazenamento da confirmação.

- [Atlas JSON](example.atlas.json) é a base gerada e o intermediário do tradutor.
- [Atlas Markdown](example.atlas.md) e [Atlas LaTeX](example.atlas.tex) preservam o mesmo conteúdo.
- [PDF](example.atlas.pdf) é uma publicação derivada; seus grafos partem dos registros estruturados.
- [Wireframe do formulário](assets/request-form.svg) é uma ilustração de canal, fora da alegação de L1.
- [Fluxo de envio](assets/request-flow.svg) inclui todos os nós e arestas, com chave estável das arestas.

A fonte `SRC-REQUEST-BRIEF`, revisão 2, é sintética. A meta de dois segundos e o cenário de 30 solicitações são hipóteses didáticas que exigem evidência real das partes interessadas e do ambiente antes da adoção; `OI-REQUEST-LATENCY` mantém essa questão visível. A autorização é semântica, com recusa por padrão; a implementação da autenticação fica fora deste exemplo.

O exemplo declara os caminhos de validade do código e duplicidade, a origem do conteúdo, o contexto confiável do chamador e os resultados explícitos de escrita.

O catálogo de recursos preserva o nome do gerador original dos desenhos como proveniência. As fontes SVG editáveis e suas variantes PNG originais estão em `assets/`; `examples/build.py` reutiliza e verifica esses arquivos ao reconstruir as representações do documento.

## Autoria

Douglas de Oliveira Alkimim.
