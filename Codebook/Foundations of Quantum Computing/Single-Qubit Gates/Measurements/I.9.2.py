def prepare_psi():
    qp.RX(-np.pi*2/3,0)
    pass

def y_basis_rotation():
    qp.Hadamard(0)
    qp.S(0)
    pass