n_list = range(3, 7)
opt_steps = []

for n_bits in n_list:
    combo = [0] * n_bits 
    step_list = range(1, 10) 

    prob_list = [grover_iter(combo, step)[0] for step in step_list]
    best_step = local_max_arg(prob_list)
    opt_steps.append(best_step)

    pass

print("The optimal number of Grover steps for qubits in", [3, 4, 5, 6], "is", opt_steps, ".")
