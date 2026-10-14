dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_z_to_plus():
   
    qp.Hadamard(wires=0)
    qp.PauliZ(wires=0)

    return qp.state()

print(apply_z_to_plus())