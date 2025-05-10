OPENQASM 2.0;
include "qelib1.inc";
// Toffoli gate acting as classical AND
// Inputs: q0 (A), q1 (B). Output AND stored in target q2 (initialised |0>)
qreg q[3];
creg c[3];

// (Optionally prepare inputs here, e.g. X q[0]; X q[1];)

ccx q[0], q[1], q[2];  // q2 := A ∧ B

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
