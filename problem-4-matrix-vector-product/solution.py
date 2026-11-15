import numpy as np


def solve(A, x):
    """Implement Matrix-Vector Product from the mathematical contract in README.md."""
    A = np.asarray(A, dtype=float)
    x = np.asarray(x, dtype=float)
    return np.array([np.dot(row, x) for row in A])
