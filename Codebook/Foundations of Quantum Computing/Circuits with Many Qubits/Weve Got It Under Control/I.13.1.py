dev = qp.device("default.qubit", wires=2)

phi, theta, omega = 1.2, 2.3, 3.4

@qp.qnode(device=dev)
def true_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.CZ([0,1])

    return qp.state()


@qp.qnode(dev)
def imposter_cz(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.Hadamard(0)
    qp.CNOT([1,0])
    qp.Hadamard(0)

    return qp.state()

print(f"True CZ output state {true_cz(phi, theta, omega)}")
print(f"Imposter CZ output state {imposter_cz(phi, theta, omega)}")
