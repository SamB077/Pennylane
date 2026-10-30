wires = 2
my_wires = range(wires)
dev = qp.device("default.qubit", wires=wires)
state = np.array([np.sqrt(2/9), np.sqrt(2/9), np.sqrt(2/9), 1/np.sqrt(3)])

@qp.prod
def generator(my_wires, state):

    qp.StatePrep(state, wires=my_wires)

def oracle(my_wires):

    qp.FlipSign(3, wires=my_wires)

def diffusion_operator(my_wires, state):

    qp.adjoint(generator)(my_wires, state)
    qp.FlipSign(0, wires=my_wires)  
    qp.GlobalPhase(np.pi, wires=my_wires)
    generator(my_wires, state)

def amplification_operator(my_wires, state):

    oracle(my_wires)
    diffusion_operator(my_wires, state)

@qp.qnode(dev)
def amp_amp_circuit(my_wires, state):
    generator(my_wires, state)
    amplification_operator(my_wires, state)
    
    return qp.state()