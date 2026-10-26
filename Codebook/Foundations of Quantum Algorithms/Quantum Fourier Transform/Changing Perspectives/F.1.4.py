def fft_multiplication(poly_a, poly_b):

    x = len(poly_a) + len(poly_b) - 1

    n = 1 if x <= 1 else 2 ** (x - 1).bit_length()

    value_a = np.fft.fft(poly_a, n)
    value_b = np.fft.fft(poly_b, n)
    value = value_a * value_b
    
    return np.fft.ifft(value)