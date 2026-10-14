dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def two_qubit_circuit():

    qp.Hadamard(0)  # Puts qubit 0 into the |+> state
    qp.X(1)    # Puts qubit 1 into the |1> state

    return qp.expval(qp.PauliY(0)), qp.expval(qp.PauliZ(1))