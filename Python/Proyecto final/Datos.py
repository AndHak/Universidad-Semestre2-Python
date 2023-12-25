

class DatosPelicula:
    def __init__(self, titulo_pelicula, sinopsis, duracion, genero, edad_minima, costo_pelicula):
        self.titulo_pelicula = titulo_pelicula
        self.sinopsis = sinopsis
        self.duracion = duracion
        self.genero = genero
        self.edad_minima = edad_minima
        self.costo_pelicula = costo_pelicula

    def obtener_datos_pelicula(self):
        return self.titulo_pelicula, self.sinopsis, self.duracion, self.genero, self.edad_minima, self.costo_pelicula

class DatosCliente:
    def __init__(self, identificacion_cliente, nombre_cliente, edad_cliente):
        self.identificacion_cliente = identificacion_cliente
        self.nombre_cliente = nombre_cliente
        self.edad_cliente = edad_cliente

    def obtener_datos_cliente(self):
        return self.identificacion_cliente, self.nombre_cliente, self.edad_cliente

class DatosConfiteria:
    def __init__(self, id_producto, nombre_producto, categoria_producto, precio_compra_producto, precio_venta_producto, cantidad_producto):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.categoria_producto = categoria_producto
        self.precio_compra_producto = precio_compra_producto
        self.precio_venta_producto = precio_venta_producto
        self.cantidad_producto = cantidad_producto

    def obtener_datos_producto(self):
        return self.id_producto, self.nombre_producto, self.categoria_producto, self.precio_compra_producto, self.precio_venta_producto, self.cantidad_producto

class DatosEgreso:
    def __init__(self, numero_factura, valor_egreso, descripcion_egreso, el_dinero_sale_de):
        self.numero_factura = numero_factura
        self.valor_egreso = valor_egreso
        self.descripcion_egreso = descripcion_egreso
        self.el_dinero_sale_de = el_dinero_sale_de

    def obtener_datos_egreso(self):
        return self.numero_factura, self.valor_egreso, self.descripcion_egreso, self.el_dinero_sale_de
    

