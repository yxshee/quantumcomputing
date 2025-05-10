#!/usr/bin/env python3
"""
Section 2 – First Quantum Circuit with Qiskit

Creates a single‑qubit circuit (|0⟩ → X → |1⟩) and measures it.
"""
# Add import check for qiskit
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit.providers.aer import AerSimulator
except ImportError:
    print("qiskit is not installed. Please install it with `pip install qiskit`.")
    exit(1)

def build_circuit():
    qc = QuantumCircuit(1, 1)
    qc.x(0)          # Apply Pauli‑X gate
    qc.measure(0, 0) # Measure qubit into classical bit
    return qc

def main(shots=1024):
    qc = build_circuit()
    simulator = AerSimulator()
    qc = transpile(qc, simulator)
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    print("Circuit:")
    print(qc)
    print(f"Results for {shots} shots:", counts)

if __name__ == "__main__":
    main()
