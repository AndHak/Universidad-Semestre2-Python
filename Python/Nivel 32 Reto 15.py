alumnos = ["Jorge", "Sara", "Lucia", "Andrés", "Miguel"]

edades = [25, 19, 31, 22, 42]

notas = [7.4, 8.3, 9.2, 6.5, 5.8]

datos_alumnos = zip(alumnos, edades, notas)

for a, e, n in datos_alumnos:
    print(f"Alumno: {a}, {e} años, Nota: {n}")

datos_alumnos = list(zip(alumnos, edades, notas))

print(datos_alumnos)

primero = [5, 7, 3, 5, 4]
segundo = [7, 9, 5, 6, 3]
tercero = [6, 8, 4, 7, 2]

notas = {}
for n, p, s, t in zip(alumnos, primero, segundo, tercero):
    notas[n] = (p+s+t)/3

print(notas)