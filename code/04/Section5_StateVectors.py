#!/usr/bin/env python3
"""
Section 5 – State‑vector tasks for Assignment 4.

1. Construct a state |ψ₁⟩ with Pr(|0⟩)=1/3.
2. Construct a different state |ψ₂⟩ with the same measurement probabilities.
3. Verify Pr(|1⟩)=2/3 for both states.

Uses Qiskit's Statevector class.
"""
from qiskit.quantum_info import Statevector
import numpy as np

def make_state(alpha: complex):
    """Return |ψ⟩ = α|0⟩ + β|1⟩ with |α|² = 1/3 (β chosen real ≥0)."""
    beta = np.sqrt(1 - abs(alpha)**2)
    return Statevector([alpha, beta])

def main():
    # State 1: α real, positive
    alpha1 = np.sqrt(1/3)
    sv1 = make_state(alpha1)

    # State 2: α with non‑zero phase (e^{iπ/3})
    alpha2 = alpha1 * np.exp(1j * np.pi/3)
    sv2 = make_state(alpha2)

    for idx, sv in enumerate([sv1, sv2], start=1):
        probs = sv.probabilities_dict()
        print(f"State {idx}: {sv}")
        print(f"Probabilities: {probs}\n")
        assert abs(probs['0'] - 1/3) < 1e-10, "|0⟩ prob not 1/3"
        assert abs(probs['1'] - 2/3) < 1e-10, "|1⟩ prob not 2/3"

    print("✔ Verified: Pr(|0⟩)=1/3 and Pr(|1⟩)=2/3 for both states.")

if __name__ == "__main__":
    main()
