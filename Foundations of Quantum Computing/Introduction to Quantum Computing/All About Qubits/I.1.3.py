def measure_state(state, num_meas):

    a0 = np.real(np.conj(state[0]) * state[0])
    a1 = np.real(np.conj(state[1]) * state[1])
    b = np.random.choice([0, 1], size=num_meas, p=[a0,a1])

    return np.array(b)

    pass
