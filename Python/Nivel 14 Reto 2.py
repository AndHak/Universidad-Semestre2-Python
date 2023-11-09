#Eliminar por filtro

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

print(meses)

pregunta = input("Eliminar los meses que contengan la letra:  ")

"""
copia = list(meses)
for n in copia:
    if pregunta in n:
        meses.remove(n)
"""

for i in range(len(meses)-1,-1,-1):
    if pregunta in meses[i]:
        meses.remove(meses[i])

print(f"Los meses sin la letra {pregunta} son {meses}")

