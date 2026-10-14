dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def many_rotations():
   
    qp.Hadamard(wires=0)
    qp.S(wires=0)
    qp.adjoint(qp.T)(wires=0)
    qp.RZ(0.3,wires=0)
    qp.adjoint(qp.S)(wires=0)

    return qp.state()