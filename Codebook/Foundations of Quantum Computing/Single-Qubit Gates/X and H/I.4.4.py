dev = qml.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_hxh(state):

    if state == 1:
        qp.PauliX(wires=0)

    qp.Hadamard(wires=0)
    qp.PauliX(wires=0)
    qp.Hadamard(wires=0)

    return qp.state()

print(apply_hxh(0))
print(apply_hxh(1))
