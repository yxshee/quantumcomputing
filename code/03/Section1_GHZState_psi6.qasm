OPENQASM 2.0;
include "qelib1.inc";
// |ψ6⟩ = (|000> − |111>)/√2   (3‑qubit GHZ−)
qreg q[3];
creg c[3];

h q[0];
cx q[0], q[1];
cx q[0], q[2];
z q[2];      // flip phase of |111>

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
