# Tradutor Atlas 0.1.0

[English](README.md) · [Português (Brasil)](README.pt-br.md)

Implementação em Python 3.11+ dos perfis **Atlas JSON**, **Atlas Markdown** e **Atlas LaTeX** para Atlas Specifications `Alpha-v0.1.0`. Traduz representações do mesmo conteúdo Atlas; não deriva artefatos L2 do OAL, não migra versões da especificação e não importa Markdown/LaTeX arbitrários.

## Instalação e uso

Execute todos os comandos no **diretório da edição**, que contém `pyproject.toml`. Crie e ative um ambiente virtual Python primeiro:

```bash
python -m pip install .
python translator/atlas_translate.py formats
python translator/atlas_translate.py validate examples/task-board/example.atlas.json
python translator/atlas_translate.py convert examples/task-board/example.atlas.json --from json --to markdown -o work/task-board.atlas.md
python translator/atlas_translate.py convert work/task-board.atlas.md --from markdown --to latex -o work/task-board.atlas.tex
```

O comando instalado `atlas-spec` oferece a mesma interface que o [lançador Python](atlas_translate.py). O lançador seleciona somente o runtime que está ao seu lado, portanto copiar a edição preserva seu comportamento. A [skill para IA](../skills/atlas-specs/SKILL.md) autossuficiente inclui um lançador idêntico e uma cópia gerada do mesmo runtime.

## Contrato de tradução

As quatro operações primitivas são Markdown → JSON, JSON → Markdown, LaTeX → JSON e JSON → LaTeX. Markdown ↔ LaTeX é composto por meio do Atlas JSON validado, totalizando seis direções. Não é necessário criar um arquivo intermediário em disco.

Cada conversão padrão da CLI e `AdapterRegistry.convert_file` valida a origem, codifica o destino, decodifica esse resultado novamente e compara o conteúdo completo de `atlas` antes de escrever. A comparação ignora os metadados externos de transporte (`format`, `$schema`) e a ordem das propriedades dos objetos, preservando a ordem das listas, os tipos escalares, as diferenças entre ausente/nulo/vazio e o texto autoral exato. Alterações de conteúdo provocam falha em vez de sucesso aparente.

A opção `--no-verify` ignora explicitamente a comparação final e informa essa limitação. `--no-check-resources` ignora a verificação dos bytes dos recursos e não demonstra sua preservação. Nenhuma dessas opções é necessária para os exemplos fornecidos.

A conversão não reescreve recursos. Mantenha o destino no mesmo pacote ou use `--resources CAMINHO` para indicar a raiz compartilhada dos recursos. Para publicar uma pasta autocontida:

```bash
python translator/atlas_translate.py package examples/minimal/example.atlas.json --from json -o work/request-package
python translator/atlas_translate.py convert work/request-package/example.atlas.json --from json --to latex -o work/request-package/example.atlas.tex
```

A pasta inclui a instância de origem, os recursos locais e `atlas.sty`. PDF é uma visualização compilada do Atlas LaTeX, não um quarto perfil de intercâmbio. Reconstrua os PDFs fornecidos com `python examples/build.py --pdf`; a conversão JSON/Markdown/LaTeX não exige instalação de TeX. O [guia LaTeX](../implementations/latex/README.pt-br.md) explica a publicação de outros documentos.

## API Python

```python
from pathlib import Path
from atlas_spec import AdapterRegistry, atlas_content_equal

registry = AdapterRegistry()
source = Path("examples/task-board/example.atlas.json")
document = registry.decode_to_atlas_json(source, source_format="json")
markdown = registry.encode_from_atlas_json(document, target_format="markdown")
recovered = registry.decode_to_atlas_json(markdown, source_format="markdown")
assert atlas_content_equal(document, recovered)
```

`encode_from_atlas_json` e `decode_to_atlas_json` são operações de baixo nível separadas. Use `convert_file` para a conversão combinada com a verificação após a codificação. O pacote também exporta `Adapter`, `DecodeOptions`, `EncodeOptions`, `JsonAdapter`, `MarkdownAdapter`, `LatexAdapter`, `Validator`, `validate_document` e classes de diagnóstico derivadas de `AtlasError`. `Validator` verifica as regras estruturais/referenciais publicadas e os recursos locais. Não prova a veracidade do texto de um projeto nem todas as obrigações semânticas do OAL; essa análise é separada.

## Verificação

No diretório da edição:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python skills/build.py --check
```

Os testes exercitam ciclos de conversão, preservação exata de Unicode/quebras de linha, diagnósticos, recursos, metadados externos de transporte, igualdade que distingue tipos, vínculos recíprocos RF/fluxo, instalação do pacote, equivalência dos modelos iniciais e execução de cópias isoladas da edição e da skill. O teste de instalação usa um ambiente virtual temporário sem resolução pela rede e reutiliza o caminho das dependências do ambiente de teste; falhas de instalação ou execução reprovam o teste.

As cópias do schema e do estilo no pacote precisam ser iguais aos arquivos publicados em `implementations/`. `skills/build.py` atualiza as cópias de distribuição; `--check` aponta diferenças sem alterá-las. O [manual da edição](../README.pt-br.md) define o contrato de preservação, o processo de tradução e o escopo de conformidade.

**Autor:** Douglas de Oliveira Alkimim. [Licença MIT](../LICENSE).
