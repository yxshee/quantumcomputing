# Assignment 3 – QASM Code Bundle

This package contains Quantum Assembly (OpenQASM 2.0) implementations for every exercise in **Assignment 3 – Working with QASM**.

| File | Section | Description |
|------|---------|-------------|
| `Section1_BellState_psi1.qasm` – `psi4.qasm` | 1 | Bell states Φ⁺, Φ⁻, Ψ⁺, Ψ⁻ (2‑qubit). |
| `Section1_GHZState_psi5.qasm`, `psi6.qasm` | 1 | 3‑qubit GHZ states with ± phase. |
| `Section2_C3NOT.qasm` | 2 | Four‑qubit controlled‑NOT (three controls) built from two Toffoli gates and an ancilla. |
| `Section3_Toffoli_AND.qasm` | 3‑1 | Toffoli gate acting as a classical AND. |
| `Section3_Toffoli_NOT.qasm` | 3‑2 | Toffoli gate configured as a NOT gate via constant |1,1⟩ controls. |
| `Section4_Half_Adder.qasm` | 4 | Half‑adder producing **Sum** (XOR) and **Carry** (AND). |

## How to Run

1. Install Qiskit (Python >= 3.8 recommended):
   ```bash
   pip install qiskit
   ```
2. Load any `.qasm` file in **IBM Quantum Composer** or execute via `qasm_simulator`:
   ```python
   from qiskit import QuantumCircuit, Aer, execute

   qc = QuantumCircuit.from_qasm_file("Section4_Half_Adder.qasm")
   job = execute(qc, Aer.get_backend("qasm_simulator"), shots=1024)
   print(job.result().get_counts())
   ```

All circuits compile cleanly under the OpenQASM 2.0 specification and have been verified on the Qiskit simulator.
