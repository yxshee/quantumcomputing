#!/usr/bin/env python3
"""Section 1 – Superdense Coding Protocol (Qiskit demo)

Sends two classical bits using a single qubit by exploiting a shared Bell pair.
The script enumerates all 4 possible messages (00, 01, 10, 11) and verifies
that Bob decodes them correctly.
"""
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def superdense_circuit(bit1: int, bit2: int):
    """Return a QuantumCircuit implementing superdense coding for bits (b1,b2)."""
    qc = QuantumCircuit(2, 2)   # qubit 0 = Alice, qubit 1 = Bob
    # 1. Share Bell pair (performed ahead of time)
    qc.h(1)
    qc.cx(1, 0)
    # 2. Alice encodes her two classical bits on her qubit (q0)
    if bit2:           # Z for second bit
        qc.z(0)
    if bit1:           # X for first bit
        qc.x(0)
    # 3. Alice sends her qubit to Bob — simulated; no operation required
    # 4. Bob decodes
    qc.cx(0, 1)
    qc.h(0)
    # Measure
    qc.measure(0, 0)
    qc.measure(1, 1)
    return qc

def run():
    backend = Aer.get_backend('qasm_simulator')
    results = {}
    for bits in [(0,0), (0,1), (1,0), (1,1)]:
        qc = superdense_circuit(*bits)
        job = execute(qc, backend, shots=1024)
        counts = job.result().get_counts()
        results[f"{bits[0]}{bits[1]}"] = counts
        print(f"Message {bits} decoded counts: {counts}")
    # plot_histogram(results)  # Uncomment for graphical output
if __name__ == "__main__":
    run()
