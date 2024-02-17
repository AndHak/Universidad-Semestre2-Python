from arma import *
from superheroe import *

martillo = Arma("Martillo", 6, 4)
hacha = Arma("Hacha", 4, 5)

thor = Superheroe("Thor", 20, 3, True, martillo)
hulk = Superheroe("Hulk", 20, 5, False, hacha)

print("Salud de Hulk: ", hulk.salud)
thor.atacar(hulk)
print("Salud de Hulk: ", hulk.salud)
print(f"Resistencia martillo: {martillo.resistencia}")
print(f"Ataque martillo: {martillo.destruccion}")
print(f"Categoria martillo: {martillo.categoria}")

thor.encontrar_mejora("Martillo")

print(f"Resistencia martillo: {martillo.resistencia}")
print(f"Ataque martillo: {martillo.destruccion}")
print(f"Categoria martillo: {martillo.categoria}")

thor.atacar(hulk)
print("Salud de Hulk: ", hulk.salud)

print(f"Resistencia martillo: {martillo.resistencia}")
print(f"Ataque martillo: {martillo.destruccion}")
print(f"Categoria martillo: {martillo.categoria}")

