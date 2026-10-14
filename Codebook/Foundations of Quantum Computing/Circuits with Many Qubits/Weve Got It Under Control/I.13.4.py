dev = qp.device("default.qubit", wires=4)

@qp.qnode(dev)
def four_qubit_mcx():
    for wire in [0,1,2]:
        qp.Hadamard(wire)
    qp.MultiControlledX([0,1,2,3],[0,0,1])

    return qp.state()

print(four_qubit_mcx())
