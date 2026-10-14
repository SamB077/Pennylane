def deutsch_jozsa(promise_var):

    if promise_var == 0:
        how_many = 2**(n_bits - 1)
    else:
        how_many = np.random.choice([0, 2**n_bits])
    combos = multisol_combo(n_bits, how_many)=
    
    probs = multisol_hoh_circuit(combos)[0]
    guess = int(np.rint(probs))

    return guess
