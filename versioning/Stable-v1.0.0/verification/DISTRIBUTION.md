# Distribution / Distribuição

The repository-wide procedure is maintained in [English](../../../docs/releasing.md) and [Portuguese](../../../docs/releasing.pt-br.md). Root `CONTENT-SHA256.json` is the only active distribution inventory; it covers all editions and every indexed delivery file except itself. There is no active per-edition `release-inputs.json`.

O procedimento do repositório está nos guias acima. O inventário único da raiz cobre todas as edições e arquivos indexados da entrega, exceto a si mesmo. Checkpoints anteriores permanecem como evidência histórica, com seus escopos originais.

From the repository root / Na raiz do repositório:

```bash
python scripts/content_inventory.py --check
python scripts/build_distribution.py --output /absolute/path/Atlas-Stable-v1.0.0.zip
python scripts/check_archive.py /absolute/path/Atlas-Stable-v1.0.0.zip
```

After extraction, use the copied `scripts/check_archive.py` against the extracted repository root before installation or regeneration; no Git is needed. A copied edition alone retains its own translator, dependencies, examples, tests and portable skill, while full-distribution integrity is a repository-level check. See the [edition verification guide](../README.md#verification) and [examples guide](../examples/README.md) for its installation, conversions and PDF publication.

Após extrair, confira a raiz extraída com o `scripts/check_archive.py` copiado, antes de instalar ou regenerar; Git não é necessário. A edição isolada mantém tradutor, dependências, exemplos, testes e skill próprios; a integridade da distribuição completa é conferida na raiz. Regenerar PDFs pode alterar seus bytes; mantenha ambientes e temporários fora do pacote.
