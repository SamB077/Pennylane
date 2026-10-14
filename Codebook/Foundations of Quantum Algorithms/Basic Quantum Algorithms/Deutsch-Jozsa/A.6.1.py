n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

@qp.qnode(dev)
def multisol_hoh_circuit(combos):

    for wires in range(n_bits):
        qp.Hadamard(wires)
    oracles = multisol_oracle_matrix(combos)
    qp.QubitUnitary(oracles,wires=range(n_bits))
    for wires in range(n_bits):
        qp.Hadamard(wires)

    return qp.probs(wires=range(n_bits))