dev = qp.device("default.qubit", wires=1, shots=100000)

@qp.qnode(dev)
def circuit():
    qp.RX(np.pi / 4, wires=0)
    qp.Hadamard(wires=0)
    qp.PauliZ(wires=0)

    return qp.sample(qp.PauliY(0))

def compute_expval_from_samples(samples):
    
    return np.mean(samples)

samples = circuit()
print(compute_expval_from_samples(samples))