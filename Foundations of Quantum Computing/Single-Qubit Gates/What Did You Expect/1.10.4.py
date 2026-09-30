def variance_experiment(n_shots):
   
    n_trials = 100

    dev = qp.device("default.qubit",wires=1,shots=n_shots)
    @qp.qnode(dev)

    def circuit():
        qp.Hadamard(wires=0)
        return qp.expval(qp.PauliZ(wires=0))

    trial_results = [circuit() for _ in range(n_trials)]

    return np.var(trial_results)

def variance_scaling(n_shots):
    
    estimated_variance = 1/n_shots

    return estimated_variance

shot_vals = [10, 20, 40, 100, 200, 400, 1000, 2000, 4000]

results_experiment = [variance_experiment(shots) for shots in shot_vals]
results_scaling = [variance_scaling(shots) for shots in shot_vals]
plot = plotter(shot_vals, results_experiment, results_scaling)