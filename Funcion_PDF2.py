
from reportlab.pdfgen import canvas
from Funcion_QR import *
from funciones import *
from reportlab.lib.pagesizes import A4
from Funcion_PDF import *
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
fecha_actual = datetime.datetime.now()

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"
nombreArchivo = ruta + "Historial_Clientes_Coppiel.pdf"
nombreQR = ruta + "miQR.png"
Imagen = ruta + "Coppel_Historial.png"

def HistorialPDF(ListaClientes):
    generarQR(nombreQR,"Hola desde funcion")
    c = canvas.Canvas(nombreArchivo, pagesize= (1200,900))
    c.drawImage(Imagen,870,710,300,280,mask="auto")
    h = 800
    x = 0
    y = h -50
    c.line(x,y,x + 2000, y)
    c.setFont('Helvetica', 16)
    c.drawString(100,850,"Regimen fiscal: Regimen General de Ley Personas Morales")
    c.drawString(410,800,"Para más información llama al: 01-800-2207735")
    c.drawString(100,800,"Coppiel S.A. de C.V.")
    c.drawString(100,765,"Fecha de Hoy:")
    c.drawString(590,765,fecha_actual.strftime("%Y-%D"))
    

    c.drawString(90,730,"|Nombre del cliente|")
    c.drawString(300,730,"|Correo Electronico|")
    c.drawString(600,730,"|Hora registro|")
    c.drawString(850,730,"|ID del usuario|")

    Yinicial = 715
    c.setFont('Helvetica',13)
    for cliente in ListaClientes:
        c.drawString(119,Yinicial,f"{cliente['Nombre']}")
        c.drawString(303,Yinicial,f"{cliente['Correo']}")
        c.drawString(617,Yinicial,f"{Hora()}:{Minutos()}")
        c.drawString(870,Yinicial,f"{IDUsuario()}")
        Yinicial=Yinicial-15

        

    c.save()
    print("------ Historial imprimido con exito ------")

def IDUsuario():
    return str(random.randint(100000,999999))
def Hora():
    return str(random.randint(8,23))
def Minutos():
    return str(random.randint(00,60))
