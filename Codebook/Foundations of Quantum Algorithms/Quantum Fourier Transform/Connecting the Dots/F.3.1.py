num_wires = 3
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def three_qubit_QFT(basis_id):

    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1, 2])
    
    omega = np.exp(2j * np.pi / 8)
    
    U = np.zeros((8, 8), dtype=complex)
    for j in range(8):
        for k in range(8):
            U[j, k] = (omega ** (j * k)) / np.sqrt(8.0)
            
    qp.QubitUnitary(U, wires=[0, 1, 2])

    return qp.state()