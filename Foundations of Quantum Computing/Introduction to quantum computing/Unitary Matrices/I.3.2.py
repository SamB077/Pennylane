dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def apply_u_as_rot(phi, theta, omega):

    qp.Rot(phi,theta,omega,wires=0)

    return qp.state()