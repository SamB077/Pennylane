m_list = range(3)
opt_steps = []

for m_bits in m_list:
    combos = [[int(s) for s in np.binary_repr(j, n_bits)] for j in range(2**m_bits)]
    step_list = range(1, 10)
    prob_list = [grover_iter_multi(combos, step)[0] for step in step_list]
    best_step = local_max_arg(prob_list)
    opt_steps.append(best_step)

    pass

print("The optimal number of Grover steps for the number of solutions in", [1, 2, 4], "is", opt_steps, ".")
