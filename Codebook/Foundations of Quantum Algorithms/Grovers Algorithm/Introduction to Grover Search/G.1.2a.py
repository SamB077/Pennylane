n_bits = 4

def diffusion_matrix():

    n = 2 ** n_bits
    I = np.identity(n)
    J = np.ones((n,n))/n

    matrix = 2*J - I

    return matrix

@qp.qnode(dev)
def difforacle_amp(combo):

    for wire in range(n_bits):
        qp.H(wire)
    matrix_oracle = oracle_matrix(combo)
    matrix_diff = diffusion_matrix()
    qp.QubitUnitary(matrix_oracle,wires=list(range(n_bits)))
    qp.QubitUnitary(matrix_diff,wires=list(range(n_bits)))

    return qp.state()
