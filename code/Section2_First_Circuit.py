#!/usr/bin/env python3
"""
Section 2 – First Quantum Circuit with Qiskit

Creates a single‑qubit circuit (|0⟩ → X → |1⟩) and measures it.
"""
from qiskit import QuantumCircuit, Aer, execute

def build_circuit():
    qc = QuantumCircuit(1, 1)
    qc.x(0)          # Apply Pauli‑X gate
    qc.measure(0, 0) # Measure qubit into classical bit
    return qc

def main(shots=1024):
    qc = build_circuit()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=shots)
    counts = job.result().get_counts()
    print("Circuit:")
    print(qc)
    print(f"Results for {shots} shots:", counts)

if __name__ == "__main__":
    main()
