# Response to full review

Article: *Strict majority partitions and weighted certificates for normalized Laplacian gaps*. Creator: Anonymous. Version: 0.1.0-candidate. Date: 13 October 2026. DOI: 10.5281/zenodo.23336669. Article license: CC0 1.0.

Frozen manuscript SHA-256:

`0fadfbb083a4128eab0019640c192e723f2fe375f878eb9592729f25b811487b`

The original archives and prior manuscripts remain unchanged. This ledger identifies the completed revisions and exact remaining publication gates; it does not itself assert publication or independent human peer review.

## Required and recommended revisions

| Review item | Implemented action | Status |
|---|---|---|
| 4.1 matrix attribution | Full Boman–Chen–Parekh–Toledo citation, classical specialization label, graph-specific matrix derivation clearly separated. Ground-state transformation attributed to Keller–Pinchover–Pogorzelski; Perron–Frobenius/Collatz–Wielandt optimization identified as classical. | Done |
| 4.2 fixed-partition versus graph-class scope | Explicit partition-search distinction retained. New Theorem 7 proves graph-class separation: neither H_k nor its complement has any majority partition. The certificate succeeds with an integer witness. | Done, strengthened beyond requested correction |
| 4.3 permanent article versus process | Removed archive, submission and prior-review history from theorem exposition; standalone contribution paragraph and restrained open-problem scope. Provenance belongs in separate PROVENANCE.md. | Done |
| 4.4 direct pendant calculation | Corollary 9 now uses rank-two singular values for the full spectrum; singleton classification follows directly, replacing polynomial positivity. General exact reduction retained as Theorem 8. | Done |
| Minor 1 local eigenfunction hypotheses | Connected graph, n≥3, nonzero generalized eigenfunction and positive Fiedler eigenvalue stated locally. | Done |
| Minor 2 equation order | Equations numbered sequentially 1–18; result labels 1–9; textual cross-references updated. | Done |
| Minor 3 definitions | Join, disjoint union, complete graph, PSD, LP and second-order-cone terminology defined. | Done |
| Minor 4 corollary domain | n≥5 explicitly in Corollary 5. Main majority theorem retains n≥3. | Done |
| Minor 5 reproducibility | Exact tables, generator hash and citation, actual release paths, replay commands, receipt filenames, arithmetic-versus-generation and replay-versus-independent-implementation distinctions. | Done |
| Minor 6 normal Python | Hardened release scripts replace assertion-based load-bearing checks with exceptions. Paper now states successful normal and optimized runs; historical originals retained separately. | Done by verifier agent and reflected in paper |
| Minor 7 references | Version-specific Kim–Madras theorem numbering retained; nauty/McKay–Piperno citation added. | Done |
| Quantitative comparison | Corollary 3 gives an explicit size-sensitive join estimate strictly exceeding k/(n−1), hence the cited k/[32(n−1)]. No generic-priority claim. | Done |
| Nonconstant rational witness | Theorem 7 uses integer coordinates 4k−7,5,1; at k=4 these are 9,5,1. Proposition 6 gives the explicit residual margin. | Done |
| Optional larger class | Infinite family proves simultaneous absence of majority partitions in graph and complement. Exact small-order comparison also records 441 examples, 338 with the complementary exclusion. | Done |
| Optional stability direction | Proposition 4 gives parity-dependent and uniform positive surplus for nonsingleton majority partitions. Explicitly not an edit-distance or general structural stability theorem. | Done within proved scope |

## Mathematical verification before freeze

The manuscript editor independently checked the weighted ground-state expansion, componentwise attainment of the optimized residual (including reducible and singular matrices), integer missing-star witness, both all-partition exclusion arguments, parity proof in all three regimes, direct pendant spectrum and singleton comparison, and size-sensitive join comparison. Elementary identities in the direct pendant and join simplifications were checked symbolically. The infinite-family and parity proofs are all-parameter proofs, not deductions from finite checking.

The spectrum of the missing-star family is included to avoid exaggerating the difficulty of those individual examples: its actual gap tends to one while the explicit weighted lower bound tends to one eighth. The graph-class enlargement and quantitative certificate are the contribution claimed for that family.

The new extension evidence is incorporated; no mathematical placeholder or pending extension claim remains in the article. Its supporting files are in verification/weighted/, with independent all-partition certificate replay, exact family checks, and parity receipts. The full release computation is documented in COMPUTATIONAL_ASSURANCE.md and verification/README.md. Candidate-list validation does not establish completeness of its original selection; no full order-10/11 replay is claimed.

## Publication gates after this freeze

- Fresh targeted correctness audit: completed, mathematical PASS; see FINAL_RIGOUR.md.
- Final contribution/REF assessment: completed; accept as specialist theorem note, indicative O3/S2/R3 and overall2; see FINAL_REVIEW.md, including its participation disclosure.
- Compilation and all-page visual inspection: completed; see MANUSCRIPT_QA.md. The presentation-only delta was checked and the final source SHA-256 is 39bf41aadad7b2d233c6b778fd5351255304eedb616ae13f1a499e5b028565d9.
- Repository, archive, provider bytes and canonical readback: root-owned publication steps; this ledger makes no claim that they are complete.

There are no unfinished editorial or extension tasks assigned to the manuscript editor. Do not present the earlier review's provisional rating as the final rating of this expanded frozen version.
