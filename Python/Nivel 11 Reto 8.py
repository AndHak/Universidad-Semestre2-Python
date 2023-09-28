#Copiando una lista al reverso

numeros = [1,2,3,4,5,6,7,8,9]
copia = list(numeros)

for i in range(len(copia)):
    for j in range(len(copia)-i-1):
        if copia[j] < copia[j+1]:
            copia[j], copia[j+1] = copia[j+1], copia[j]

print(numeros)
print(copia)