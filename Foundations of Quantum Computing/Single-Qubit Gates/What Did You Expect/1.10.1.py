dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def circuit():

    qp.RX(np.pi/4,0)
    qp.Hadamard(0)
    qp.Z(0)

    return qp.expval(qp.PauliY(0))

print(circuit())