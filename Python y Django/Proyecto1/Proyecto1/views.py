from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Adios mundo")

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