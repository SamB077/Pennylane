dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def create_one_minus():
    
    qp.X(0)   
    qp.X(1)    
    qp.Hadamard(1)  

    return qp.expval(qp.Z(0) @ qp.X(1))

print(create_one_minus())