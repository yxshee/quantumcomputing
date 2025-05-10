#!/usr/bin/env python3
"""
Section 3 – Matrix Operations
"""
import numpy as np

def read_matrix():
    print("Enter matrix rows; separate numbers by space and press Enter. Blank line to finish:")
    rows = []
    while True:
        line = input()
        if not line.strip():
            break
        rows.append(list(map(float, line.split())))
    return np.array(rows)

def main():
    M = read_matrix()
    print("\nMatrix:\n", M)
    print("\nTranspose:\n", M.T)
    if M.shape[0] == M.shape[1]:
        print("\nDeterminant:", np.linalg.det(M))
        eigvals, eigvecs = np.linalg.eig(M)
        print("\nEigenvalues:", eigvals)
        print("Eigenvectors:\n", eigvecs)
        try:
            inv = np.linalg.inv(M)
            print("\nInverse:\n", inv)
        except np.linalg.LinAlgError:
            print("\nMatrix is singular; inverse not defined.")
    else:
        print("\nDeterminant/Eigenvalues/Eigenvectors/Inverse not applicable to non‑square matrices.")

    print("\nRank:", np.linalg.matrix_rank(M))
    print("Trace:", np.trace(M))

if __name__ == "__main__":
    main()
