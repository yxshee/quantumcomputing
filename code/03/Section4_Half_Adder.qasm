OPENQASM 2.0;
include "qelib1.inc";
// Half‑Adder using CNOT (XOR) and Toffoli (AND)
// Inputs: q0 (A), q1 (B)
// Outputs: q2 (Sum = A ⊕ B), q3 (Carry = A ∧ B)
qreg q[4];
creg c[4];

// Prepare inputs here if desired, e.g. x q[0];   // set A=1

// Sum (XOR)
cx  q[0], q[2];
cx  q[1], q[2];

// Carry (AND)
ccx q[0], q[1], q[3];

measure q[0] -> c[0];   // Optional: read back A
measure q[1] -> c[1];   // Optional: read back B
measure q[2] -> c[2];   // Sum output
measure q[3] -> c[3];   // Carry output
