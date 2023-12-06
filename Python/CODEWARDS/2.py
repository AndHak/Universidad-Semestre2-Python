"""
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order(sequence):
    sequence = list(sequence)
    devolver = []
    for i in range(len(sequence)):
        if i == 0:
            devolver.append(sequence[i])
            anterior = sequence[i]
        elif sequence[i] == anterior:
            continue
        else:
            devolver.append(sequence[i])
            anterior = sequence[i]
    return devolver

unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1, 2, 2, 3, 3])
unique_in_order((1, 2, 2, 3, 3))
