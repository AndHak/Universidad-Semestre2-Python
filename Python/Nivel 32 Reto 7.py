datos = [40, 20, 51, 41, 30, 11, 50, 31, 10, 21]

datos.sort(key=lambda x: x if x % 10 == 0 else x+1000)

print(datos)