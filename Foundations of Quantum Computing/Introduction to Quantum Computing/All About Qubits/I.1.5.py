U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def initialize_state():

    return np.array([1,0])
    pass

def apply_u(state):
    return np.dot(U, state)

def measure_state(state, num_meas):
    p_alpha = np.abs(state[0]) ** 2
    p_beta = np.abs(state[1]) ** 2
    meas_outcome = np.random.choice([0, 1], p=[p_alpha, p_beta], size=num_meas)
    return meas_outcome


def quantum_algorithm():
    
    state = initialize_state()
    new_state = apply_u(state)
    return measure_state(new_state,100)
    pass