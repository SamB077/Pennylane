dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_hadamard():

    qp.Hadamard(wires=0)

    return qp.state()