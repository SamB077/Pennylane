dev = qp.device("default.qubit", wires=3)

state = [0, 1]

@qp.qnode(device=dev)
def apply_control_sequence(state):

    if state[0] == 1:
        qp.PauliX(wires=0)
    if state[1] == 1:
        qp.PauliX(wires=1)

    qp.PauliX(wires=2)
    qp.Hadamard(wires=2)

    # IF STATE OF FIRST TWO QUBITS IS 01, APPLY X TO THIRD QUBIT
    qp.PauliX(0)
    qp.Toffoli([0, 1, 2])
    qp.PauliX(0)
    # IF STATE OF FIRST TWO QUBITS IS 10, APPLY Z TO THIRD QUBIT
    qp.PauliX(1)
    qp.Hadamard(2)
    qp.Toffoli([0, 1, 2])
    qp.Hadamard(2)
    qp.PauliX(1) 
    # IF STATE OF FIRST TWO QUBITS IS 11, APPLY Y TO THIRD QUBIT
    qp.adjoint(qp.S)(2)
    qp.Toffoli([0, 1, 2])
    qp.S(2)
    
    return qp.state()

print(apply_control_sequence(state))