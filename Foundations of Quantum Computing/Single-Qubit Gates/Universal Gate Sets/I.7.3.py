dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def unitary_with_h_and_t():
   
    qp.Hadamard(0)
    qp.T(0)
    qp.Hadamard(0)
    qp.T(0)
    qp.T(0)
    qp.Hadamard(0)

    return qp.state()