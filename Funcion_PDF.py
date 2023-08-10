from reportlab.pdfgen import canvas
from Funcion_QR import *
from Datos_estaticos import *
from reportlab.lib.pagesizes import A4
from funciones import *
import datetime
import random
import locale
locale.setlocale(locale.LC_ALL,'')
fecha_actual = datetime.datetime.now()

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"

nombreQR = ruta + "miQR.png"
Imagen = ruta + "Coppel.png"

def GenerarTicket(cliente):
    nombreArchivo = ruta + f"Ticket de {cliente['Nombre']} "+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"

    c = canvas.Canvas(nombreArchivo)
    c.drawImage(Imagen,190,765,250,70,mask="auto")
    c.setFont('Helvetica-Bold', 14)
    c.drawString(220,754,"Coppel S.A de C.V.")
    c.drawString(120,742,"Guanajuato, Blvd. del Minero 305, Javier Rojo Gómez, 42030")
    c.drawString(190,730,"Pachuca de Soto, Hidalgo México")

    h = 800
    x = 10
    y = h -75
    c.line(x,y,x + 580, y)
    c.setFont('Helvetica', 14)
    c.drawString(230,712,f"Nombre: {cliente['Nombre']}")
    c.drawString(210,700,f"Correo: {cliente['Correo']}")
    c.drawString(100,686,"Fecha: ")
    c.drawString(370,686,fecha_actual.strftime("%Y-%D"))
    c.setFont('Helvetica-Bold',20)
    c.drawString(170,667,f"Nota de la Venta No. {Random()}")
    c.setFont('Helvetica',14)
    c.drawString(40,640,"|Código|")
    c.drawString(120,640,"|Marca|")
    c.drawString(230,640,"|Nombre del producto|")
    c.drawString(490,640,"|Precio|")

    c.setFont('Helvetica',12)
    Yposicion = 625
    for producto in cliente['Carrito']:
        c.drawString(45,Yposicion,f"{IDProducto()}")
        c.drawString(123,Yposicion,f"{producto['Marca']}")
        c.drawString(233,Yposicion,f"{producto['NombreProducto']}")
        c.drawString(494,Yposicion,f"{producto['PrecioProducto']}")
        Yposicion = Yposicion - 15

    Total = PagoProducto(cliente['Carrito'])
    print(f"El total a pagar es: ${Total:.2f}")
    c.setFont('Helvetica',14)
    while True:
        UsuarioPago = float(input("Ingrese el monto que tiene que pagar: "))
        if UsuarioPago >= Total:
            Cambio = UsuarioPago - Total
            print("--- Pago realizado exitosamente ---")
            print(f"Cambio: ${Cambio:.2f}")

            c.drawString(90,350,"Total a pagar:")
            c.drawString(380,350,f"${Total:.2f}")
            c.drawString(90,337,f"Pago:")
            c.drawString(380,337,f"${UsuarioPago:.2f}")
            c.drawString(90,324,"Cambio:")
            c.drawString(380,324,f"{Cambio:.2f}")
            break
        else:
            print("--- ¿Estas robando o que? Paga COMPLETO. ")

    generarQR(nombreQR,informacion=f"C.R.{IDProducto()}\n Nombre del cliente: {cliente['Nombre']}\n Correo: {cliente['Correo']}\n ID del cliente: {Random()}")
    h2 = 250
    x2 = 10
    y2 = h2 - 35
    c.line(x2,y2,x2 + 580, y2)
    c.drawImage(nombreQR,200,100,100,100)


    c.save()
    print("--------Reporte generado-------")
def Random():
    return str(random.randint(10000000,99999999))
def IDProducto():
    return str(random.randint(100000,999999))
def PagoProducto(carrito):
    SubTotal = sum(producto['PrecioProducto'] for producto in carrito)
    IVA = SubTotal * 0.16
    Total = SubTotal + IVA
    return Total
