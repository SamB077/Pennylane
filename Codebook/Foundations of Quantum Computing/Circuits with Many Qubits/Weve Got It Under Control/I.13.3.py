dev = qp.device("default.qubit", wires=3)

phi, theta, omega = 1.2, 2.3, 3.4

@qp.qnode(dev)
def no_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)
    return qp.state()

@qp.qnode(dev)
def controlled_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.Toffoli([0,1,2])
    qp.Toffoli([0,2,1])
    qp.Toffoli([0,1,2])

    return qp.state()

print(no_swap(phi, theta, omega))
print(controlled_swap(phi, theta, omega))
