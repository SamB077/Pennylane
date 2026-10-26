dev = qp.device('default.qubit', wires=4)
       
def swap_bits(n_qubits):

    for i in range(n_qubits // 2):
        qp.SWAP(wires=[i, n_qubits - 1 - i])
    pass

@qp.qnode(dev) 
def qft_node(basis_id, n_qubits):
    
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))

    swap_bits(n_qubits)
    return qp.state()