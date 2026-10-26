def coefficients_to_values(coefficients):

    return np.fft.fft(coefficients)

A = [4, 3, 2, 1]
print(coefficients_to_values(A))
