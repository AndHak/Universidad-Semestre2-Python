from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

def pag_a(request):
    ahora = datetime.datetime.now()

    return render(request, "a.html", {"Ahora":ahora})


def saludo(request):

    p1 = Persona("Andres", "Guerra", "22")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    ctx = {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "edad":p1.edad, "hora": ahora, "temas":temas}

    return render(request, "plantilla1.html", ctx)

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