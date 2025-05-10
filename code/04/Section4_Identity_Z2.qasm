OPENQASM 2.0;
include "qelib1.inc";
// Verify Z^2 = I
qreg q[1];
creg c[1];

z q[0];
z q[0];

measure q[0] -> c[0];
