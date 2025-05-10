OPENQASM 2.0;
include "qelib1.inc";
// Toffoli gate used as NOT by forcing both controls to |1⟩
// Target qubit q2 will always be flipped.
qreg q[3];
creg c[1];

// Force controls to |1>
x q[0];
x q[1];

// Optional: set target to an initial state here

ccx q[0], q[1], q[2];   // Acts as unconditional NOT on q2

measure q[2] -> c[0];
