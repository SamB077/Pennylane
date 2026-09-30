shot_results = []
i = 0

shot_values = [100, 1000, 10000, 100000, 1000000]

for shots in shot_values:
    
    dev = qp.device('default.qubit', wires=1, shots=shots)
    
    @qp.qnode(dev)
    def circuit():
        qp.RX(np.pi/4, wires=0)
        qp.Hadamard(wires=0)
        qp.Z(wires=0)
        return qp.expval(qp.PauliY(0)) 

    shot_results.append(circuit())

print(qp.math.unwrap(shot_results))