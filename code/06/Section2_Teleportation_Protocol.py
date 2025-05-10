#!/usr/bin/env python3
"""Section 2 – Quantum Teleportation Protocol (Qiskit demo)

Teleports an arbitrary single‑qubit state |ψ⟩ from Alice (q0) to Bob (q2),
using an entangled pair (q1,q2) and classical communication.
"""
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
import numpy as np
from math import pi
import random

def create_random_state():
    """Return a random single‑qubit statevector."""
    theta = 2 * pi * random.random()
    phi   = 2 * pi * random.random()
    return Statevector([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)])

def teleport_state(state: Statevector):
    qc = QuantumCircuit(3, 2)  # q0: |ψ⟩, q1: Alice, q2: Bob

    # Initialise |ψ⟩
    qc.initialize(state.data, 0)

    # Prepare Bell pair between q1 and q2
    qc.h(1)
    qc.cx(1, 2)

    # Bell‑basis measurement on q0 & q1
    qc.cx(0, 1)
    qc.h(0)

    qc.measure(0, 0)  # classical bit c0
    qc.measure(1, 1)  # classical bit c1

    # Conditional operations on Bob's qubit
    # (added after measurement via classically controlled gates)
    qc.x(2).c_if(qc.clbits[1], 1)  # if c1 == 1
    qc.z(2).c_if(qc.clbits[0], 1)  # if c0 == 1

    return qc

def run():
    backend = Aer.get_backend('statevector_simulator')
    psi = create_random_state()
    print("Original |ψ⟩:", psi)

    qc = teleport_state(psi)
    final_sv = execute(qc.remove_final_measurements(inplace=False), backend).result().get_statevector()

    print("Teleported state on Bob (q2):", final_sv.partial_trace([0,1]))
if __name__ == "__main__":
    run()
