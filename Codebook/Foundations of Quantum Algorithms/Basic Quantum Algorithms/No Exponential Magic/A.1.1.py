n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

@qp.qnode(dev)
def naive_circuit():

    for wire in range(n_bits):

        qp.Hadamard(wire)

    return qp.probs(wires=range(n_bits))