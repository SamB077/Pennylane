n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

@qp.qnode(dev)
def pair_circuit(x_tilde, combo):

    for i in range(n_bits-1): 
        if x_tilde[i] == 1:
            qp.PauliX(wires=i)

    qp.Hadamard(n_bits-1)
    oracle = oracle_matrix(combo)
    qp.QubitUnitary(oracle, wires=range(n_bits))
    qp.Hadamard(wires=n_bits-1)
 
    return qp.probs(wires=n_bits-1)
