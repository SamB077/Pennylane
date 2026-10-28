dev = qp.device("default.qubit", wires=10)

def fractional_binary_to_decimal(binary_fraction, wires):
    return float(binary_fraction/ 2 ** len(wires))

def phase_window(probs, estimation_wires):

    bound_1 = fractional_binary_to_decimal(np.argsort(probs)[-1], estimation_wires)
    bound_2 = fractional_binary_to_decimal(np.argsort(probs)[-2], estimation_wires) 
    
    return (bound_1, bound_2)

estimation_wires = range(0, 3)
target_wires = [9]
U = np.array([[1, 0], [0, np.exp((2*np.pi*1j/7))]])
probs = qpe(U, estimation_wires, target_wires)
print(phase_window(probs, estimation_wires))

done = True
