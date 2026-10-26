num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def two_qubit_QFT(basis_id):

    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1])

    omega = np.exp(2j * np.pi / 4)
    
    U = np.zeros((4, 4), dtype=complex)
    for j in range(4):
        for k in range(4):
            U[j, k] = (omega ** (j * k)) / 2.0
            
    qp.QubitUnitary(U, wires=[0, 1])

    return qp.state()