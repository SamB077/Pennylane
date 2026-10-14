dev = qp.device("default.qubit", wires=2)

phi, theta, omega = 1.2, 2.3, 3.4

@qp.qnode(dev)
def apply_swap(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.SWAP([0,1])

    return qp.state()

@qp.qnode(dev)
def apply_swap_with_cnots(phi, theta, omega):
    prepare_states(phi, theta, omega)

    qp.CNOT([0,1])
    qp.CNOT([1,0])
    qp.CNOT([0,1])

    return qp.state()

print(f"Regular SWAP state = {apply_swap(phi, theta, omega)}")
print(f"CNOT SWAP state = {apply_swap_with_cnots(phi, theta, omega)}")
