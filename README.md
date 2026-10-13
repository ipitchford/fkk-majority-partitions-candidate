# Strict majority partitions and weighted certificates for normalized Laplacian gaps

**Anonymous · 0.1.0-candidate · 13 October 2026**

Research DOI: [10.5281/zenodo.23336669](https://doi.org/10.5281/zenodo.23336669). Repository: [fkk-majority-partitions-candidate](https://github.com/ipitchford/fkk-majority-partitions-candidate).

Read [the paper](paper.pdf), its [accessible source](paper.md), and [the status and limits](STATUS.md). This unrefereed candidate proves structural sufficient conditions for the sharp normalized-Laplacian threshold. It does not resolve the general Faught–Kempton–Knudson conjecture.

The principal result is the strict-majority theorem with full equality classification. Extensions give a weighted quantitative certificate, explicit positive surplus for nonsingleton majority parts, and an infinite family outside every majority/minority partition class. Classical matrix methods are credited. The family has an elementary exact spectrum; its purpose is certificate-class separation, not a claim of a previously inaccessible spectral value.

The paper also includes an exact pendant reduction and finite computational evidence, with their scope kept separate from universal proofs. See [computational assurance](COMPUTATIONAL_ASSURANCE.md), [source comparisons](SOURCES.md), [citation audit](CITATION_AUDIT.md), and [review response](REVIEW_RESPONSE.md).

## Reproduce

Python 3 is required; install SymPy for the independent arithmetic/symbolic checks. Full enumeration needs nauty `geng` (some distributions call it `nauty-geng`). From the package root:

```sh
python3 verification/self_test.py
python3 -O verification/self_test.py
python3 verification/review_checks.py
python3 -O verification/review_checks.py
python3 verification/weighted/verify_certificates.py
python3 -O verification/weighted/verify_certificates.py
python3 verification/exact_small_graphs.py --geng /path/to/geng --max-n 9
python3 -O verification/exact_small_graphs.py --geng /path/to/geng --max-n 9
python3 verification/audit_recorded_candidates.py
python3 -O verification/audit_recorded_candidates.py
```

Further commands, receipts and data provenance are in [verification/README.md](verification/README.md). Every command must exit successfully; optimized mode retains the explicit mathematical checks. Do not replace a recorded receipt with a new execution: save new outputs separately.

The manuscript was built with Pandoc and pdfLaTeX:

```sh
pandoc paper.md --from=markdown+tex_math_single_backslash --standalone --pdf-engine=pdflatex -o rebuilt-paper.pdf
```

The output PDF can differ at the byte level because of TeX timestamps; mathematical and visual content must agree. `MANIFEST.sha256` identifies the shipped bytes. The release asset checksum file identifies the enclosing archive and PDF.

## Reuse and assurance

Original prose/data are CC0-1.0; code is MIT. Third-party works retain their terms. See [licence map](LICENSES.md) and [provenance](PROVENANCE.md). Internal agent checking is not human peer review, formal verification, or independent reproduction. A complete machine-oriented entry point is [AI_INDEX.md](AI_INDEX.md).
