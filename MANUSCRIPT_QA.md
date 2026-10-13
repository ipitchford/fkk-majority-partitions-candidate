# Manuscript inspection

The final source was compiled with Pandoc and pdfLaTeX on 13 October 2026. The PDF has 13 pages and names Anonymous as author.

- Source SHA-256: `39bf41aadad7b2d233c6b778fd5351255304eedb616ae13f1a499e5b028565d9`
- PDF SHA-256: `eb551f2bb44ec5c497c8a9ff94d558db6f8a7565675b52be3ea03f475bef8996`
- Build: `pandoc paper.md --from=markdown+tex_math_single_backslash --standalone --pdf-engine=pdflatex -o paper.pdf`

The lead agent inspected rendered images of **all 13 final pages** at 1400-pixel height, including every equation, both computation tables and the references. The initial rendering exposed an overlong piecewise definition and crowded display placement; these were repaired by splitting the definition and reserving space before selected result blocks. The final rendering has readable mathematical notation, no clipped formula, no overlapping text and no visible raw TeX. Long tables continue with repeated headers. The last reference/licence page is intentionally shorter.

The installed `pdf_tex_preflight.py` checked extracted text of the final PDF and reported zero raw-TeX findings. Source result labels run 1–9, equation labels 1–18, and source/PDF metadata agree on title, Anonymous creator, date, version and reserved DOI. The mathematical reviewer checked the layout-only source delta and rebound the exact final source hash; no mathematical assertion changed in that delta.

These checks establish the observed rendering and source identity, not the mathematical truth of the paper. Proof and literature assessment are separate in FINAL_RIGOUR.md and FINAL_REVIEW.md.
