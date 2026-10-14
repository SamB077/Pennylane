dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def prepare_psi_plus():

    qp.Hadamard(0)
    qp.CNOT([0,1])
    # PREPARE (1/sqrt(2)) (|00> + |11>)

    return qp.state()

@qp.qnode(dev)
def prepare_psi_minus():

    qp.PauliX(0)
    qp.Hadamard(0)
    qp.CNOT([0,1])
    # PREPARE (1/sqrt(2)) (|00> - |11>)

    return qp.state()

@qp.qnode(dev)
def prepare_phi_plus():

    qp.PauliX(1)
    qp.Hadamard(0)
    qp.CNOT([0,1])
    # PREPARE  (1/sqrt(2)) (|01> + |10>)

    return qp.state()

@qp.qnode(dev)
def prepare_phi_minus():

    qp.PauliX(0)
    qp.PauliX(1)
    qp.Hadamard(0)
    qp.CNOT([0,1])
    # PREPARE  (1/sqrt(2)) (|01> - |10>)
    
    return qp.state()

psi_plus = prepare_psi_plus()
psi_minus = prepare_psi_minus()
phi_plus = prepare_phi_plus()
phi_minus = prepare_phi_minus()

print(f"|ψ_+> = {psi_plus}")
print(f"|ψ_-> = {psi_minus}")
print(f"|ϕ_+> = {phi_plus}")
print(f"|ϕ_-> = {phi_minus}")
