dev = qp.device("default.qubit", wires=10)

def estimates_array(unitary):

    estimates = []
    target_wires = [9]
    
    for num_wires in range(2, 10):
        estimation_wires = range(num_wires)
        probs = qpe(unitary, estimation_wires, target_wires)
        window = phase_window(probs, estimation_wires)
        estimates.append(window)

    return estimates

U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])
estimates_array(U)