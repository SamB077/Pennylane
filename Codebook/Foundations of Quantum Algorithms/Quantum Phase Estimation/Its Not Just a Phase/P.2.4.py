estimation_wires = [0, 1, 2]
target_wires = [3]

def estimate_phase(probs):

    return np.argmax(probs) / 2 ** len(estimation_wires)

U = qp.T.compute_matrix()
probs = qpe(U)

estimated_phase = estimate_phase(probs)
print(estimated_phase)
