OPENQASM 2.0;
include "qelib1.inc";
// |ψ3⟩ = (|01> + |10>)/√2   (Bell Ψ+)
qreg q[2];
creg c[2];

x q[1];      // prepare |01>
h q[0];
cx q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
