OPENQASM 2.0;
include "qelib1.inc";
// Verify S = T^2
qreg q[1];
creg c[1];

t q[0];
t q[0];     // T squared

// A standalone S gate could be added for comparison
measure q[0] -> c[0];
