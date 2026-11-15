import numpy as np

def solve(coeffs):
    """Solve the system a*x + b*y = e and c*x + d*y = f, where coeffs is [a,b,c,d,e,f]. A singular system raises ValueError."""
    a, b, c, d, e, f = coeffs
    det = a*d - b*c
    if np.isclose(det, 0.0):
        raise ValueError("Singular Systems: No unique Solutions")
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det
    return np.array([x, y])
