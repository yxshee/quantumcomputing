#!/usr/bin/env python3
"""Section 7 – U(θ, φ, λ) parameter lookup for standard gates.

Prints (θ, φ, λ) in radians for gates X, Y, Z, H, S, T, S†, T† and verifies
by comparing statevectors of U(θ, φ, λ) with library gates on |0⟩.
"""
import json
from math import pi, isclose
from qiskit import QuantumCircuit, Aer
from qiskit.quantum_info import Statevector

# Parameter table (derivable from textbook / qiskit)
params = {
    'X':  (pi, 0, pi),
    'Y':  (pi, pi/2, pi/2),
    'Z':  (0, 0, pi),
    'H':  (pi/2, 0, pi),
    'S':  (pi/2, 0, pi/2),
    'T':  (pi/4, 0, pi/4),
    'Sdg':(-pi/2, 0, -pi/2),
    'Tdg':(-pi/4, 0, -pi/4),
}

def gate_from_label(label):
    qc = QuantumCircuit(1)
    getattr(qc, label.lower())(0) if label not in ['Sdg','Tdg'] else getattr(qc, label.lower())(0)
    return Statevector.from_instruction(qc)

def u_equivalent(theta, phi, lam):
    qc = QuantumCircuit(1)
    qc.u(theta, phi, lam, 0)
    return Statevector.from_instruction(qc)

def main():
    print(json.dumps({k: [float(x) for x in v] for k,v in params.items()}, indent=2))
    for gate, (t, p, l) in params.items():
        sv_gate = gate_from_label(gate)
        sv_u = u_equivalent(t, p, l)
        if not Statevector(sv_gate).equiv(sv_u):
            print(f"Mismatch for {gate}!")
            return
    print("✔ All parameter sets verified against Qiskit library gates.")

if __name__ == '__main__':
    main()
