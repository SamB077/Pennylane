dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_rx(theta, state):
  
    if state == 1:
        qp.PauliX(wires=0)

    qp.RX(theta,wires=0)

    return qp.state()

angles = np.linspace(0, 9 * np.pi, 200)
output_states = np.array([apply_rx(t, 0) for t in angles])

plot = plotter(angles, output_states)