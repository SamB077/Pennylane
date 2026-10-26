def nearest_power_of_2(x):
    return 1 if x <= 1 else 2**(x - 1).bit_length()