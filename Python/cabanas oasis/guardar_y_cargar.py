from clientes import *
from servicios import *
from venta import *
import pickle
import os

directorio = os.path.dirname(os.path.abspath(__file__))
subdirectorio_cargar = os.path.join(directorio, "cargar")

def crear_directorio_si_no_existe(subdirectorio):
    if not os.path.exists(subdirectorio):
        os.makedirs(subdirectorio)

def guardar():
    crear_directorio_si_no_existe(subdirectorio_cargar)
    with open(os.path.join(subdirectorio_cargar, "clientes.plk"), "wb") as file:
        pickle.dump(Cliente.clientes, file)

    with open(os.path.join(subdirectorio_cargar, "servicios.plk"), "wb") as file:
        pickle.dump(Servicio.servicios, file)

    with open(os.path.join(subdirectorio_cargar, "cabañas.plk"), "wb") as file:
        pickle.dump(Cabaña.cabañas, file)

    with open(os.path.join(subdirectorio_cargar, "ventas.plk"), "wb") as file:
        pickle.dump(Venta.registro_ventas, file)

    with open(os.path.join(subdirectorio_cargar, "numero_factura.plk"), "wb") as file:
        pickle.dump(Venta.numero_factura, file)

def cargar():
    crear_directorio_si_no_existe(subdirectorio_cargar)

    try:
        with open(os.path.join(subdirectorio_cargar, "clientes.plk"), "rb") as file:
            Cliente.clientes = pickle.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'clientes.plk'. Se creará uno nuevo al registrar clientes.")

    try:
        with open(os.path.join(subdirectorio_cargar, "servicios.plk"), "rb") as file:
            Servicio.servicios = pickle.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'servicios.plk'. Se creará uno nuevo al registrar servicios.")

    try:
        with open(os.path.join(subdirectorio_cargar, "cabañas.plk"), "rb") as file:
            Cabaña.cabañas = pickle.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'servicios.plk'. Se creará uno nuevo al registrar servicios.")

    try:
        with open(os.path.join(subdirectorio_cargar, "ventas.plk"), "rb") as file:
            Venta.registro_ventas = pickle.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.plk'. Se creará uno nuevo al registrar ventas.")

    try:
        with open(os.path.join(subdirectorio_cargar, "numero_factura.plk"), "rb") as file:
            Venta.numero_factura = pickle.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'numero_factura.plk'. Se creará uno nuevo al registrar ventas.")
