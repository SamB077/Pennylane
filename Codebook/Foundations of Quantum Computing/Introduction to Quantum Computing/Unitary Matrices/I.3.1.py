dev = qp.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qp.qnode(dev)
def apply_u():

    qp.QubitUnitary(U, wires=0)

    return qp.state()