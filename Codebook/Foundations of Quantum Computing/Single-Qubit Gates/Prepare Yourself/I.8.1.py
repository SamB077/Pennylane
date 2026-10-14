dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def prepare_state():
    
    qp.Hadamard(0)
    qp.RZ(np.pi * 5/4, wires=0)

    return qp.state()