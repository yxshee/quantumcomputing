# Assignment 4 – QASM + Qiskit Code Bundle

**Sections**

| File | Section | Description |
|------|---------|-------------|
| `Section1_Fredkin_AND.qasm` | 1 | Fredkin (CSWAP) gate behaving as classical AND. |
| `Section2_Fredkin_NOT.qasm` | 2 | Fredkin gate configured as NOT via constant controls. |
| `Section3_Fredkin_SelfInverse.qasm` | 3 | Proves CSWAP is self‑inverse. |
| `Section4_Identity_X2.qasm`, `Y2.qasm`, `Z2.qasm` | 4.1 | Verify Pauli squares equal identity. |
| `Section4_Identity_HZH.qasm` | 4.2 | Verify X = HZH. |
| `Section4_Identity_HXH.qasm` | 4.3 | Verify Z = HXH. |
| `Section4_Identity_T2.qasm` | 4.4 | Verify S = T². |
| `Section4_Identity_XYX.qasm` | 4.5 | Verify −iY = XYX (global phase ignored). |
| `Section5_StateVectors.py` | 5 | Builds two different states with Pr(|0⟩)=1/3, validates Pr(|1⟩)=2/3. |

## Requirements

```bash
pip install qiskit numpy
```

## Usage Examples

```bash
# Run state‑vector verification
python Section5_StateVectors.py

# Simulate a QASM circuit (example):
from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit.from_qasm_file('Section1_Fredkin_AND.qasm')
counts = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
print(counts)
```
