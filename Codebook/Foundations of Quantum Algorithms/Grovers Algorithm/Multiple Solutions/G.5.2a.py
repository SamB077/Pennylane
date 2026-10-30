n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qp.device("default.qubit", wires=all_wires, shots=None)

def grover_iter_multi(combos, num_steps):

    @qp.qnode(dev)
    def inner_circuit():
        qp.PauliX(wires=n_bits)
        qp.Hadamard(wires=n_bits)
        hadamard_transform(query_register)

        for _ in range(num_steps):
            oracle_multi(combos)
            diffusion(n_bits)
            
        return qp.probs(wires=query_register)

    return inner_circuit()
