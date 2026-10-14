dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_ry(theta, state):
   
    if state == 1:
        qp.PauliX(wires=0)

    qp.RY(theta,wires=0)

    return qp.state()

angles = np.linspace(0, 4 * np.pi, 200)
output_states = np.array([apply_ry(t, 0) for t in angles])

plot = plotter(angles, output_states)