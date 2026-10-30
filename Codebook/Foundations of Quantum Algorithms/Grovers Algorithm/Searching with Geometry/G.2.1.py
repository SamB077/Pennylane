n_bits = 5
dev = qp.device("default.qubit", wires=n_bits)

def oracle_matrix(combo):

    index = np.ravel_multi_index(combo, [2] * len(combo)) 
    my_array = np.identity(2 ** len(combo)) 
    my_array[index, index] = -1
    
    return my_array

def diffusion_matrix():

    psi_piece = (1 / 2**n_bits) * np.ones(2**n_bits)
    ident_piece = np.eye(2**n_bits)
    return 2 * psi_piece - ident_piece

@qp.qnode(dev)
def grover_circuit(combo, num_steps):

    for wire in range(n_bits):
        qp.H(wire)
    matrix_oracle = oracle_matrix(combo)
    matrix_diff = diffusion_matrix()

    for _ in range(num_steps):
        qp.QubitUnitary(matrix_oracle,wires=list(range(n_bits)))
        qp.QubitUnitary(matrix_diff,wires=list(range(n_bits)))

    return qp.state()

my_steps = 4 
