dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_rx_pi(state):
   
    if state == 1:
        qp.PauliX(wires=0)

    return qp.state()

print(apply_rx_pi(0))
print(apply_rx_pi(1))