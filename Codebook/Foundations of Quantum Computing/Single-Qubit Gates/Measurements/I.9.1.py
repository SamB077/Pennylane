dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_h_and_measure(state):
   
    if state == 1:
        qp.PauliX(wires=0)

    qp.Hadamard(0)

    return qp.probs(0)

print(apply_h_and_measure(0))
print(apply_h_and_measure(1))