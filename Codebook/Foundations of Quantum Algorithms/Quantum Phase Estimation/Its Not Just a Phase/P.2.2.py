estimation_wires = [0, 1, 2]
target_wires = [3]

def apply_controlled_powers_of_U(unitary):

    for k in estimation_wires:
        U = U_power_2k(unitary, len(estimation_wires)-k-1)
        qp.ControlledQubitUnitary(U, wires = [k] + target_wires)
        
    pass
