num_wires = 2
dev = qp.device("default.qubit", wires=num_wires)

@qp.qnode(dev)
def apply_cnot(basis_id):

    bits = [int(x) for x in np.binary_repr(basis_id, width=num_wires)]
    qp.BasisState(bits, wires=[0, 1])

    qp.CNOT(wires=[0,1])

    return qp.state()

cnot_truth_table = {"00": "00", "01": "01", "10": "11", "11": "10"}

print(apply_cnot(0))
