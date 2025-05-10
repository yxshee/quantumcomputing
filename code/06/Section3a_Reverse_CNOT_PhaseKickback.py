#!/usr/bin/env python3
"""Section 3a – Reverse CNOT via Phase Kickback (Qiskit demo)

Implements a CNOT where the target and control roles are reversed using
an H‑gate conjugation: CX_{1→0} = H₀ CX_{0→1} H₀.
Verifies truth‑table equivalence.
"""
from qiskit import QuantumCircuit, Aer, execute

def reverse_cnot_circuit(control: int, target: int):
    qc = QuantumCircuit(2, 2)
    # Prepare basis state |control target⟩
    if control:
        qc.x(1)  # original control q1
    if target:
        qc.x(0)  # original target q0
    # Reverse CNOT using phase‑kickback trick
    qc.h(0)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0,1], [0,1])
    return qc

def run():
    backend = Aer.get_backend('qasm_simulator')
    for ctrl in [0,1]:
        for targ in [0,1]:
            qc = reverse_cnot_circuit(ctrl, targ)
            counts = execute(qc, backend, shots=1024).result().get_counts()
            print(f"Input ({ctrl}{targ}) → counts {counts}")
if __name__ == "__main__":
    run()
