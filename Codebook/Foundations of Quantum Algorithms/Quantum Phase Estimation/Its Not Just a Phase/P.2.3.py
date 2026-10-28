dev = qp.device("default.qubit", wires=4)

estimation_wires = [0, 1, 2]
target_wires = [3]

def prepare_eigenvector():
    qp.PauliX(target_wires)

@qp.qnode(dev)
def qpe(unitary):
    
    for wire in estimation_wires:
        qp.Hadamard(wire)
    prepare_eigenvector()
    apply_controlled_powers_of_U(unitary)
    qp.adjoint(qp.QFT)(estimation_wires)

    return qp.probs(estimation_wires)

U = qp.T.compute_matrix()
print(qpe(U))
