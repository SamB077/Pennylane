dev = qp.device("default.qubit", wires=1)


@qp.qnode(dev)
def fake_z():

    qp.Hadamard(wires=0)
    qp.RZ(np.pi,wires=0)

    return qp.state()