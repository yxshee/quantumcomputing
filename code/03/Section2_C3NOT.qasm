OPENQASM 2.0;
include "qelib1.inc";
// 4‑qubit controlled NOT (three controls) using two Toffoli gates
// Controls: q0, q1, q2   Target: q3   Ancilla: q4
qreg q[5];
creg c[4];   // Classical bits for the four logical qubits (ancilla un‑measured)

// -- BEGIN C3X (q0,q1,q2 -> q3) --
ccx q[0], q[1], q[4];    // Toffoli #1: store (q0 AND q1) in ancilla q4
ccx q[4], q[2], q[3];    // Toffoli #2: if (q0∧q1)∧q2 then flip target q3
ccx q[0], q[1], q[4];    // Uncompute ancilla to reset
// -- END C3X --

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
