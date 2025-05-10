#!/usr/bin/env python3
"""
Section 5 – Hadamard Gate on Four Qubits

Constructs a 4‑qubit circuit where each qubit is placed in equal superposition
(|+⟩) using a Hadamard gate, then measures the outcome distribution over 1024
shots.
"""
from qiskit import QuantumCircuit, Aer, execute

def build_circuit():
    qc = QuantumCircuit(4, 4)
    qc.h(range(4))   # Apply H on all qubits
    qc.measure(range(4), range(4))
    return qc

def main(shots=1024):
    qc = build_circuit()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=shots)
    counts = job.result().get_counts()
    print("Circuit:")
    print(qc.draw())
    print(f"Results for {shots} shots:", counts)

if __name__ == "__main__":
    main()
