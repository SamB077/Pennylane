dev = qp.device("default.qubit", wires=1)

@qp.qnode(dev)
def measure_in_y_basis():

  prepare_psi()

  qp.adjoint(y_basis_rotation)()

  return qp.probs(0)

print(measure_in_y_basis())