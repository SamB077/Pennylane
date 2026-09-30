def my_circuit(theta, phi):

    qp.CNOT(wires=[0, 1])
    qp.RX(theta, wires=2)
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[2, 0])
    qp.RY(phi, wires=1)

    return qp.probs(wires=[0, 1, 2])