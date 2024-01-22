from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


def saludo(request):

    p1 = Persona("Andres", "Guerra", "22")

    ahora = datetime.datetime.now()

    doc_externo = open("C:/Programacion Universidad/Semestre 2/Python y Django/Proyecto1/Proyecto1/Plantillas/Html/plantilla1.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "edad":p1.edad, "hora": ahora})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hola mundo")

def dame_fecha(request):
    fecha = datetime.datetime.now()

    vista = f"""
<html>
<body>
<h1>
Fecha y hora: {fecha}
</h1>
</body>
</html>
"""
    return HttpResponse(vista)

def calculate_age(request, age, year):

    age = 22
    period = year-2024
    future_age = age + period

    view = f"""
<html>
<body>
<h1>
Años actuales: {age}. En el año {year} tendras {future_age} años
</h1>
</body>
</html>
"""
    
    return HttpResponse(view)