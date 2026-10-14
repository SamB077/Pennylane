def parity_checker(combos):

    parity = 0
    x_tilde_strs = [np.binary_repr(n, n_bits-1) for n in range(2**(n_bits-1))]
    x_tildes = [[int(s) for s in x_tilde_str] for x_tilde_str in x_tilde_strs]
    i = 0
    for x_tilde in x_tildes:
        
        probs = multisol_pair_circuit(x_tilde, combos)
        if np.isclose(probs[1], 1.0):
            parity += 1

    return parity % 2
