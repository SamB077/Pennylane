def values_to_coefficients(values):

    return np.fft.ifft(values)

A = [10.+0.j,  2.-2.j,  2.+0.j,  2.+2.j]
print(values_to_coefficients(A))