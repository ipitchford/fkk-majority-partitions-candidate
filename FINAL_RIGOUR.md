# Final mathematical rigour audit

Date: 13 October 2026. Source: `paper.md`, version `0.1.0-candidate`, with DOI header `10.5281/zenodo.23336669`.

Exact source SHA-256:

```text
39bf41aadad7b2d233c6b778fd5351255304eedb616ae13f1a499e5b028565d9
```

The full proof read was performed on the preceding source, SHA-256 `0fadfbb083a4128eab0019640c192e723f2fe375f878eb9592729f25b811487b`. A line-by-line delta read confirms that this final source changes only TeX page-layout directives and splits the β/Γ display, moving the identical definitions of r and e into prose. No hypothesis, coefficient or conclusion changes. The audit therefore binds the final hash shown above.

## Finding and review boundary

No mathematical error or missing essential argument was found in this frozen source. The new weighted quantitative certificate, infinite separation family, parity-dependent surplus, direct pendant spectrum and join comparison are valid as stated. No mathematical correction is required before freezing this version. Confidence is high, but this is an agent-assisted proof audit, not a claim of formal verification, independent human peer review, global originality, journal acceptance or official REF quality. The DOI header was checked as part of the source bytes; this audit does not establish publication or DOI-resolution status.

The whole frozen manuscript was read. Particular attention was given to the new mathematics relative to the earlier corrected theorem note. The reviewer had previously audited the original sum-of-squares identity, equality classification, linear feasibility equivalence, pendant Schur complement, supporting eigenfunction identities and exact spectral matrix. These remain valid in the frozen version. No desired verdict was assumed. Literature attribution and priority are addressed by the separate source and citation audits, not independently recertified here.

## Proposition 4: effective strictness

For an ordinarily centred vector, the reduction from `X ≥ Γ‖f‖²` to the spectral surplus `Γ/((n−1)Δ)` has the correct direction: the weighted variance is at most `Δ‖f‖²`.

In the even/even case each opposite part has even order, so the nonnegative integer `q` is odd and at least one. The retained diagonal in the exact identity gives the claimed coefficient `n−2`.

For an odd part of size `r`, each edge difference or nonedge sum square is at least the corresponding absolute-value difference square. The sum of the latter over all pairs is `r‖f‖²−(P+N)²`; adding the squared coordinate sum gives `r‖f‖²−4PN`. If there are `p` positive and `q` negative coordinates, Cauchy–Schwarz and `2xy≤x²+y²` give `4PN≤2√(pq)‖f‖²`. Integer counts with `p+q≤r` and odd `r` satisfy `4pq≤r²−1`, including zero coordinates. Thus the claimed odd-part bound is valid without any nonzero-coordinate assumption. Allocating the two part sums and discarding remaining nonnegative terms is legitimate; the odd-part coefficient decreases with part size.

In the mixed case, every odd-side coordinate has `q≥1`. Every zero-q even-side coordinate has `(o−1)/2≥1` missing neighbours, and selecting one creates disjoint stars because each such coordinate selects exactly one centre. Every centre has at most `e/2−1` missing neighbours by strict majority. The retained coefficient of each selected missing-pair square can be lowered from `n−1` to `n−2`. Positive-q even coordinates contribute independent positive diagonal terms. For a j-leaf star the centre/constant-leaf block has characteristic polynomial `x²−(j+2)x+1`, while leaf differences have eigenvalue one. Its least eigenvalue is precisely βj; βj decreases with j. The e=2 case has no missing pair and is covered by β0=1.

The uniform constant is conservative but correct. In the odd case Γ exceeds `1/(2r)≥1/(2(n−2))`. In the mixed case rationalisation gives `βd≥1/(d+2)`, and `e≤n−3` is more than sufficient to reach the stated universal lower bound. With `Δ≤n−1`, equation (5) follows. The near-equality consequence is an exclusion of nonsingleton majority partitions, correctly distinguished from an edit-distance stability theorem.

## Proposition 6: weighted optimum and LP statement

Expanding the positive-scaling identity cancels exactly the added diagonal terms and leaves off-diagonal coefficients `−2(n−1)yuyv`. It therefore establishes `C ⪰ τ(z)D` for every positive z, irrespective of the sign of τ. Sign switching one part preserves the degree norm. The spectral lower bound uses `τ≥0` exactly where the weighted squared norm is replaced by variance; the manuscript explicitly includes that hypothesis.

For the converse optimisation, every nontrivial missing-edge component gives an irreducible symmetric matrix with nonpositive off-diagonal entries after degree scaling. A sufficiently large diagonal shift is nonnegative and irreducible, so Perron–Frobenius gives a positive eigenvector for its smallest eigenvalue. Setting `z=D^(−1/2)v` gives `Cz=θDz` on that component. Isolated coordinates have the same ratio for every positive choice. Concatenating component vectors attains the least component eigenvalue. Thus the expression is a maximum, not merely a supremum; reducibility and singularity do not invalidate attainment.

For fixed τ, the same argument applied to `C−τD` proves the stated positive-vector feasibility criterion, and homogeneous scaling supplies `z≥1`. The warning that joint optimisation in τ and z is not a single LP is correct. No generic matrix-theory novelty is claimed.

## Theorem 7: graph-class separation and quantitative witness

The connectivity claims follow from the complete ordinary rows and the nonempty complementary linking star. Both exclusions concern all partitions, rather than merely failure of the natural partition.

For the bipartite graph, mixing original colours within either proposed part would require incompatible strict majorities of the two colours on the opposite side. Hence any majority partition must be the original colouring, which fails at the exceptional degree-two vertex for k≥4.

For the complement, an ordinary A vertex and either of the two retained-neighbour vertices P have neighbours confined to disjoint original colours. They cannot share a part. Since both classes are nonempty, this forces all ordinary A vertices together and both P vertices opposite. An ordinary A vertex has either no cross neighbour or just u, in a side of at least three vertices. This excludes majority in the complement, and hence minority in the original graph.

The matrix diagonal coefficients and degrees are correct. Multiplying the stated positive witness gives `2(k−3)²` on the whole missing-star component, and `2(k−1)²` elsewhere. The centre ratio is the minimum: `5(k−1)≤2(4k−7)` for k≥4 controls the leaves, and comparison with the other vertices is strict. Substituting τ gives equation (11); subtracting 1/8 has positive numerator `34k−47` over a positive denominator. The k=4 witness is exactly 9 at the exceptional vertex, 5 at its two missing neighbours, and 1 elsewhere.

The claim about adding arbitrary internal edges is also correct. The matrix C depends only on cross pairs, and the positive τ witness already makes C positive definite. Internal additions preserve connectedness and the sufficient matrix certificate. This claim does not preserve the numerical 1/8 bound or the absence of other majority partitions; the manuscript does not assert either preservation.

The spectrum in equation (12) follows from two independent row types, one singular value equal to one and squared Frobenius norm `1+(k−2)/k²`. The remaining singular value is `√(k−2)/k` and all additional adjacency eigenvalues are zero. Multiplicities total 2k. The stated limitation—actual gap tending to one while the certificate tends to 1/8—is essential and accurate.

## Pendant spectrum and joins

For a pendant attached in the a-part of K(a,b), the normalized bipartite block has rank two for a≥2,b≥1. The attachment row and ordinary rows are independent because only the former meets the leaf. The three contributions to its squared Frobenius norm are `b/[a(b+1)]`, `(a−1)/a` and `1/(b+1)`, summing to `1+(a−1)/[a(b+1)]`. This proves all eigenvalues and the multiplicity in (16), including a=2,b=1. For a=1 the separate star statement is correct.

For a,b≥2 the nontrivial singular value is strictly less than 1/√3. Since `1−1/√3>2/5`, all N≥5 cases follow; the N=4 case has gap `1−1/√6>1/2`. The singleton classification follows on squaring a comparison between positive quantities and reduces exactly to `a²−4a−1>0`. The Schur-complement criterion remains independently correct and is not needed to force this simpler application.

For a join, `η≥(k−1)/(n−1)` is valid and the proposed bound exceeds `k/(n−1)` by `(n−k)/(n−1)²>0`. The comparison to the explicitly quoted weaker Kim–Madras bound is algebraically valid; priority beyond that comparison is not implied.

## Focused checks and computational scope

In addition to analytic checking, a focused independent countercheck enumerated all 127 unordered nontrivial cuts of H4 and of its complement; neither had a majority partition. Exact Fraction arithmetic checked the star residual, minimum ratio, rational lower-bound formula and strict comparison with 1/8 for k=4 through 20. All passed. These small checks supplement the all-parameter proofs; they are not their justification.

The release hardening audit already executed the original finite graph claims in ordinary and optimised Python, with matching 288,248-graph results and all 72,677 candidate decisions. Its 600-matrix independent oracle tests PSD decisions rather than rank, as the frozen source explicitly states. The weighted/parity search and receipts are described by their separate computational reviewer; this final mathematical audit did not repeat that broader search or claim independent validation of its coverage counts.

## Strongest remaining objection and final disposition

The main remaining objection is significance and originality, not a detected proof defect. The weighted optimisation is established matrix machinery, the displayed separation family has an elementary exact spectrum, and the parity surplus is a conservative class-specific estimate. None resolves unrestricted partition existence or the full conjecture. The manuscript accurately limits these claims and nevertheless proves a genuine strict enlargement of certificate coverage and an effective gap for nonsingleton majority partitions.

**Disposition:** mathematical rigour check passed for the exact source hash above; no required mathematical revision identified. A later source edit requires a scoped readback and a new hash before this audit can be represented as applying to that version.
