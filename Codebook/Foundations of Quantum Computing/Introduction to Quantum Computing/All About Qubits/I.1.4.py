U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

def apply_u(state):
    
    New = np.array(U @ state.T)
    
    return New
    pass
