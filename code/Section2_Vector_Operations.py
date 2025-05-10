#!/usr/bin/env python3
"""
Section 2 – Vector Operations

Functions:
• read_vector() – read vector from keyboard (space‑separated floats).
• is_normalized(vec)
• dot_product(a, b)
• cross_product(a, b)
• unit_vector(a)
"""
import numpy as np

def read_vector(prompt="Enter vector elements separated by space: "):
    values = list(map(float, input(prompt).split()))
    return np.array(values)

def is_normalized(vec, tol=1e-9):
    return abs(np.dot(vec, vec) - 1.0) < tol

def dot_product(a, b):
    return np.dot(a, b)

def cross_product(a, b):
    if a.size != 3 or b.size != 3:
        raise ValueError("Cross product is defined for 3‑D vectors.")
    return np.cross(a, b)

def unit_vector(a):
    norm = np.linalg.norm(a)
    if norm == 0:
        raise ValueError("Zero vector has no direction.")
    return a / norm

def demo():
    print("Vector A:")
    A = read_vector()
    print("Vector B:")
    B = read_vector()

    print("\n--- Results ---")
    print("A is normalized:", is_normalized(A))
    print("B is normalized:", is_normalized(B))
    print("Dot product A·B:", dot_product(A, B))
    try:
        print("Cross product A×B:", cross_product(A, B))
    except ValueError as e:
        print(e)
    print("Unit vector of A:", unit_vector(A))

if __name__ == "__main__":
    demo()
