wires = 2
my_wires = range(wires)
dev = qp.device("default.qubit", wires=wires)
a = 1/25
state = np.array([np.sqrt((1-a)/3), np.sqrt((1-a)/3), np.sqrt((1-a)/3), np.sqrt(a)])

def optimal_iters(a):

    theta = np.arcsin(np.sqrt(a))
    iter = int(np.floor(np.pi / (4 * theta)))
    
    return iter

@qp.qnode(dev)
def built_in_amp_amp_circuit(my_wires, state):

    qp.StatePrep(state, wires=my_wires)
    iters = optimal_iters(a)
    qp.AmplitudeAmplification(U=qp.StatePrep(state, wires=my_wires),O=qp.FlipSign(3, wires=my_wires),iters=iters)

    return qp.state()