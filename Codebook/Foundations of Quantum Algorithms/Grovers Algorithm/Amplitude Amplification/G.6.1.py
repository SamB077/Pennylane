wires = 2
my_wires=range(wires)
dev = qp.device("default.qubit", wires=wires)
state=np.array([np.sqrt(2/9), np.sqrt(2/9), np.sqrt(2/9), 1/np.sqrt(3)])

@qp.prod
def generator(my_wires,state):

    qp.StatePrep(state, wires=my_wires)
