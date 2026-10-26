num_wires = 1
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def one_qubit_QFT(basis_id):

    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0])

    qp.H(0)
    
    return qp.state()