dev = qp.device("default.qubit", wires=1)

phi, theta, omega = np.pi/2, np.pi/2, np.pi/2

@qp.qnode(dev)
def hadamard_with_rz_rx():
    qp.RZ(phi, wires=0)
    qp.RX(theta, wires=0)
    qp.RZ(omega, wires=0)
    return qp.state()