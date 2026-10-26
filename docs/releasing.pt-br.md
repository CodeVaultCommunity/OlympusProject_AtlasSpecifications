# Preparação de uma release do Atlas

[English](releasing.md) · [Início](../README.pt-br.md) · [Guia dos agentes](../AGENTS.md)

Este procedimento não acrescenta requisitos ao modelo Atlas. Selecione a edição antes de escolher contratos, tradutor, skill e verificações. `CITATION.cff` fornece a identidade de release para o inventário; revisões de documentos e versões do pacote do tradutor mantêm significados independentes. Commit e ZIP verificados localmente não implicam publicação nem aprovação de stakeholders.

## Finalizar fontes e verificar

Confira branch e árvore de trabalho, preservando alterações do usuário e edições históricas. Coordene inglês/português, versões, snapshots OAL e hashes da skill. Confirme a pessoa responsável pela migração editorial separadamente da autoria e da aprovação dos requisitos dos exemplos. Preserve logs e checkpoints anteriores com seu escopo original, sem apresentá-los como execução nova.

Use checkout canônico limpo ou exportação do índice Git e respeite `.gitattributes`, inclusive quebras literais dos documentos Atlas e evidências brutas. Calcule hashes sobre bytes reais, sem normalização durante o cálculo; não reescreva arquivos Alpha congelados nem regenere o inventário para esconder bytes mistos. Mantenha ambientes e temporários fora da entrega.

Na raiz, execute `python -m pytest scripts/tests`. Para Stable-v1.0.0, use Python 3.11+ e execute no diretório da edição:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

Quando fontes canônicas mudarem, execute `python skills/build.py` antes da conferência. Mudanças de publicação também exigem `python examples/build.py --pdf`, dependências LaTeX documentadas e inspeção visual. Alterar ferramentas/guias não exige reconstruir PDFs intactos; preserve a evidência visual anterior e informe o que foi repetido. Reconstruir PDFs pode mudar timestamps e hashes.

## Gerar o inventário único

`CONTENT-SHA256.json` na raiz é o único inventário ativo da distribuição, seguindo o padrão OAL. Registra `algorithm`, `atlas_edition` (correspondente a `CITATION.cff`), escopo, exclusões e entradas com `path` POSIX relativo, `size_bytes` e `sha256`. Cobre todos os arquivos indexados da entrega, inclusive Alpha, PDFs, arte, scripts, relatórios, evidências brutas, checkpoints históricos e `.github/`. Somente o próprio inventário é excluído. A geração ordena caminhos deterministicamente; a conferência compara identidade e conteúdo independentemente da ordem dos registros e rejeita duplicatas.

Finalize fontes e evidências, então adicione ao índice as inclusões, modificações e exclusões pretendidas, com caminhos explícitos. Inclusões não rastreadas não são descobertas automaticamente. Na raiz:

```bash
python scripts/content_inventory.py --write
python scripts/content_inventory.py --check
git add -- CONTENT-SHA256.json
```

O gerador lê caminhos do índice e bytes reais da árvore de trabalho. Confira também a igualdade desses bytes com os blobs preparados no Git antes do commit. Não existe `release-inputs.json` ativo por edição nem contagem fixa de arquivos. Inventários de checkpoints anteriores permanecem como evidência histórica; não os regenere. Registros de execução podem identificar baseline e hashes das fontes alteradas relevantes, excluindo a si mesmos e o inventário final para evitar ciclos. Toda evidência concluída é coberta pelo inventário da raiz. Gere/confira esse inventário por último e faça o commit local da árvore completa.

## Empacotar e inspecionar

Após o commit, execute na raiz:

```bash
python scripts/build_distribution.py --output /absolute/path/Atlas-Stable-v1.0.0.zip
python scripts/check_archive.py /absolute/path/Atlas-Stable-v1.0.0.zip
```

O empacotador recusa conteúdo rastreado pendente, inventário desatualizado, caches/intermediários rastreados e destino existente. Arquiva os arquivos commitados e verifica cobertura completa e bytes exatos. O ZIP contém todas as edições em `Atlas_Stable/`, sem `.git`; o verificador também aceita arquivos diretamente na raiz do ZIP.

Extraia o ZIP efetivo em diretório novo e vazio, então confira a raiz extraída **antes** de instalar ou regenerar qualquer coisa:

```bash
python /path/to/extracted/Atlas_Stable/scripts/check_archive.py /path/to/extracted/Atlas_Stable
```

O verificador de ZIP/diretório usa apenas a biblioteca padrão do Python, sem Git, e rejeita arquivos ausentes, adicionais, duplicados ou alterados. `content_inventory.py` exige um checkout Git. Mantenha um ambiente novo fora da árvore extraída e siga as instruções de instalação/validação da edição. Caches e metadados de instalação contam como arquivos extras em auditoria estrita do pacote.

Mantenha commit final, tamanho e SHA-256 do ZIP, contagem de arquivos, verificações e limites em recibo externo, fora do commit e ZIP que ele identifica. Commit e digest externo do ZIP protegem o próprio inventário.

## Publicação opcional

Somente após autorização explícita, envie o commit e exija CI aprovada para essa revisão nos jobs Windows/Linux e Python suportados, além do job de publicação. Configuração não é evidência de execução. Crie a tag anotada da edição e a release desse commit, anexe ZIP verificado e SHA-256 e confirme as identidades. A entrega apenas local termina no commit, ZIP e recibo verificados; não cria push, tag ou release remota. Snapshots publicados são imutáveis.
