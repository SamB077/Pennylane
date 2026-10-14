def oracle_matrix(combo):

    index = np.ravel_multi_index(combo, [2]*len(combo))
    my_array = np.identity(2**len(combo)) 
    my_array[index,index] = -1

    return my_array