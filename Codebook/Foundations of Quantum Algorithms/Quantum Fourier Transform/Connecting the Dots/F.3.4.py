dev = qp.device('default.qubit', wires=4)

def qft_recursive_rotations(n_qubits, wire=0):

    if wire >= n_qubits:
        return
        
    qp.H(wire)

    for next_bit in range(wire + 1, n_qubits):
        angle = np.pi / (2 ** (next_bit - wire))
        qp.ControlledPhaseShift(angle, wires=[next_bit, wire])

    qft_recursive_rotations(n_qubits, wire=wire + 1)

@qp.qnode(dev) 
def qft_node(basis_id, n_qubits):
    bits = [int(x) for x in np.binary_repr(basis_id, width=n_qubits)]
    qp.BasisState(bits, wires=range(n_qubits))
    qft_recursive_rotations(n_qubits)
    swap_bits(n_qubits)
    return qp.state()