
print((lambda x: x/4) (17))

cuarta = lambda x: x/4

print(cuarta(17))

datos = [[9, "Jc", 2],
         [7, "aK", 5],
         [4, "Sv", 5],
         [3, "Dw", 5],
         [5, "mx", 4]]

datos.sort(key=lambda x: x[0] + x[2])

print(datos)