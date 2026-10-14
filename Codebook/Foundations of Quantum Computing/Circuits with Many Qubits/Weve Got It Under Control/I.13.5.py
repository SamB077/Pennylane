dev = qp.device("default.qubit", wires=5)

@qp.qnode(dev)
def four_qubit_mcx_only_tofs():

    qp.PauliX(wires=0)
    qp.PauliX(wires=1)
    qp.PauliX(wires=2)

    qp.Toffoli([0,1,3])
    qp.Toffoli([2,3,4])
    qp.Toffoli([0,1,3])

    return qp.state()

print(four_qubit_mcx_only_tofs())
