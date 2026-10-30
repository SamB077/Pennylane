@qp.qnode(dev)
def grover_circuit(combo):

    qp.PauliX(aux)
    qp.H(aux)
    
    hadamard_transform(query_register)
    for _ in range(1): 
        oracle(combo)
        diffusion()

    return qp.probs(query_register)
