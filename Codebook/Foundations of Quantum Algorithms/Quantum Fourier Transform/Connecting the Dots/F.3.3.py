dev = qp.device('default.qubit', wires=4)

def qft_rotations(n_qubits):

    for bit in range(n_qubits):
        qp.H(wires=bit)
        
        for next_bit in range(bit + 1, n_qubits):
            angle = np.pi / (2 ** (next_bit - bit))
            qp.ControlledPhaseShift(angle, [next_bit, bit])
    pass

@qp.qnode(dev) 
def qft_node(basis_id, n_qubits):
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    qft_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()