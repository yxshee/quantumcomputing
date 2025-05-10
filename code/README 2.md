# Assignment 2 – Code Bundle

This archive gathers code artefacts for each practical section of **Assignment 2 (Working with IBM Composer and qubit normalization)**.

| File | Section | Purpose |
|------|---------|---------|
| `Section2_First_Circuit.py` | 2 | Builds and simulates the very first one‑qubit circuit (X gate). |
| `Section3_Hadamard_Single_Shot.py` | 3 | Runs a Hadamard on one qubit and records 10 single‑shot outcomes. |
| `Section4_OpenQASM_Single_Qubit.qasm` | 4 | OpenQASM 2.0 for single qubit + Hadamard + measurement. |
| `Section4_OpenQASM_Four_Qubits.qasm` | 4 | OpenQASM 2.0 for four qubits each with a Hadamard gate. |
| `Section5_Hadamard_Four_Qubits.py` | 5 | Four‑qubit superposition circuit with measurement statistics. |
| `Section6_Complex_Number_Operations.py` | 6 | Converts complex numbers between Cartesian and polar forms. |

## Requirements

```bash
pip install qiskit
```

Only **Qiskit** (and Python standard library) are required. `cmath` is built‑in.

## Usage Quick‑Start

```bash
python Section2_First_Circuit.py
```
Replace the file name with any other script to explore additional sections.
