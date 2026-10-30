def hadamard_transform(my_wires):

    for wire in my_wires:
        qp.H(wire)

def diffusion():

    hadamard_transform(query_register)
    qp.MultiControlledX(wires = query_register + aux, control_values= [0] * len(query_register))
    hadamard_transform(query_register)

    pass
