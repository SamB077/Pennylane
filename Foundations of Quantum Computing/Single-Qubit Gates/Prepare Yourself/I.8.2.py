dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def prepare_state():

    qp.RX(np.pi/3,0)

    return qp.state()