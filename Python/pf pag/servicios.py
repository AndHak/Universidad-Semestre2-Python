class Servicio:
    servicios = []

    def __init__(self, nombre, descripcion, costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
   
    @classmethod
    def agregar_servicio(cls, nombre, descripcion, costo):
        if descripcion == "Cabañas":
            nuevo_servicio = Cabaña(nombre, descripcion, costo, ocupada=False)
            Cabaña.cabañas.append(nuevo_servicio)
            print(f"Cabaña '{nombre}' agregada con éxito.")
            return
        if descripcion != "Cabañas":
            nuevo_servicio = Servicio(nombre, descripcion, costo)
            cls.servicios.append(nuevo_servicio)
            print(f"Servicio '{nombre}' agregado con éxito.")

    @classmethod
    def eliminar_servicio(cls, indice):
        if 0 <= indice-1 < len(cls.servicios):
            servicio_eliminado = cls.servicios.pop(indice-1)
            print(f"Servicio '{servicio_eliminado.nombre}' eliminado con éxito.")
        else:
            print("Índice de servicio no válido.")

    @classmethod
    def ver_servicios(cls):
        print("\n-------- Servicios --------")
        if not cls.servicios:
            print("No hay servicios registrados.")
            return

        for i, servicio in enumerate(cls.servicios):
            print(f"{i+1}. {servicio.nombre} - {servicio.descripcion} - Costo: ${servicio.costo:.2f}")

class Cabaña(Servicio):
    cabañas = []

    def __init__(self, nombre, descripcion, costo, ocupada):
        super().__init__(nombre, descripcion, costo)
        self.ocupada = ocupada

    @classmethod
    def ver_cabañas(cls):
        if not cls.cabañas:
            print("No hay cabañas registradas.")
            return

        for i, cabaña in enumerate(cls.cabañas):
            estado = "Disponible" if cabaña.ocupada == False else "Ocupada"
            print(f"{i+1}. {cabaña.nombre} - {cabaña.descripcion} - Costo: ${cabaña.costo:.2f} - Estado: {estado}")

    @classmethod
    def mostrar_cabaña(cls, cabaña):
        estado = "Disponible" if not cabaña.ocupada else "Ocupada"
        print(f"Cabaña: {cabaña.nombre} - Estado: {estado}")

    @classmethod
    def marcar_como_disponible(cls, cabaña):
        cabaña.ocupada = False
        print(f"Cabaña '{cabaña.nombre}' marcada como disponible.")

    @classmethod
    def seleccionar_cabaña(cls, indice):
        if 0 <= indice - 1 < len(cls.cabañas):
            return cls.cabañas[indice - 1]
        else:
            print("Índice de cabaña no válido.")
            return None

    @classmethod
    def eliminar_cabaña(cls, cabaña):
        cls.cabañas.remove(cabaña)
        print(f"Cabaña '{cabaña.nombre}' eliminada con éxito.")
