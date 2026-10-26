# Clean distribution / Distribuição limpa

Create the release archive from a committed repository. The helper refuses
uncommitted tracked changes and tracked caches/intermediates, then archives only
the committed files. Deliberately distributed examples, PDFs, resources, source
artwork and evidence remain included. Untracked local environments never enter
the archive. It prints the actual ZIP's SHA-256; keep that receipt outside the
commit to avoid a circular identity.

Crie o pacote a partir do repositório com alterações commitadas. O helper recusa
mudanças versionadas pendentes e temporários versionados, preservando exemplos,
PDFs, recursos, fontes e evidências intencionais. O recibo com SHA-256 do ZIP deve
ficar fora do commit. Não são criados tag, release ou push.

From the Stable edition / A partir da edição Stable:

```bash
python verification/capture_release.py --check
python verification/build_distribution.py --output /absolute/path/Atlas_Stable.zip
```

Extract the actual archive to a new directory and check it before generating
anything. The extracted `Atlas_Stable/` folder contains the complete repository
distribution, including preserved Alpha; it does not contain `.git`. Run
`verification/capture_release.py --check` from its Stable edition. The checker
uses relative POSIX paths as identities and compares bytes/sizes/hashes by path,
independent of Windows/POSIX sort order. Duplicate paths are invalid.

Extraia o ZIP efetivo em uma pasta nova e confira o manifesto antes de regenerar.
A pasta `Atlas_Stable/` inclui a distribuição completa e a Alpha preservada, sem
exigir Git. Caminhos POSIX relativos identificam registros; ordem de enumeração
não altera a comparação. Duplicatas e diferenças reais são rejeitadas.

Install Python 3.11+ in a fresh environment **outside** the extracted folder,
activate it, and install the edition with `python -m pip install -e ".[test,assets]"`.
Then run the following from the extracted Stable edition. The full tests include
wheel/editable installation and the standalone skill. PDF publication also
requires pdfLaTeX and the packages documented in the LaTeX guide.

Instale Python 3.11+ em ambiente novo **fora** da pasta extraída, ative-o e instale
as dependências da edição. Execute na ordem abaixo; os testes incluem instalação
da edição e da skill portátil. A publicação requer os pacotes LaTeX documentados.

```bash
python skills/build.py
python examples/build.py --pdf
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

PDF regeneration can change timestamps and bytes. Verify the delivered manifest
before regeneration; capture a new inventory only for a deliberately rebuilt
candidate. Do not replace historical checkpoint manifests to describe new bytes.
Inspect the ZIP's entries and extracted files for environments, caches, pytest
temporary files and TeX intermediates; reviewing `.gitignore` alone is insufficient.

A regeneração de PDFs pode alterar bytes e timestamps. Confira o manifesto
entregue antes de regenerar; capture outro inventário para uma nova candidata,
preservando os checkpoints. Inspecione o ZIP e a extração, além do `.gitignore`.
