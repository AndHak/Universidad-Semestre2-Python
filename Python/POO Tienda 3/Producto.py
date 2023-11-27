from colorama import init, Fore
import os

init(autoreset=True)


class CaracteristicasProducto():
    def __init__(self, id_producto, nombre, categoria, precio_compra, precio_venta, cantidad):
        self.id_producto = id_producto
        self.nombre_producto = nombre
        self.categoria_producto = categoria
        self.precio_compra_producto = precio_compra
        self.precio_venta_producto = precio_venta
        self.cantidad_producto = cantidad
