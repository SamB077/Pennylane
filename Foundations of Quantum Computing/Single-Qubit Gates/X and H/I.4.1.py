dev = qp.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qp.qnode(dev)
def varied_initial_state(state):

    if state == 1:
        qp.PauliX(wires=0)

    qp.QubitUnitary(U, wires=0)

    return qp.state()