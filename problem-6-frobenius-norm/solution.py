import numpy as np


def solve(A):
    return float(np.linalg.norm(A, 'fro'))
