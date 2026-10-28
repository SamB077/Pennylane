dev = qp.device("default.qubit", wires=2)
        
@qp.qnode(dev)
def phase_kickback_X(eigenvector):

    qp.H(0)
    
    if eigenvector == "plus":  
        qp.H(1) 
    elif eigenvector == "minus":
        qp.X(1)
        qp.H(1) 
        
    qp.CNOT(wires=[0, 1])
    qp.H(0)
    
    return qp.probs(0) 

print(phase_kickback_X("plus"))
print(phase_kickback_X("minus"))

eigenvalue_of_X_plus = 1
eigenvalue_of_X_minus = -1
