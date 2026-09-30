num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def make_basis_state(basis_id):

    binary_string = f"{basis_id:0{num_wires}b}"
    bits = [int(bit) for bit in binary_string]
    
    qml.BasisState(bits, wires=range(num_wires))

    return qp.state()

basis_id = 3
print(f"Output state = {make_basis_state(basis_id)}")