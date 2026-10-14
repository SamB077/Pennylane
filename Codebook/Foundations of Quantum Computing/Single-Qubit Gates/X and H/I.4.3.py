dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_hadamard_to_state(state):
   
    if state == 1:
        qp.PauliX(wires=0)

    qp.Hadamard(wires=0)

    return qp.state()

print(apply_hadamard_to_state(0))
print(apply_hadamard_to_state(1))