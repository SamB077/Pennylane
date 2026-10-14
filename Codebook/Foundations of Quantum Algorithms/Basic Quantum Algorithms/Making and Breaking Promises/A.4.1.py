n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

def multisol_oracle_matrix(combos):

    indices = [np.ravel_multi_index(combo, [2]*len(combo)) for combo in combos]
    my_array = np.identity(2**len(combos[0]))
    my_array[indices,indices] = -1

    return my_array
    
@qp.qnode(dev)
def multisol_pair_circuit(x_tilde, combos):

    for i in range(n_bits-1):
        if x_tilde[i] == 1:
            qp.PauliX(wires=i)

    oracle = multisol_oracle_matrix(combos)
    qp.Hadamard(n_bits-1)
    qp.QubitUnitary(oracle,wires=range(n_bits))
    qp.Hadamard(n_bits-1)

    return qp.probs(wires=n_bits-1)
