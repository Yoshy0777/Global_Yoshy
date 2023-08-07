from funciones import *
import datetime

Horario = datetime.time(8,00)
H_Limite = datetime.time(23,30)
Hora_Actual = datetime.datetime.now().time()

if (Hora_Actual>=Horario and Hora_Actual<H_Limite):
    print(f"Hora actual: {Hora_Actual.strftime('%H:%M')}")
    print("--- Bienvenido a la tienda departamental Coppiel ---")
    print("------------------------------------------------------")
    menu()
else:
    print(f"Hora actual: {Hora_Actual.strftime('%H:%M')}")
    print("Acceso denegado. No se puede usar el programa debido al horario establecido")