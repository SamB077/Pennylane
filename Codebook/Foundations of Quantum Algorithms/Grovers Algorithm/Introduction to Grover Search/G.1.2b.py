@qp.qnode(dev)
def two_difforacle_amp(combo):

    for wire in range(n_bits):
        qp.H(wire)
    
    matrix_oracle = oracle_matrix(combo)
    matrix_diff = diffusion_matrix()
    for _ in range(2):
        qp.QubitUnitary(matrix_oracle,wires=list(range(n_bits)))
        qp.QubitUnitary(matrix_diff,wires=list(range(n_bits)))

    return qp.state()
