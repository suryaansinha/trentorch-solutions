import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    arr = np.asarray(x, dtype=float)
    norm = np.linalg.norm(arr)

    if norm == 0:
        raise ValueError("Cannot noramalise Zero Vector.")

    return arr/norm
