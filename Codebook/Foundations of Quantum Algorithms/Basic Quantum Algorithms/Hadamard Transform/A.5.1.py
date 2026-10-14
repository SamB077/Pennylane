n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

@qp.qnode(dev)
def hoh_circuit(combo):

    for wires in range(n_bits):
        qp.Hadamard(wires)
    oracle = oracle_matrix(combo)
    qp.QubitUnitary(oracle,wires=range(n_bits))
    for wires in range(n_bits):
        qp.Hadamard(wires)
  
    return qp.probs(wires=range(n_bits))
