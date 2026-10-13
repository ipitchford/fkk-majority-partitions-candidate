---
title: "Strict majority partitions and weighted certificates for normalized Laplacian gaps"
author: "Anonymous"
license: "CC0-1.0"
version: "0.1.0-candidate"
doi: "10.5281/zenodo.23336669"
date: "13 October 2026"
geometry: margin=1in
fontsize: 11pt
header-includes:
  - '\usepackage{needspace}'
  - '\raggedbottom'
---

Version 0.1.0-candidate · [DOI: 10.5281/zenodo.23336669](https://doi.org/10.5281/zenodo.23336669) · [Source and verification](https://github.com/ipitchford/fkk-majority-partitions-candidate)

## Abstract

We establish a sharp structural sufficient condition for the normalized-Laplacian Nordhaus–Gaddum threshold: if a graph of order $n\ge3$ has a bipartition in which every vertex is adjacent to strictly more than half of the opposite part, then its second normalized-Laplacian eigenvalue is at least $2/(n-1)$. Equality occurs precisely for $K_1\vee(K_m+K_m)$. A sum-of-squares identity yields degree-sensitive and parity-sensitive improvements. Applying classical positive-scaling identities to a graph-specific matrix gives a quantitative weighted certificate. An explicit infinite family satisfies that certificate although neither the graph nor its complement admits a strict-majority partition. We also give an exact pendant reduction and a direct spectrum for a complete bipartite graph with a pendant. Exact arithmetic verifies the conjectured bound and equality classification through order nine. These structural results do not resolve the general Faught–Kempton–Knudson conjecture.

## 1. Setting and contribution

All graphs are finite, simple and undirected. The join $H_1\vee H_2$ is obtained from their disjoint union by adding every edge between the two vertex sets. We write $H_1+H_2$ for disjoint union and $K_m$ for the complete graph of order $m$. Write $\overline H$ for the complement, $d_u$ for vertex degrees, $D=\operatorname{diag}(d_u)$, $A$ for adjacency, and $L=D-A$. We use
\[
\mathcal L=D^{-1/2}LD^{-1/2},
\]
with inverse square roots zero at isolated vertices. Thus isolated vertices contribute zero eigenvalues. Write $\lambda_2(H)$ for the second-smallest eigenvalue. For connected $H$ of order at least two, all degrees are positive, and
\[
E_H(f)=\sum_{uv\in E(H)}(f_u-f_v)^2,\qquad
V_H(f)=\min_c\sum_u d_u(f_u-c)^2
=\sum_u d_uf_u^2-\frac{(\sum_ud_uf_u)^2}{w_H},
\]
where $w_H=\sum_ud_u$. The variational formula is
\[
\lambda_2(H)=\min_{f\text{ nonconstant}}E_H(f)/V_H(f).
\]
Both forms are invariant under adding a constant. In particular we may impose ordinary, rather than degree-weighted, mean zero when proving inequalities between them.

Faught, Kempton and Knudson [1, Conjecture 3.3] conjecture that, for $n\ge5$,
\[
\max\{\lambda_2(G),\lambda_2(\overline G)\}\ge\frac2{n-1},
\tag{1}
\]
with equality exactly when $n$ is odd and one graph is $K_1\vee(K_{(n-1)/2}+K_{(n-1)/2})$. The equality formulation here is symmetric under complementation.

The main result below proves (1) for graphs possessing a strict majority or strict minority partition, including the case where either graph is disconnected. It also covers some both-connected graphs outside the diameter-two setting of Kim–Madras [2, Proposition 4.1]. For example, $C_6=K_{3,3}$ minus a perfect matching has a strict majority partition and connected complement, but has diameter three. This describes coverage, not a claim of priority over every existing spectral bound.

Related recent work studies Kemeny's constant [4] and Nordhaus–Gaddum upper bounds [5]; these concern different targets.

Our main contribution is the sharp strict-majority theorem and its equality classification, obtained from a partition sum-of-squares identity. The same identity yields degree-sensitive and parity-sensitive improvements and a graph-specific weighted certificate. An infinite family proves that the weighted certificate strictly enlarges the graph class covered by majority or minority partitions. The latter uses classical positive-semidefinite and scaled-diagonal-dominance equivalences [6]. An exact pendant reduction and an elementary complete-bipartite application illustrate complementary certificate methods. Exact finite checks support these results without resolving the general conjecture.

## 2. The partition identity

Fix nonempty parts $S,T$ with $V(H)=S\sqcup T$. Put $s=|S|$, $t=|T|$, $n=s+t\ge3$. Let $M$ be the missing cross pairs, and let $m_u$ be the number of pairs in $M$ incident to $u$. Define
\[
q_u=\begin{cases}t-1-2m_u,&u\in S,\\s-1-2m_u,&u\in T.\end{cases}
\]
Equivalently, $q_u=2d_{\rm cross}(u)-|\text{opposite part}|-1$.
Let $E_S,E_T$ be the internal edge energies and let
\[
\overline Q_S(f)=\sum_{\substack{\{u,v\}\subseteq S\\uv\notin E(H)}}(f_u+f_v)^2
\]
and similarly define $\overline Q_T$. Each sum is over unordered pairs once. Set
\[
X_H(f)=(n-1)E_H(f)-2V_H(f),\quad
\sigma_S=\sum_{u\in S}f_u,\quad z_H=\sum_ud_uf_u.
\]

\Needspace{11\baselineskip}

**Lemma 1 (sum-of-squares identity).** For connected $H$ and $\sum_uf_u=0$,
\[
\begin{split}
X_H(f)={}&(n-2)(E_S+E_T)+\overline Q_S+\overline Q_T\\
&+(n-1)\sum_{uv\in M}(f_u+f_v)^2
+(n-2)\sum_uq_uf_u^2\\
&+2(n-2)\sigma_S^2+\frac{2z_H^2}{w_H}.
\end{split}\tag{2}
\]

*Proof.* The all-pairs energy identity gives $E_H+E_{\overline H}=n\sum_uf_u^2$ on this subspace. Since $\overline d_u=n-1-d_u$ and
\[
2\sum_u\overline d_uf_u^2-E_{\overline H}(f)
=\sum_{uv\in E(\overline H)}(f_u+f_v)^2,
\]
we obtain
\[
X_H=(n-2)E_H-(n-2)\sum_uf_u^2
+\sum_{uv\in E(\overline H)}(f_u+f_v)^2+2z_H^2/w_H.
\]
The cross energy is
\[
t\sum_Sf_u^2+s\sum_Tf_u^2+2\sigma_S^2
-\sum_M(f_u-f_v)^2.
\]
Substitute it and use $(a-b)^2=2a^2+2b^2-(a+b)^2$ on each missing cross pair. Collecting coefficients proves (2). $\square$

## 3. Strict majority partitions

**Theorem 2.** Let $H$ have order $n\ge3$. If every vertex is adjacent to strictly more than half of the opposite part, then
\[
\lambda_2(H)\ge\frac2{n-1}.
\tag{3}
\]
Equality holds if and only if $n=2m+1$ and $H\cong K_1\vee(K_m+K_m)$.

*Proof of the bound.* The hypothesis implies $q_u\ge0$ by integrality. It also implies connectedness: any two vertices of $S$ share a neighbor in $T$, and every vertex of $T$ has a neighbor in $S$. All terms on the right of (2) are nonnegative. Thus $X_H(f)\ge0$ for every mean-zero $f$, and shift invariance proves (3). $\square$

*Proof of equality.* Suppose $X_H(f)=0$ for a nonzero mean-zero $f$. Internal edge energies vanish, so $f$ is constant on each component within each part. Internal nonedge squares vanish, so values at nonadjacent vertices within one part are opposite. Also $\sigma_S=\sigma_T=0$.

It follows that, on either part, $f$ is identically zero or that part induces two equal-sized cliques with opposite nonzero values. Indeed, three components force all component values to zero; a connected part is constant and hence zero; and a nonzero component must be complete. With exactly two nonzero components their sizes agree by the zero-sum condition.

Suppose both part sizes are at least two, and $f$ is nonzero on $S$. Then $S$ consists of two equal cliques. The terms $q_uf_u^2$ force $2m_u=t-1$ at every $u\in S$. Consequently $t$ is odd and at least three, and each $u\in S$ has a missing cross neighbor. The missing-pair squares force that neighbor's value to be nonzero. Thus $f$ is nonzero on $T$, forcing $t$ even, a contradiction.

Hence one part is a singleton, its value is zero, and the majority hypothesis makes it universal. The other part is two equal cliques. Conversely the function taking values $1,-1,0$ on the two cliques and hub has energy $2m$, variance $2m^2$ and quotient $1/m=2/(n-1)$. $\square$

\Needspace{8\baselineskip}

**Corollary 3 (degree-sensitive improvement).** Under the same hypothesis put $\eta=\min_u q_u/d_u$. Then
\[
\lambda_2(H)\ge\frac{2+(n-2)\eta}{n-1}.
\tag{4}
\]
Indeed (2) implies $X_H(f)\ge(n-2)\eta\sum_ud_uf_u^2\ge(n-2)\eta V_H(f)$. In particular, with $\rho=\min_uq_u$ and $\Delta=\max_ud_u$, one may replace $\eta$ by $\rho/\Delta$. If both parts have even size then $\rho\ge1$, giving an explicit positive surplus over (3).

**Proposition 4 (effective strictness).** Suppose the strict-majority partition has sizes $s,t\ge2$, and let $\Delta$ be the maximum degree. Set
\[
\beta_d=\frac{d+2-\sqrt{d^2+4d}}2\quad(d\ge0).
\]
Write $r=\max(s,t)$ and, in the opposite-parity case, let $e$ be the even part size. Define
\[
\Gamma(s,t)=
\begin{cases}
n-2,&s,t\text{ even},\\
r-\sqrt{r^2-1},&s,t\text{ odd},\\
(n-2)\beta_{e/2-1},&s,t\text{ of opposite parity}.
\end{cases}
\]
Then
\[
\lambda_2(H)\ge\frac2{n-1}+\frac{\Gamma(s,t)}{(n-1)\Delta}
\ge\frac2{n-1}+\frac1{2(n-1)^2(n-2)}.
\tag{5}
\]

*Proof.* We show $X_H(f)\ge\Gamma(s,t)\|f\|^2$ for ordinarily centered $f$ and use $V_H(f)\le\Delta\|f\|^2$. If both sizes are even, every $q_u$ is a positive odd integer, so (2) gives the claim immediately.

For a graph $F$ on an odd number $r$ of coordinates,
\[
E_F(f)+\overline Q_F(f)+\Big(\sum_i f_i\Big)^2
\ge\big(r-\sqrt{r^2-1}\big)\|f\|^2.
\]
Indeed every edge or nonedge square dominates $(|f_i|-|f_j|)^2$. Let $P,N$ be the sums of positive and absolute negative coordinates, with counts $p,q$. The sum of these absolute-difference squares and $(\sum f_i)^2$ is $r\|f\|^2-4PN$. Cauchy–Schwarz gives $4PN\le2\sqrt{pq}\|f\|^2\le\sqrt{r^2-1}\|f\|^2$. The last inequality uses $p+q\le r$ and odd $r$. Apply this on both odd parts, allocating $2(n-2)\sigma_S^2=(n-2)(\sigma_S^2+\sigma_T^2)$ in (2), and discard the other nonnegative terms.

For opposite parity, write $E,O$ for the even and odd parts, of sizes $e,o$. Every $q_v$ on $O$ is at least one. For each $u\in E$ with $q_u=0$, select one of its $(o-1)/2\ge1$ missing neighbors in $O$. Each center in $O$ receives at most $d=e/2-1$ selected neighbors. Retain from (2) the diagonal terms on $O$ and on positive-$q$ vertices of $E$, and one selected missing-pair square per zero-$q$ vertex. The resulting lower bound, divided by $n-2$, is a sum of disjoint star forms
\[
f_v^2+\sum_{u\text{ selected at }v}(f_u+f_v)^2
\]
and isolated coordinate squares. A star with $j$ leaves has smallest eigenvalue $\beta_j$, decreasing in $j$; this follows from its two eigenvalues $(j+2\pm\sqrt{j^2+4j})/2$ and the remaining eigenvalues $1$. An isolated center has value $\beta_0=1$. If $e=2$ there are no missing pairs and no selected leaves. This proves the mixed case.

Finally $r-\sqrt{r^2-1}>1/(2r)$ with $r\le n-2$, and $\beta_d\ge1/(d+2)$. Thus every case has $\Gamma(s,t)\ge1/[2(n-2)]$; use $\Delta\le n-1$ for the last inequality. $\square$

Consequently a graph admitting a majority partition and having surplus smaller than the last term in (5) must have a singleton majority partition, hence a universal vertex. This is an effective exclusion of nonsingleton partitions near equality; it does not give an edit-distance stability theorem.

For a join $H=H[S]\vee H[T]$, let $k=\min(s,t)$. Since $q_u$ is the opposite part's size minus one and $d_u\le n-1$, we have $\eta\ge(k-1)/(n-1)$. Consequently
\[
\lambda_2(H)\ge
\frac{2(n-1)+(n-2)(k-1)}{(n-1)^2}
>\frac{k}{n-1}.
\]
The last strict comparison follows because the difference of the numerators is $n-k>0$. Thus the quantitative corollary uniformly strengthens the bound $k/[32(n-1)]$ in Kim–Madras [2, Theorem 3.1]. This comparison concerns those two stated bounds; the constant-only estimate (3) need not dominate a size-dependent estimate.

**Corollary 5 (Nordhaus–Gaddum classes).** Let $G$ have order $n\ge5$. If $G$ has a partition with every cross degree strictly above half the opposite part, apply Theorem 2 to $G$. If every cross degree is strictly below half, apply it to $\overline G$. In either case (1) holds. Within this class its equality cases are exactly those stated in (1), since equality in the certified graph forces the hub-and-two-cliques graph, whose complement is disconnected.

If $G$ is disconnected, any partition into two nonempty unions of components is a strict minority partition. The same argument applies with $G$ and $\overline G$ exchanged. No connectedness convention is needed for their variational quotients: the proof uses the connected join on the other side.

**Sharpness of the hypothesis.** Replacing “strictly more than half” by “at least half” permits $K_{p,p}+K_{p,p}$, using the unions of left and right parts. Every cross degree is exactly half, but the graph is disconnected and its gap is zero. This shows failure of the weaker universal hypothesis, not optimality of every possible partition certificate.

## 4. Unequal deficits: an exact linear certificate

For a fixed partition, the exact identity gives a relaxation of the vertexwise condition. Feasibility for a supplied partition does not supply an algorithm for finding that partition. Theorem 7 below separately establishes additional graph-class coverage beyond all majority and minority partitions. Write
\[
R_u=(|\text{opposite part}|-1)(n-2),\qquad
a_u=R_u-(n-3)m_u.
\]
The terms involving $M$ and the diagonal $R_u$ before the last square rearrangement are
\[
\sum_ua_uf_u^2+2(n-1)\sum_{uv\in M}f_uf_v.
\tag{6}
\]
For every missing pair oriented from $S$ to $T$, choose $\varepsilon_{uv}>0$. The bound
$2f_uf_v\ge-\varepsilon_{uv}f_u^2-\varepsilon_{uv}^{-1}f_v^2$
shows that $\lambda_2(H)\ge2/(n-1)$ whenever
\[
(n-1)\sum_{v:uv\in M}\varepsilon_{uv}\le a_u\ (u\in S),\qquad
(n-1)\sum_{u:uv\in M}\varepsilon_{uv}^{-1}\le a_v\ (v\in T).
\tag{7}
\]
Here $H$ is assumed connected. This is a sufficient certificate; it is not asserted necessary for the spectral bound.

Condition (7) is convex, not linear in the displayed variables. An exact second-order-cone formulation (linear inequalities together with Euclidean-norm inequalities) uses $x_e,y_e\ge0$, the corresponding endpoint sum constraints, and
\[
\|(2,x_e-y_e)\|_2\le x_e+y_e.
\]
The last condition is $x_ey_e\ge1$. From a feasible solution choose $\varepsilon_e=x_e$ and replace $y_e$ by $1/x_e$, which only decreases its endpoint sum. Conversely set $(x_e,y_e)=(\varepsilon_e,1/\varepsilon_e)$.

There is also an equivalent linear programming (LP) feasibility formulation. A symmetric matrix is positive semidefinite (PSD) if its quadratic form is nonnegative at every vector. The equivalence below is a self-contained specialization of classical symmetric H-matrix and scaled-diagonal-dominance theory; see Boman et al. [6, Lemma 5, Definition 7 and Theorem 8]. The graph-specific step is obtaining this particular matrix from (2). Let $A_M$ be the adjacency matrix of the missing-cross-pair graph and set
\[
C=\operatorname{diag}(a)-(n-1)A_M.
\]
Then the following three conditions are equivalent:

1. Positive weights satisfy (7).
2. $C$ is positive semidefinite.
3. The linear system $Cz\ge0$, $z_u\ge1$ is feasible.

To prove this, Young's inequality gives the first implication. For the second, split $C$ into components of $M$. On a nontrivial component, the smallest-eigenvalue eigenvector can be chosen strictly positive: apply Perron–Frobenius to $kI-C$ for $k$ at least the largest diagonal entry. If $C$ is positive semidefinite, this vector satisfies $Cz\ge0$. At an isolated vertex choose $z_u=1$; positive semidefiniteness ensures its diagonal is nonnegative. Rescaling each positive component vector supplies $z\ge\mathbf1$. Finally, given this linear witness, set $\varepsilon_{uv}=z_v/z_u$ for $u\in S$, $v\in T$. The endpoint inequalities follow directly from $Cz\ge0$, proving the third implication.

Changing signs on $T$ transforms (6) into the quadratic form of $C$, so each equivalent condition certifies the spectral bound. The strict-majority hypothesis is the special witness $z=\mathbf1$, since $(C\mathbf1)_u=(n-2)q_u$. The reciprocal constraints are therefore equivalent to a linear feasibility problem. This equivalence does not assert the existence of a certifying partition for every graph.

### 4.1. Quantitative positive-vector certificates

**Proposition 6.** For a positive vector $z$ put
\[
\tau(z)=\min_u\frac{(Cz)_u}{d_uz_u}.
\]
If $\tau(z)\ge0$, then
\[
\lambda_2(H)\ge\frac{2+\tau(z)}{n-1}.
\tag{8}
\]
Moreover,
\[
\max_{z>0}\tau(z)=\lambda_{\min}(D^{-1/2}CD^{-1/2}).
\tag{9}
\]

*Proof.* Write $r_u=(Cz)_u/z_u$. Direct expansion gives the classical positive-scaling, or ground-state, identity
\[
y^{\mathsf T}Cy=\sum_ur_uy_u^2
+(n-1)\sum_{uv\in M}z_uz_v
\left(\frac{y_u}{z_u}-\frac{y_v}{z_v}\right)^2.
\tag{10}
\]
Changing signs on $T$ in the retained form (6) and using (2) therefore gives
$X_H(f)\ge\tau(z)\sum_ud_uf_u^2\ge\tau(z)V_H(f)$ for ordinarily centered $f$. The last step uses $\tau(z)\ge0$, and proves (8).

Identity (10) also implies $C\succeq\tau(z)D$, giving one direction of (9). On each connected component of $M$, Perron–Frobenius applied after a diagonal shift provides a positive smallest-eigenvalue eigenvector $v$ of $D^{-1/2}CD^{-1/2}$. Set $z=D^{-1/2}v$ there. On an isolated vertex choose any positive coordinate. Concatenating these vectors makes $\tau(z)$ equal to the smallest component eigenvalue, proving (9), including reducible and singular cases. $\square$

The ground-state identity and the Collatz–Wielandt/Perron–Frobenius optimization are classical methods, not new matrix principles [6,8]. Here they quantify the graph certificate derived from (2). The choice $z=\mathbf1$ recovers Corollary 3. For a specified real $\tau$, feasibility is the LP $(C-\tau D)z\ge0$, $z\ge\mathbf1$. Joint optimization in $\tau,z$ is not itself one LP; monotone feasibility permits bisection if numerical optimization is desired.

### 4.2. An infinite separation from majority partitions

**Theorem 7.** For $k\ge4$, let $H_k$ be $K_{k,k}$ with all but two edges at one fixed vertex $u$ deleted. Both $H_k$ and $\overline H_k$ are connected, neither has a strict-majority partition, and
\[
\lambda_2(H_k)\ge
\frac{k^2+2k-5}{(4k-7)(2k-1)}>\frac18.
\tag{11}
\]
In particular the weighted certificate covers graphs not covered by either reading of Corollary 5.

*Proof.* Let $A,B$ be the original parts, $u\in A$, let $P\subset B$ be its two neighbors, and put $Z=B\setminus P$. Connectedness of $H_k$ is immediate. Its complement consists of the two cliques $A,B$ joined by the nonempty star from $u$ to $Z$, so is also connected.

A strict-majority partition of a bipartite graph cannot mix the original colors in either part: an $A$-vertex and a $B$-vertex on one side would require the opposite side to contain strictly more than half of each color. Thus the only candidate for $H_k$ is $A\mid B$, which fails at $u$ because $2\le k/2$.

In the complement, every vertex of $A\setminus\{u\}$ has neighbors only in $A$, and every vertex of $P$ has neighbors only in $B$. Such two vertices cannot lie on the same side of a majority partition, by the same incompatible color-count requirements. Hence all $A\setminus\{u\}$ lie on one side and both $P$ vertices on the other. Each former vertex has at most $u$ as a cross neighbor. If $u$ is across, that side has at least three vertices; otherwise there is no cross neighbor. Neither possibility is a strict majority.

For the natural partition, $M$ is a star with center $u$ and leaves $Z$. The diagonal entries of $C$ are
\[
a_u=3k-4,\quad a_v=2k^2-6k+5\ (v\in Z),\quad
a_v=2(k-1)^2\text{ otherwise};
\]
its star off-diagonals are $-(2k-1)$. Use the positive integer witness
\[
z_u=4k-7,\qquad z_v=5\ (v\in Z),\qquad z_v=1\text{ otherwise}.
\]
Direct multiplication gives residual $2(k-3)^2$ on the star and $2(k-1)^2$ elsewhere. The graph degrees are $2$ at $u$, $k-1$ on $Z$, and $k$ elsewhere. Consequently
\[
\tau(z)=\frac{(k-3)^2}{4k-7}>0:
\]
the center ratio is at most the leaf ratio because $5(k-1)\le2(4k-7)$, and is smaller than the other ratios. Proposition 6 proves (11). Its last strict inequality follows from
$8(k^2+2k-5)-(4k-7)(2k-1)=34k-47>0$. $\square$

The witness is nonconstant already at order eight: it assigns $9$ to the exceptional vertex, $5$ to the two missing neighbors and $1$ elsewhere. The pointwise deficit grows without bound with $k$, while the certificate supplies a constant lower bound. Because $C$ depends only on the cross pairs, its positive definiteness also certifies the threshold after arbitrary internal edges are added. The absence of majority partitions is asserted only for the bipartite family just proved.

The family itself has an elementary spectrum, which clarifies the role of the example. Its normalized bipartite adjacency block has rank two and squared Frobenius norm $1+(k-2)/k^2$; one singular value is $1$. Therefore
\[
\operatorname{spec}(\mathcal L(H_k))=
\left\{0,2,1-\frac{\sqrt{k-2}}k,1+\frac{\sqrt{k-2}}k,
1^{[2k-4]}\right\}.
\tag{12}
\]
The actual gap tends to $1$, whereas the certificate in (11) tends to $1/8$. This example proves additional certificate coverage, not a new universal Nordhaus–Gaddum constant or a sharp estimate for these individual graphs.

## 5. Exact pendant reduction

Let $H$ be a connected graph on $N\ge3$ vertices, let $u\in V(H)$, and attach a new vertex $h$ only to $u$, giving $K$. Put $W=\sum_vd_v$, $c(g)=W^{-1}\sum_vd_vg_v$ and
\[
C_{N,W}=\frac{4(N-1)W}{(N-2)W+2(N-1)}.
\]

**Theorem 8 (exact criterion).** The following are equivalent:
\[
\lambda_2(K)\ge2/N;
\qquad
N E_H(g)-2V_H(g)-C_{N,W}(g_u-c(g))^2\ge0
\quad\text{for every }g.
\tag{13}
\]

*Proof.* Shift $g$ and the value $t$ at $h$ by $c(g)$, and write $a=g_u-c(g)$, $z=t-c(g)$. The exact weighted variance in $K$ is
\[
V_K=V_H+z^2+a^2-\frac{(z+a)^2}{W+2}.
\]
Thus
\[
N E_K-2V_K=N E_H-2V_H
+N(z-a)^2-2z^2-2a^2+\frac{2(z+a)^2}{W+2}.
\]
The coefficient of $z^2$ is $A=N-2+2/(W+2)>0$. Completing the square gives
\[
N E_K-2V_K
=N E_H-2V_H-C_{N,W}a^2
+A\left(z-\frac{N-2/(W+2)}{A}a\right)^2.
\tag{14}
\]
Minimize over $z$. Nonnegativity for all $(t,g)$ is therefore equivalent to the second condition in (13), and the variational formula proves the theorem. $\square$

The coefficient satisfies $C_{N,W}<4(N-1)/(N-2)$; retaining the optimizing mean is essential for the equivalence. This reduction alone does not settle the degree-$(n-2)$ branch of (1): one still needs an implication from a small gap in the complementary graph to the quadratic-form condition. Its use is not restricted to complete bipartite bases, whose pendant spectra admit the direct calculation below.

**Corollary 9 (complete bipartite base).** If $a,b\ge2$, attaching a pendant vertex anywhere to $K_{a,b}$ gives
\[
\lambda_2(K)>\frac2{a+b}.
\tag{15}
\]

*Proof.* More generally, suppose the attachment vertex lies in the $a$-part, with $a\ge2$ and $b\ge1$. The graph remains bipartite, with parts of sizes $a$ and $b+1$. Its normalized adjacency matrix has the block form
\[
D^{-1/2}AD^{-1/2}=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}.
\]
The block $B$ has rank two: the attachment vertex and the other $a-1$ vertices give two independent row types. Connectedness gives one singular value equal to $1$, and
\[
\|B\|_F^2=\frac{b}{a(b+1)}+\frac{a-1}{a}+\frac1{b+1}
=1+\frac{a-1}{a(b+1)}.
\]
Here $\|B\|_F^2$ is the sum of squared entries. Thus the other singular value is $r=\sqrt{(a-1)/(a(b+1))}$, and the complete normalized-Laplacian spectrum is
\[
0,\quad 2,\quad 1-r,\quad 1+r,\quad
1\text{ with multiplicity }a+b-3.
\tag{16}
\]
In particular $\lambda_2(K)=1-r$. If $a,b\ge2$ and $a+b\ge5$, then $r<1/\sqrt3$ and hence $\lambda_2>1-1/\sqrt3>2/5\ge2/(a+b)$. For $a=b=2$, the gap is $1-1/\sqrt6>1/2$. $\square$

The same calculation classifies singleton parts. For $a=1$ the graph is a star and its gap is $1$. If $b=1$ and $N=a+1\ge4$, comparison of $1-\sqrt{(a-1)/(2a)}$ with $2/(a+1)$ gives strict inequality above the threshold exactly when $a^2-4a-1>0$. Therefore $a=3,4$ give a gap below the threshold, and $a\ge5$ give a gap above it. There is no equality for these integer parameters.

For $a,b\ge2$, Corollary 9 also settles (1) for the family $G=(K_1\vee(K_a+K_b))-hu$, where $h$ is the hub and $u$ is a clique vertex. Its complement is precisely $K_{a,b}$ with a leaf at $u$. No assertion about $G$ itself being below the threshold is needed.

Arbitrary joins with a pendant need not satisfy the bound. An exact counterexample starts with $K_1\vee(K_2+K_2)$ and attaches the leaf to a clique vertex. Give the attachment clique value $1$, the other clique value $-1$, the hub value zero, and the leaf value $17/11$. Here $N=5$, $W=12$, $E_H=4$, $V_H=8$, and (14) gives $5E_K-2V_K=-4/11<0$. By contrast, attachment to the universal hub retains a cone and always satisfies Theorem 2.

## 6. Supporting eigenfunction identities

Let $H$ be connected of order $n\ge3$, let $\lambda=\lambda_2(H)>0$, and let $x$ be a nonzero generalized Fiedler eigenfunction, satisfying $Lx=\lambda Dx$, rather than an untransformed eigenvector of $\mathcal L$. If $\phi$ is the latter, $x=D^{-1/2}\phi$. At its maximum and minimum write $x_p=a>0$, $x_q=-b<0$.

If $p\sim q$, the endpoint equations give $a+b\le\lambda d_pa$ and $a+b\le\lambda d_qb$, and hence
\[
\lambda\ge d_p^{-1}+d_q^{-1}.
\]
If $p,q$ are nonadjacent with $k\ge1$ common neighbors, summing the two endpoint equations over those neighbors gives
\[
\lambda\ge\frac{k(a+b)}{d_pa+d_qb}\ge\frac{k}{\max(d_p,d_q)}.
\]
Consequently $\lambda<2/(n-1)$ forces nonadjacent extremes with at most one common neighbor. If there is exactly one, then $d_p+d_q\le n-1$, exactly one endpoint degree exceeds $(n-1)/2$, and that endpoint has larger absolute eigenfunction value. The latter follows by rearranging $(n-1)(a+b)<2(d_pa+d_qb)$. This is an elementary local obstruction, not a solution of the distance-three case.

For the sign cut $S=\{x>0\}$, $T=\{x\le0\}$, let $m_u$ now denote the number of graph edges across that cut. Summing $Lx=\lambda Dx$ over $S$ proves the exact identity
\[
\sum_um_u|x_u|=\frac\lambda2\sum_ud_u|x_u|.
\tag{17}
\]
Thus the average of $m_u/d_u$ uses weights $d_u|x_u|$, and equals $\lambda/2$. The average of $m_u$ with weights $|x_u|$ is at most $\lambda\Delta/2$. When $\lambda<2/(n-1)$ and the complement is connected it is strictly below $\Delta/(n-1)<1$. Even this stronger average does not give a vertexwise partition condition: vertices of very small eigenfunction value may violate it.

## 7. Evidence and unresolved scope

The computational supplement tests the equivalent integer-matrix condition
\[
Q_H=w_H\big((n-1)L_H-2D_H\big)+2dd^\mathsf T\succeq0
\tag{18}
\]
for connected graphs. Since $Q_H\mathbf1=0$, it suffices to test the principal submatrix obtained by deleting one row and column: subtracting the last coordinate from a vector leaves its quadratic value unchanged. Fraction-free Schur elimination with exact divisibility checks tests positive semidefiniteness and rank, without eigensolver tolerances. For a PSD matrix, a rank deficit beyond the constant vector identifies equality. Enumeration counts, commands and graph-stream hashes are recorded in `verification/enumeration-normal.json`.

The exact finite checks do not determine the large-order behavior. Theorem 2 leaves graphs with no qualifying partition untreated. The exact pendant criterion is a reduction, and (17) does not supply the missing pointwise control. The diameter-two conjecture together with the remaining diameter-three pair case would imply (1), but the reverse implication is not established: (1) can be certified by the complement instead of the diameter-two graph itself.

All unlabeled graphs of orders 5 through 9 were tested. The table reports the number of graphs and the equality counts for (1) and for the diameter-at-most-two bound $\lambda_2\ge2/(n-1)$.

| Order | All graphs | Both connected | Diameter at most two | Equality in (1) | Diameter-two equality |
|---|---:|---:|---:|---:|---:|
| 5 | 34 | 8 | 15 | 2 | 1 |
| 6 | 156 | 68 | 60 | 0 | 0 |
| 7 | 1,044 | 662 | 374 | 2 | 1 |
| 8 | 12,346 | 9,888 | 4,155 | 0 | 0 |
| 9 | 274,668 | 247,492 | 91,519 | 2 | 1 |

The total is 288,248 graphs. Both inequalities and their stated equality classifications pass. Separately, every one of 72,677 listed order-10 candidate graphs was checked exactly: each is below $2/9$ and its complement is strictly above it. This verifies the listed candidates, not completeness of their selection. Reported exhaustive floating-point searches at orders 10 and 11 are not used as exact exclusions here.

**Reproducibility.** The source repository and versioned archive named above contain `verification/exact_small_graphs.py`, `verification/audit_recorded_candidates.py`, `verification/data/n10_small.g6`, and the exact receipts. The release scripts use explicit exceptions for load-bearing validation and work under both ordinary and optimized Python. They use the Python standard library and nauty's `geng` generator [7]; the independent symbolic checks additionally require SymPy. From the `verification/` directory run:

```sh
python3 self_test.py
python3 review_checks.py
python3 exact_small_graphs.py --max-n 9 > replay-enumeration.json
python3 audit_recorded_candidates.py > replay-candidates.json
```

The same commands with `python3 -O` were also run successfully. Each mode passed 25 semantic controls, 600 independently implemented exact PSD comparisons and two symbolic checks, all 288,248 enumerated graphs, and all 72,677 packaged candidates. The independent principal-minor oracle checks PSD decisions, not the rank returned by the enumeration kernel. Full commands, assumptions and receipts are documented in `verification/README.md`, `verification/release-assurance.json` and `COMPUTATIONAL_ASSURANCE.md`.

The recorded interpreter was Python 3.14.7. The generator was invoked as `geng -q n`; an alternative executable can be supplied using `--geng`. Its SHA-256 identifier is

```text
ad2f68adf733dbed7cad543841cfa329740596ee5cd136f17a0a17f6e744f5ad
```

The enumeration receipts include a SHA-256 hash of each complete graph6 stream. Normal and optimized runs match the scientific counts and stream hashes. Enumeration trusts nauty's isomorphism-class generation; these checks are not a second independent implementation of the complete enumeration. Rerun times and stream order may change with the software environment. Candidate validation does not prove completeness of the candidate selection.

**Weighted-class comparison.** An exact search through order eight examined every partition of each connected graph lacking a strict-majority partition. The counts are:

| Order | Connected graphs | No majority partition | Weighted certificate found |
|---|---:|---:|---:|
| 5 | 21 | 8 | 0 |
| 6 | 112 | 46 | 0 |
| 7 | 853 | 530 | 0 |
| 8 | 11,117 | 6,612 | 441 |

Of the 441 order-eight examples, 338 also have no majority partition in the complement. The saved certificates include the graph6 encoding, a partition and a positive rational witness. The portable checker reconstructs the matrix, checks the residual exactly and tests every partition for the claimed exclusions; this replay requires no graph generator. The finite search illustrates the separation proved for all orders in Theorem 7, rather than proving that theorem.

From `verification/weighted/`, run `python3 verify_certificates.py` and `python3 check_family.py`, or their `python3 -O` counterparts. The files `weighted-certificates.json`, `replay.json`, `replay-optimized.json`, `family-normal.json` and `family-optimized.json` record these checks. `README.md` gives the optional discovery command and its nauty dependency. Family checks cover integer parameters 4 through 100 and all-partition exclusions at 4 through 6; the proof of Theorem 7 supplies the unrestricted parameter range. The separate `check_parity.py` script and `parity-normal.json`/`parity-optimized.json` receipts verify the uniform bound in Proposition 4 for every qualifying connected graph of orders 4 through 7, covering all three parity cases.

Write $\mu_2$ for the second-smallest eigenvalue of the combinatorial Laplacian. The combinatorial-Laplacian theorem of Einollahzadeh–Karkhaneei [3] and the comparison $\lambda_2(H)\ge\mu_2(H)/\Delta(H)$ yield
\[
\lambda_2(G)+\lambda_2(\overline G)\ge\frac1{n-2}
\]
when both graphs are connected, and their asymptotic maximum estimate transfers to $(1-O(n^{-1/3}))/(n-2)$. These are corollaries of prior work and remain weaker than the target constant. No improved universal constant or complete resolution is claimed here.

## References

1. J. Nolan Faught, Mark Kempton and Adam Knudson. *A Nordhaus–Gaddum type problem for the normalized Laplacian spectrum and graph Cheeger constant*. Applied Mathematics and Computation **480** (2024), 128920. [arXiv:2304.01979](https://arxiv.org/abs/2304.01979).
2. Sooyeong Kim and Neal Madras. *A Nordhaus–Gaddum Problem for the Spectral Gap of a Graph*. Journal of Graph Theory **110** (2025), 132–144. [arXiv:2404.15167](https://arxiv.org/abs/2404.15167), [doi:10.1002/jgt.23253](https://doi.org/10.1002/jgt.23253). Numbering here refers to arXiv v2.
3. Mostafa Einollahzadeh and Mohammad Mahdi Karkhaneei. *On the lower bound of the sum of the algebraic connectivity of a graph and its complement*. Journal of Combinatorial Theory, Series B **151** (2021), 235–249. [arXiv:1901.02047](https://arxiv.org/abs/1901.02047).
4. Wei Li, Wensheng Sun and Yujun Yang. *On two conjectures concerning Kemeny's constant of graphs*. [arXiv:2608.08797v2](https://arxiv.org/abs/2608.08797), 2026. This concerns Kemeny's constant and does not establish (1).
5. Mark Kempton, Xavier Zaitzeff and Sibi Muthuprakash. *Nordhaus–Gaddum upper bounds for graph connectivity parameters*. [arXiv:2606.12751](https://arxiv.org/abs/2606.12751), 2026.
6. Erik G. Boman, Doron Chen, Ojas Parekh and Sivan Toledo. *On factor width and symmetric H-matrices*. Linear Algebra and Its Applications **405** (2005), 239–248. [doi:10.1016/j.laa.2005.03.029](https://doi.org/10.1016/j.laa.2005.03.029).
7. Brendan D. McKay and Adolfo Piperno. *Practical graph isomorphism, II*. Journal of Symbolic Computation **60** (2014), 94–112. [doi:10.1016/j.jsc.2013.09.003](https://doi.org/10.1016/j.jsc.2013.09.003). Software: [nauty and Traces](https://pallini.di.uniroma1.it/).

8. Matthias Keller, Yehuda Pinchover and Felix Pogorzelski. *Criticality theory for Schrödinger operators on graphs*. Journal of Spectral Theory **10** (2020), no. 1, 73–114. [doi:10.4171/JST/286](https://doi.org/10.4171/JST/286). The ground-state transformation is Proposition 4.8.

## License

This article is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Cited publications and third-party software retain their respective rights and licenses.
