ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])


def normalize_state(alpha, beta):
   
    normal = np.linalg.norm([alpha,beta])
    return np.array([alpha/normal,beta/normal])

    pass