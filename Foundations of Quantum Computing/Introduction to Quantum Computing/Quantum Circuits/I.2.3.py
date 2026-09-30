dev = qp.device("default.qubit", wires=3)

@qp.qnode(dev)

def my_circuit(theta, phi, omega):
    qp.RX(theta, wires=0)
    qp.RY(phi, wires=1)
    qp.RZ(omega, wires=2)
    qp.CNOT(wires=[0, 1])
    qp.CNOT(wires=[1, 2])
    qp.CNOT(wires=[2, 0])
    return qp.probs(wires=[0, 1, 2])

theta, phi, omega = 0.1, 0.2, 0.3

my_circuit(theta,phi,omega)