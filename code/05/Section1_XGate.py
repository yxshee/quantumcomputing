#!/usr/bin/env python3
"""Section 1 – X‑Gate demonstration on |0⟩, |1⟩, and |+⟩.

The script:
1. Builds a 1‑qubit circuit.
2. Applies X.
3. Draws the circuit (text).
4. Prints Bloch‑sphere vector & statevector.

Requires: qiskit, matplotlib (optional for Bloch plot).
"""
from math import sqrt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

def bloch_from_sv(sv):
    """Return Bloch‑vector components (x,y,z) from a Statevector."""
    rho = sv.data.reshape(2,1) @ sv.data.conj().reshape(1,2)  # |ψ><ψ|
    x = 2* (rho[0,1].real)
    y = 2* (rho[1,0].imag)
    z =   (rho[0,0].real - rho[1,1].real)
    return (x, y, z)

def demo(initial_sv, label):
    qc = QuantumCircuit(1)
    qc.initialize(initial_sv.data, 0)
    qc.x(0)
    print(f"\n=== X‑Gate on {label} ===")
    print(qc.draw())
    backend = Aer.get_backend('statevector_simulator')
    final_sv = Statevector.from_instruction(qc)
    print("Statevector:", final_sv)
    bloch = bloch_from_sv(final_sv)
    print("Bloch vector:", bloch)
    try:
        plot_bloch_vector(bloch, title=f"X on {label}")
        plt.show()
    except Exception:
        pass  # running headless

if __name__ == '__main__':
    states = {
        '|0>': Statevector([1,0]),
        '|1>': Statevector([0,1]),
        '|+>': Statevector([1/sqrt(2), 1/sqrt(2)]),
    }
    for lbl, sv in states.items():
        demo(sv, lbl)
