from colorama import init, Fore
import os

init(autoreset=True)

class Producto:
    def __init__(self, id_producto, nombre, precio_compra, precio_venta, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock

