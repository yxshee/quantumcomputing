# Assignment 5 – Single‑Qubit Gate Experiments (Qiskit)

**Sections & Files**

| File | Section | Gate |
|------|---------|------|
| `Section1_XGate.py` | 1 | X |
| `Section2_YGate.py` | 2 | Y |
| `Section3_ZGate.py` | 3 | Z |
| `Section4_SGate.py` | 4 | S (Phase) |
| `Section5_TGate.py` | 5 | T |
| `Section6_SdgGate.py` | 6a | S† |
| `Section6_TdgGate.py` | 6b | T† |
| `Section7_U_Gate_Values.py` | 7 | U‑gate parameters |

Each script:

1. Starts from three base states (|0⟩, |1⟩, |+⟩).
2. Applies the specified single‑qubit gate.
3. Prints the ASCII circuit, state vector, and Bloch‑vector coordinates.
4. Optionally opens a Bloch‑sphere graphic if GUI is available.

## Dependencies

```bash
pip install qiskit matplotlib
```

## Quickstart

```bash
python Section1_XGate.py
```

Run any other section by changing the filename.
