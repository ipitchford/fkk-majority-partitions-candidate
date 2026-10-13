# Final contribution and indicative REF assessment

**Review date:** 13 October 2026  
**Manuscript:** *Strict majority partitions and weighted certificates for normalized Laplacian gaps*, version 0.1.0-candidate  
**Reviewed file:** `paper.md`  
**SHA-256:** `39bf41aadad7b2d233c6b778fd5351255304eedb616ae13f1a499e5b028565d9`

This report is bound to the manuscript bytes identified above. A later manuscript requires a checked update to this record. It assesses research content, not publication, DOI activation, website deployment or public playback.

The full manuscript read used the immediately preceding hash `0fadfbb083a4128eab0019640c192e723f2fe375f878eb9592729f25b811487b`. The final layout changes were inspected: page-spacing directives were added, the beta/Gamma display was split, and the identical r/e definitions moved into prose. The scientific assessment is unchanged. The separately authored `FINAL_RIGOUR.md`, read for this report, records a mathematical PASS bound to the final hash, with no required mathematical revision.

**Review provenance.** This is an AI-assisted internal editorial assessment. The reviewer initially conducted a fresh literature review without consulting earlier verdicts, then supplied prior-art advice and some extension calculations. The present assessment is therefore not a blind independent review of the subsequent revision, and is not human journal peer review. Its conclusions should be read with that limitation.

## 1. Executive assessment

The strengthened manuscript is a coherent and potentially publishable specialist theorem note. Its central contribution is a sharp sufficient condition for the normalized-Laplacian Nordhaus–Gaddum threshold, including a complete equality classification. A single sum-of-squares identity also supplies degree-sensitive bounds, an explicit exclusion of nonsingleton majority partitions near equality, and a weighted certificate. The revision now proves that this certificate covers an infinite family admitting neither majority nor minority partitions; it no longer leaves additional coverage merely hypothetical.

The prior major contribution-positioning objections have been addressed. Classical matrix equivalences and ground-state methods receive explicit credit; the elementary spectra are identified as illustrations; and computational claims retain precise limits. The stronger join comparison and the parity-sensitive surplus add substantive mathematical information, rather than merely length.

My editorial recommendation is **accept as a specialist theorem note within its stated scope**, subject to the separately conducted final correctness and release checks. My indicative overall REF assessment remains **2\***, with a credible but presently unestablished case for 3*. The limiting consideration is demonstrated significance: the framework gives useful sharp sufficient conditions, but its strongest new coverage example has a much larger elementary exact gap, and the manuscript has not demonstrated a wider structural consequence or a comparably difficult additional class. Solving the entire conjecture is not a prerequisite for 3*. Confidence in this borderline quality judgement is moderate; it is not an official REF decision.

## 2. Scope and evidence limits

The relevant field is spectral graph theory, under Mathematical Sciences, UoA 10. This report evaluates originality, significance, mathematical presentation and the limits of inference for the exact frozen manuscript. I read the complete final text and its computational assurance statement. I checked the odd-part elementary inequality and independently derived the two rank-two bipartite spectral calculations during development. I did not independently rerun the final release's full enumeration or establish the completeness of its generator.

The live primary-source searches conducted on the review date are carried forward into this assessment. They are targeted searches, not exhaustive priority verification. Editorial acceptance here means suitability of the contribution and presentation for a specialist note; it is not acceptance by a named journal or confirmation that the release checks have finished.

## 3. Contribution and positioning

Theorem 2 is the main result: a vertexwise strict cross-majority condition guarantees the exact conjectured threshold, and equality forces the hub-and-two-equal-cliques structure. The novelty candidate is the sufficient theorem and necessity of that equality structure; the threshold and extremal example are already in Faught–Kempton–Knudson.

The revision makes four material improvements to the contribution:

1. Proposition 4 turns strictness for nonsingleton partitions into explicit parity-sensitive bounds, including cases where the minimum pointwise deficit is zero.
2. The join corollary now explicitly and uniformly improves the particular Kim–Madras size-sensitive estimate it compares against.
3. Proposition 6 quantifies the graph-specific weighted certificate and correctly distinguishes a fixed-parameter LP from joint nonlinear optimization.
4. Theorem 7 proves graph-level separation from **both** majority and minority partitions, with an explicit positive integer witness and a constant certificate bound exceeding 1/8.

These additions form a connected mathematical development. Their value is not measured by how many propositions they produce. The weighted machinery is classical, but applying familiar tools can still support original graph theory. Conversely, the new family should not be treated as a hard new spectral calculation: its exact gap tends to 1, and the manuscript candidly records that the certificate tends to 1/8.

## 4. Major comments

**No unresolved major contribution-reporting correction is required for the stated specialist-note scope.** The principal remaining objection concerns the level of significance, not a false theorem or a missing attribution.

**Issue:** the demonstrated reach of the certificate remains relatively local. **Manuscript evidence:** Theorem 7 supplies an infinite separation family, but Equation (12) gives a straightforward stronger exact answer on that family; Proposition 4 gives a small explicit surplus rather than a structural classification of near-extremisers. **Why it matters:** these results show that the framework is more than a restatement of the majority condition, but do not yet establish that it changes how a substantial unresolved part of the problem can be attacked. **Decision-changing evidence:** a further structurally broad class not already accessible to elementary spectra, a useful existence theorem for certifying partitions, or a strong structural consequence of the surplus could materially strengthen the significance case. None is required to make the present narrowly stated results publishable.

The strongest contrary argument is that the combination of a sharp threshold, full equality classification, quantitative refinements and a provably broader certificate already constitutes internationally excellent specialist research. This is a reasonable 3* argument. My reservation is that the newly demonstrated breadth chiefly concerns certificate expressiveness, while a stronger mathematical consequence of that breadth has not yet been shown.

## 5. Rigour, results and inference

The final manuscript's logical boundaries are unusually explicit. It distinguishes the exact decomposition from sufficient positivity conditions, the LP certificate from partition discovery, numerical discovery from exact decisions, and finite verification from proof for arbitrary order. The proof of absence of a majority partition in the complement of the missing-star family is necessary and now supplied. The positive-vector optimization includes reducible and singular cases. The exact pendant reduction retains the variance correction and is genuinely an equivalence.

The elementary odd-part estimate follows from the identity `r||f||^2-4PN` and the odd-cardinality bound `2sqrt(pq)<=sqrt(r^2-1)`. It supports the stated quantitative exclusion of nonsingleton partitions. The text appropriately does not rename this an edit-distance stability theorem. Likewise, the stronger join comparison is limited to the two displayed estimates, rather than claimed to dominate all existing join theory.

The computational assurance statement reports hardened guards, exact PSD decisions, independent principal-minor comparisons, symbolic residual checks and normal/optimized execution. The manuscript acknowledges that the independent PSD oracle does not independently check returned rank, and that nauty remains the enumeration dependency. These are proper assurance boundaries. My rigour calibration below is based primarily on inspectable mathematical proofs and transparent reproducibility design; it does not claim that this reviewer independently repeated all release computations.

## 6. External literature check

Search date: 13 October 2026. Sources: web search, arXiv full text/PDF, primary publisher passages and author-hosted published PDFs. Search families included normalized-Laplacian majority/bipartition/half-degree bounds; missing-star and near-complete bipartite spectra; symmetric M-matrix and diagonal-scaling certificates; ground-state representations; and signed-graph parity/stability estimates. Latest relevant 2026 preprints were checked. No exact prior match for the main sharp majority theorem or its parity refinement was found. This does not establish global priority.

| Pivotal primary source and locator | Supported comparison |
|---|---|
| [Faught–Kempton–Knudson](https://arxiv.org/pdf/2304.01979), Conjecture 3.3 and Proposition 3.4 | Establishes the prior threshold, conjectured extremal structure and known extremal spectrum. The manuscript proves a sufficient structural case. |
| [Kim–Madras v2](https://arxiv.org/html/2404.15167v2), Theorem 3.1 and Proposition 4.1 | Supplies the specific join and diameter-two benchmarks. The final quantitative join estimate improves the former; diameter-three coverage distinguishes the majority condition from the latter's hypothesis. |
| [Boman et al.](https://www.cs.tau.ac.il/research/doron.chen/Pubs/factorwidth.pdf), printed p. 242, Lemma 5, Definition 7, Theorem 8 | Supplies classical PSD/positive-scaling equivalences and explicitly discusses linear feasibility. The final manuscript now credits this accurately. |
| [Keller–Pinchover–Pogorzelski](https://arxiv.org/pdf/1708.09664), Proposition 4.8 | Supplies the classical ground-state transformation. Proposition 6 is a graph-specific application, not a new general identity. |
| [Einollahzadeh–Karkhaneei](https://arxiv.org/pdf/1901.02047), Theorems 1–2 | Gives unnormalized algebraic-connectivity results; the final contextual normalized comparisons are correctly presented as consequences of prior work. |

The inspected [2026 Kemeny paper](https://arxiv.org/html/2608.08797v2), Section 5, and [2026 upper-bound paper](https://arxiv.org/html/2606.12751v1), Section 4.2, address different targets. Searches also found second-largest-eigenvalue results for near-complete bipartite graphs; spectral ordering and inequality direction prevent treating these as direct lower-gap antecedents.

Limitations include incomplete citation chaining, unsearched languages and dissertations, and possible equivalent results indexed under other terminology. A direct prior theorem implying the main result would change the originality assessment. No retraction/correction claim is made beyond the sources actually inspected.

## 7. Minor comments

No mandatory textual correction remains within this contribution review. Future exposition could move some computational execution details into the supplement and give a small schematic of the missing-star witness, but these are optional presentation choices. The manuscript is already clear about its restricted scope.

## 8. Prioritised revision and release plan

**Must complete before treating the release as verified:** the separate mathematical audit has passed; complete and preserve the artefact/release checks and bind them to the actual released manuscript and files. If the manuscript changes, update this report only after examining the change.

**Should strengthen in future research:** test the certificate on structurally richer families, investigate existence or discovery of certifying partitions, and determine whether the parity surplus has useful structural consequences.

**Could improve presentation:** shorten operational detail in the article while retaining executable supplement instructions. Additional finite enumeration alone would chiefly strengthen assurance, not remedy the significance limitation.

## 9. Editorial disposition

**Accept as a specialist theorem note**, conditional on separate final correctness and release checks; moderate confidence. The original requests for attribution, demonstrated extra coverage, exact pendant comparison and precise computational boundaries have been met. There is no contribution-based reason to keep the manuscript in a major-revision state merely because the overall indicative REF grade is 2*. Editorial publishability and REF excellence calibration are distinct judgements.

## 10. Indicative REF calibration

The [current REF 2029 CKU guidance](https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/) provides the assessment context. Mathematical Sciences remains [UoA 10](https://2029.ref.ac.uk/panels/units-of-assessment/). The star meanings below use the official established [output-level definitions](https://2021.ref.ac.uk/guidance-on-results/guidance-on-ref-2021-results/index.html): 2* is internationally recognised; 3* internationally excellent; 4* world-leading in originality, significance and rigour. I have not verified a final REF 2029 Mathematical Sciences-specific output rubric, so do not imply one has been applied.

| Dimension | Indicative grade | Rationale and confidence |
|---|---|---|
| Originality | **3\*** | A plausibly new sharp structural theorem and equality classification, now coherently extended by quantitative strictness and a proved certificate separation. Classical ingredients are properly distinguished. Moderate confidence because priority searches are bounded. |
| Significance | **2\*** | A useful, substantial specialist contribution with sharper known-bound comparisons. The broader certificate has not yet produced a comparably strong consequence beyond an elementary-spectrum family, and the parity result is an effective surplus rather than broad structural stability. Moderate confidence; 3* is a defensible alternative judgement. |
| Rigour | **3\*** | Explicit proofs, singular-case handling, exact reductions and unusually clear computational assurance boundaries. Confidence is moderate-to-high for the inspected mathematics and limited by reliance on the separate final release audit. |
| Overall output quality | **2\*** | Holistic assessment, not an average. The revision strengthens originality and removes earlier weaknesses, but demonstrated significance still supports internationally recognised quality more securely than internationally excellent quality. Moderate confidence. |

A complete solution of the general conjecture is **not** required for 3*. Nor do elementary methods preclude 3* or 4*: a short sharp theorem can be highly significant. The assessment rests on what this particular collection of results establishes and enables. More pages, more theorem labels, more exact checks, author identity, journal reputation and a requested target rating have not been used as quality proxies. This is indicative internal judgement, not an official panel decision or a prediction of institutional REF outcomes.

## 11. References

Faught, J. N., Kempton, M., & Knudson, A. (2024). A Nordhaus–Gaddum type problem for the normalized Laplacian spectrum and graph Cheeger constant. *Applied Mathematics and Computation, 480*, 128920. https://arxiv.org/abs/2304.01979

Kim, S., & Madras, N. (2025). A Nordhaus–Gaddum problem for the spectral gap of a graph. *Journal of Graph Theory, 110*, 132–144. https://doi.org/10.1002/jgt.23253

Boman, E. G., Chen, D., Parekh, O., & Toledo, S. (2005). On factor width and symmetric H-matrices. *Linear Algebra and Its Applications, 405*, 239–248. https://doi.org/10.1016/j.laa.2005.03.029

Keller, M., Pinchover, Y., & Pogorzelski, F. (2020). Criticality theory for Schrödinger operators on graphs. *Journal of Spectral Theory, 10*(1), 73–114. https://doi.org/10.4171/JST/286

Einollahzadeh, M., & Karkhaneei, M. M. (2021). On the lower bound of the sum of the algebraic connectivity of a graph and its complement. *Journal of Combinatorial Theory, Series B, 151*, 235–249. https://arxiv.org/abs/1901.02047

Li, W., Sun, W., & Yang, Y. (2026). *On two conjectures concerning Kemeny's constant of graphs* [Preprint, version 2]. https://arxiv.org/abs/2608.08797

Kempton, M., Zaitzeff, X., & Muthuprakash, S. (2026). *Nordhaus–Gaddum upper bounds for graph connectivity parameters* [Preprint]. https://arxiv.org/abs/2606.12751

Research Excellence Framework. (n.d.). *Section 4—Contributions to Knowledge and Understanding guidance*; *Units of assessment*; *Guidance on REF 2021 results*. Official URLs are linked in Section 10; accessed 13 October 2026.

All eleven review-protocol parts have been completed within the evidence limits stated above.
