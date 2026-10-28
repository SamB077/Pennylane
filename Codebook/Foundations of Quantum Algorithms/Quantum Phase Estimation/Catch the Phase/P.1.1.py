dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def guess_the_unitary(unitary):

    qp.H(0)
    qp.ControlledQubitUnitary(unitary,[0,1])
    qp.H(0)
    
    return qp.probs(0)

U = qp.PauliZ.compute_matrix() 
print(guess_the_unitary(U))
