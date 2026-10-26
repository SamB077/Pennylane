dev = qp.device('default.qubit', wires=4)

@qp.qnode(dev)
def pennylane_qft(basis_id, n_qubits):

    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))

    qp.QFT(wires=range(4))
    
    return qp.state()
