#!/usr/bin/env python3
"""
Section 1 – Vector Basics

This script demonstrates basic vector operations requested in Assignment 1.
"""
import numpy as np
import math

def main():
    # Variables
    a = 1 / math.sqrt(2)
    b = 1 / math.sqrt(2)

    # Vector creation
    v = np.array([a, b])

    # Normalization check
    is_normalized = math.isclose(a**2 + b**2, 1.0, abs_tol=1e-9)

    # Length (magnitude)
    length = np.linalg.norm(v)

    print(f"Vector v: {v}")
    print(f"Is normalized? {is_normalized}")
    print(f"Length of v: {length:.6f}")

if __name__ == "__main__":
    main()
