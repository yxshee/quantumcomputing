OPENQASM 2.0;
include "qelib1.inc";
// Verify X^2 = I
qreg q[1];
creg c[1];

x q[0];
x q[0];

measure q[0] -> c[0];
