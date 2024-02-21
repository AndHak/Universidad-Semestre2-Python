resultados = [
    ["101","Alicia","03:20:05"],
    ["102","Alberto","03:20:01"],
    ["103","Jorge","03:20:04"],
    ["104","Susana","03:20:07"],
    ["105","Roberto","03:20:06"],
    ["106","Silvia","03:20:04"],
    ["107","Ignacio","03:20:02"],
    ["108","Raquel","03:20:03"]
]

resultados.sort(key= lambda x: x[2])

print(resultados)

datos = [(5, "a"), ("d", 3), ("e", 1), (2, "b"), ("c", 4)]

datos.sort(key=lambda x: x[0] if isinstance(x[0], int) else x[1])

print(datos)