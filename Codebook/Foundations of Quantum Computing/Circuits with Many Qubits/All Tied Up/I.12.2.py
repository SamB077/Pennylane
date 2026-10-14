dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def apply_h_cnot():

    qp.Hadamard(0)
    qp.CNOT([0,1])

    return qp.state()

print(apply_h_cnot())

state_status = "entangled"
