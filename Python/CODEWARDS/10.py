"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
"""

def max_sequence(arr):
    if not arr:
        return 0

    suma_total = 0
    limite = len(arr)

    suma_acumulativa = [0] + [sum(arr[:i+1]) for i in range(limite)]

    for secuencias in range(1, limite + 1):
        for i in range(limite - secuencias + 1):
            suma = suma_acumulativa[i + secuencias] - suma_acumulativa[i]
            if suma > suma_total:
                suma_total = suma
                break

    return suma_total

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))