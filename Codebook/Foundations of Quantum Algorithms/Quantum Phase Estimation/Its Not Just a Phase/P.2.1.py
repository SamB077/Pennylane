def U_power_2k(unitary, k):

    return np.linalg.matrix_power(unitary, 2**(k))
            
U = qp.T.compute_matrix()
print(U)

U_power_2k(U, 2)
