#!/usr/bin/env python3
"""Section 3b – Phase Kickback with T‑Gate (Qiskit demo)

Demonstrates that applying a controlled‑T (on ancilla) transfers the phase
to the control qubit when ancilla is |+⟩.
"""
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import math

def kickback_circuit():
    qc = QuantumCircuit(2, 2)
    # Prepare |+⟩ on ancilla q1 and |1⟩ on control q0 to see phase effect
    qc.x(0)
    qc.h(1)
    # Controlled‑T with control q0, target q1
    qc.ct(0, 1)
    # Transform ancilla back with H to observe phase in measurement
    qc.h(1)
    qc.measure([0,1], [0,1])
    return qc

def run():
    backend = Aer.get_backend('qasm_simulator')
    qc = kickback_circuit()
    counts = execute(qc, backend, shots=1024).result().get_counts()
    print("Kickback measurement counts:", counts)
if __name__ == "__main__":
    run()
