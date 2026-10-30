def grover_iter(combo, num_steps):

    n_bits = len(combo)
    query_register = list(range(n_bits))
    aux = [n_bits]
    all_wires = query_register + aux
    dev = qp.device("default.qubit", wires=all_wires)

    @qp.qnode(dev)
    def inner_circuit():

        qp.PauliX(aux)
        qp.H(aux)
        
        hadamard_transform(query_register)
        for _ in range(num_steps):
            oracle(combo)
            diffusion(n_bits)
    
        return qp.probs(wires=query_register)

    return inner_circuit()
