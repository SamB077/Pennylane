num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def decompose_two_qubit_QFT(basis_id):

    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1])
    
    qp.H(0)
    qp.ControlledPhaseShift(np.pi / 2, wires=[1, 0])
    qp.H(1)
    
    qp.SWAP([0,1])
    
    return qp.state()