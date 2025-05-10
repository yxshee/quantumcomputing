OPENQASM 2.0;
include "qelib1.inc";
// Fredkin (CSWAP) gate acting as a classical AND gate.
// Controls/Targets:
//   q0 – control (A)
//   q1 – target 1 (B)
//   q2 – target 2 initialised to |0⟩; becomes A∧B
qreg q[3];
creg c[3];

// --- Optional test input preparation ---
//x q[0];      // Set A = 1
//x q[1];      // Set B = 1
// --------------------------------------

// Apply CSWAP
cswap q[0], q[1], q[2];

// Measure
measure q[0] -> c[0];     // A
measure q[1] -> c[1];     // B
measure q[2] -> c[2];     // A∧B  (AND output)
