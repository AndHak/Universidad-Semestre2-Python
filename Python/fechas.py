from datetime import date, datetime

today = date.today()

print(today)

hora = datetime.now()

fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(fecha_venta)
print(hora)



