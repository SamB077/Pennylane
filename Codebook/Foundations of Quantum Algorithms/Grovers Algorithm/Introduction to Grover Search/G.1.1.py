n_bits = 4
dev = qp.device("default.qubit", wires=n_bits)

def oracle_matrix(combo):

    index = np.ravel_multi_index(combo, [2] * len(combo))
    my_array = np.identity(2 ** len(combo)) 
    my_array[index, index] = -1
    return my_array

@qp.qnode(dev)
def oracle_amp(combo):

    for wire in range(n_bits):
        qp.H(wire)
    matrix = oracle_matrix(combo)
    qp.QubitUnitary(matrix, wires=list(range(n_bits)))

    return qp.state()
