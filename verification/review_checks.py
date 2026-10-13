#!/usr/bin/env python3
"""Bounded independent checks; run from any cwd with Python and SymPy.

This compares the supplied PSD routine with a separate exact principal-minor
criterion and checks two symbolic identities. It does not re-enumerate graphs.
"""
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys
from fractions import Fraction

import sympy as s

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from exact_small_graphs import psd_rank


def determinant(matrix):
    matrix = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for i in range(len(matrix)):
        k = next((j for j in range(i, len(matrix)) if matrix[j][i]), None)
        if k is None:
            return Fraction(0)
        if k != i:
            matrix[k], matrix[i] = matrix[i], matrix[k]
            result = -result
        pivot = matrix[i][i]
        result *= pivot
        for j in range(i + 1, len(matrix)):
            ratio = matrix[j][i] / pivot
            for column in range(i + 1, len(matrix)):
                matrix[j][column] -= ratio * matrix[i][column]
    return result


def main():
    rng = random.Random(130)
    cases = 0
    digest = hashlib.sha256()
    for n in range(1, 7):
        for trial in range(100):
            matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1):
                    matrix[i][j] = matrix[j][i] = rng.randrange(-4, 5)
            if trial % 2 == 0:
                matrix = [[sum(matrix[k][i] * matrix[k][j] for k in range(n))
                           for j in range(n)] for i in range(n)]
            digest.update((json.dumps(matrix, separators=(',', ':')) + '\n').encode())
            exact = all(
                determinant([[matrix[i][j] for j in indices] for i in indices]) >= 0
                for size in range(1, n + 1)
                for indices in itertools.combinations(range(n), size)
            )
            actual = psd_rank(matrix)[0]
            if actual != exact:
                raise AssertionError((n, trial, matrix, actual, exact))
            cases += 1

    N, W = s.symbols('N W', positive=True)
    A = N - 2 + 2 / (W + 2)
    B = N - 2 / (W + 2)
    C = 4 * (N - 1) * W / ((N - 2) * W + 2 * (N - 1))
    pendant = s.factor(A - B ** 2 / A + C)
    a, b = s.symbols('a b')
    N = a + b
    R = 1 / (4 * a * b * (N - 1)) + (a - 1) / (a * b * (N - 2))
    C = 4 * (N - 1) * 2 * a * b / ((N - 2) * 2 * a * b + 2 * (N - 1))
    D = (a * b + 1) * (N - 2) ** 2 - 4 * (a - 1) * (N - 1)
    bipartite = s.factor(1 - C * R - D / ((N - 2) * ((N - 2) * a * b + N - 1)))
    if pendant != 0 or bipartite != 0:
        raise AssertionError((pendant, bipartite))
    print(json.dumps({
        'status': 'pass', 'python_version': sys.version,
        'sympy_version': s.__version__, 'random_seed': 130,
        'matrix_orders': list(range(1, 7)), 'matrices_per_order': 100,
        'matrix_count': cases, 'matrix_stream_sha256': digest.hexdigest(),
        'oracle': 'Exact Fraction determinants of all principal minors; nonnegative iff PSD',
        'scope': 'PSD decisions only; does not independently compare returned ranks',
        'pendant_symbolic_residual': str(pendant),
        'bipartite_symbolic_residual': str(bipartite),
        'review_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'tested_checker_sha256': hashlib.sha256((ROOT / 'exact_small_graphs.py').read_bytes()).hexdigest(),
    }, indent=2))


if __name__ == '__main__':
    main()
