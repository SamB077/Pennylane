dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def convert_to_rz_rx():
  
    qp.RX(np.pi/2,wires=0)
    qp.RZ(np.pi*7/4,wires=0)
    qp.RX(np.pi,wires=0)

    return qp.state()