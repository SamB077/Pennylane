v = np.array([0.52889389 - 0.14956775j, 0.67262317 + 0.49545818j])

dev = qp.device("default.qubit", wires=1)
@qp.qnode(dev)

def prepare_state(state=v):
    qp.MottonenStatePreparation(state,0)

    return qp.state()

print(prepare_state(v))
print()
print(qp.draw(prepare_state, level="device")(v))