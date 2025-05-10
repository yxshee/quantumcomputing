OPENQASM 2.0;
include "qelib1.inc";
// Demonstrate that CSWAP • CSWAP = I (Fredkin is its own inverse)
qreg q[3];
creg c[3];

// Prepare arbitrary basis state (optional)
//x q[0];
//x q[1];
//x q[2];

// First CSWAP
cswap q[0], q[1], q[2];
// Second CSWAP (undoes the first)
cswap q[0], q[1], q[2];

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
