dev = qp.device("default.qubit", wires=3)

@qp.qnode(dev)
def controlled_rotations(theta, phi, omega):

    qp.Hadamard(0)
    qp.CRX(theta,[0,1])
    qp.CRY(phi,[1,2])
    qp.CRZ(omega,[2,0])

    return qp.probs([0, 1, 2])

theta, phi, omega = 0.1, 0.2, 0.3
print(controlled_rotations(theta, phi, omega))
