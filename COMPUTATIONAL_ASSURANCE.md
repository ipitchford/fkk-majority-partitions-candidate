# Computational assurance

The release verifier lives in `verification/`. Original verifier scripts remain
unchanged in the source workspace and are preserved byte-for-byte in
`verification/originals/`. Release scripts use explicit exceptions for
load-bearing validation, so optimisation (`python3 -O`) cannot remove their
scientific checks. This is a bounded computational assurance record, not a proof
of the conjecture at arbitrary order.

## Changes

- Replaced all assertion-based acceptance checks with explicit guards, including
  exact division, conjecture acceptance, equality classification, generator exit,
  candidate uniqueness, candidate order and candidate count.
- Validated graph6 byte type, nonempty input, supported single-byte orders 2–62,
  character range, encoded length and zero padding. Extended graph6 and headers
  are intentionally unsupported, rather than silently misdecoded.
- Factored scientific outcome validation into one function used both by the
  enumeration loop and semantic negative controls.
- Made the generator executable portable (`geng` on PATH, overridable with
  `--geng`) and packaged only graph6 candidate/minimizer data needed by the audit.
  Floating-point columns and original archive contents are not required.
- Added provenance hashes for the input extraction and separate self-tests.

## Checks and receipts

All commands below run from `verification/`; add an explicit `--geng` path if the
external nauty binary is not on PATH. The recorded execution used the installed
Homebrew nauty binary. Two concurrent processes were used at most.

| Command (run once normally and once with `-O`) | Receipt files | Scope |
|---|---|---|
| `python3 self_test.py` | `self-test-normal.json`, `self-test-optimized.json` | 25 semantic positive/negative controls |
| `python3 review_checks.py` | `independent-checks-normal.json`, `independent-checks-optimized.json` | 600 independent exact PSD comparisons; two symbolic identities |
| `python3 exact_small_graphs.py --max-n 9` | `enumeration-normal.json`, `enumeration-optimized.json` | All 288,248 unlabeled graphs of orders 5–9 |
| `python3 audit_recorded_candidates.py` | `candidates-normal.json`, `candidates-optimized.json` | All 72,677 included candidates and seven recorded minimizers |

The self-tests require rejection of malformed graph6, indefinite matrices with
zero or positive diagonal, a connected P5 below threshold, falsely accepted
equality classifications, flipped spectral decisions, and sign/threshold
mutations of the defining quadratic form. Exact hub-and-two-cliques equality and
strict positivity for K5 are positive controls. These are semantic controls, not
an exhaustive mutation-testing campaign.

The separate Fraction oracle computes principal-minor determinants and compares
PSD decisions against the fraction-free routine on deterministic symmetric
integer and Gram matrices. It does not independently compare the returned rank.
SymPy checks the pendant Schur coefficient and bipartite polynomial equivalence
by exact zero residuals. Both normal and optimised runs pass. The enumeration
receipts match each other and the historical scientific counts and graph-stream
hashes exactly. The packaged candidate data omit numerical estimates: every
listed graph is decided using integer arithmetic, and its complement must be
strictly above threshold.

## Limits

Nauty remains a trusted enumeration dependency; this is not an independent
isomorphism-class generator. Re-execution of a hardened version of the same
scientific algorithm is not wholly independent implementation of the spectral
checker. No full order-10 or order-11 enumeration was performed here. Candidate
validation does not prove the completeness of the historical candidate selection.
The data provenance record retains the source-file hash and extraction rule;
raw archive histories are not bundled. The handwritten proofs remain the basis
for the infinite structural classes.
