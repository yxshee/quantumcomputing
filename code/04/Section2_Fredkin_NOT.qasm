OPENQASM 2.0;
include "qelib1.inc";
// CSWAP configured to act as NOT on qubit 1.
//   Control q0 is fixed to |1⟩,
//   Target 1 q1 holds bit b,
//   Target 2 q2 is set to |1⟩.
// Swap(q1,q2) flips q1 when control is 1.
qreg q[3];
creg c[2];

// Force control and second target to |1⟩
x q[0];
x q[2];

// --- Optional: prepare q1 = b (comment/uncomment) ---
//x q[1];     // initialise b = 1
// --------------------------------------

cswap q[0], q[1], q[2];   // Acts as NOT on q1

measure q[1] -> c[0];     // ¬b
measure q[2] -> c[1];     // original b
