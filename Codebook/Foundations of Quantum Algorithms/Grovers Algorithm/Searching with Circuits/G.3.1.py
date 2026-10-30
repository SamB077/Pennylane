n_bits = 5
query_register = list(range(n_bits))
aux = [n_bits]
all_wires = query_register + aux
dev = qp.device("default.qubit", wires=all_wires)

def oracle(combo):

    qp.MultiControlledX(wires=all_wires, control_values=combo)

    pass