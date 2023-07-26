from Funcion_PDF import *
from Datos_estaticos import *
listaNombres = []
listaEdades = []

def menu():
    opcion = 1
    while(opcion!=0):
        print("1. Pedir datos")
        print("2. Imprimir datos")
        print("3. Denerar PDF")
        print("4. Generar QR")
        print("0, Salir")
        opcion = int(input("Elije una opcion: "))
        if(opcion==1):
            pedirDatos()
        elif (opcion==2):
            imprimirDatos()
        elif (opcion==3):
            GenerarPDF()
        elif (opcion==5):
            listarProductos()



        

def pedirDatos():
    listaNombres.append(input("Ingresa tu nombre: "))
    listaEdades.append(input("Ingresa una edad: "))
    print("--------- Guardado ---------")

def imprimirDatos():
    for i in range(len(listaNombres)):
        print(f"Nombre: {listaNombres[i]} Edad: {listaEdades[i]}")
