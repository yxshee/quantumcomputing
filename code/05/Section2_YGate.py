#!/usr/bin/env python3
"""Section 2 – Y‑Gate demonstration on |0⟩, |1⟩, and |+⟩."""
from math import sqrt
from qiskit import QuantumCircuit, Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

def bloch(sv):
    rho = sv.data.reshape(2,1) @ sv.data.conj().reshape(1,2)
    return (2*rho[0,1].real, 2*rho[1,0].imag, rho[0,0].real - rho[1,1].real)

def demo(sv, label):
    qc = QuantumCircuit(1)
    qc.initialize(sv.data, 0)
    qc.y(0)
    print(f"\n=== Y‑Gate on {label} ===")
    print(qc.draw())
    final_sv = Statevector.from_instruction(qc)
    print("Statevector:", final_sv)
    vec = bloch(final_sv)
    print("Bloch vector:", vec)
    try:
        plot_bloch_vector(vec, title=f"Y on {label}")
        plt.show()
    except Exception:
        pass

if __name__ == '__main__':
    states = {
        '|0>': Statevector([1,0]),
        '|1>': Statevector([0,1]),
        '|+>': Statevector([1/sqrt(2), 1/sqrt(2)]),
    }
    for lbl, sv in states.items():
        demo(sv, lbl)
