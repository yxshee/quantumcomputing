#!/usr/bin/env python3
"""
Section 3 – Hadamard Gate Single‑Shot Experiment

Applies a Hadamard gate on a single qubit and executes 10 one‑shot runs to
illustrate the inherent randomness (0 or 1 with equal probability).
"""
from qiskit import QuantumCircuit, Aer, execute

def run_single_shot():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=1)
    counts = job.result().get_counts()
    return list(counts.keys())[0]  # '0' or '1'

def main():
    outcomes = [run_single_shot() for _ in range(10)]
    print("Single‑shot results:", " ".join(outcomes))

if __name__ == "__main__":
    main()
