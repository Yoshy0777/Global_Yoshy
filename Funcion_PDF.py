from reportlab.pdfgen import canvas
from Funcion_QR import *
from Datos_estaticos import *
from reportlab.lib.pagesizes import A4
import datetime
import locale
locale.setlocale(locale.LC_ALL,'')
fecha_actual = datetime.datetime.now()

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"
nombreArchivo = ruta + "ReporteGlobal.pdf"
#nombreArchivo = ruta + "ReporteGlobal_"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
nombreQR = ruta + "miQR.png"
Imagen = ruta + "Coppel.png"

def GenerarPDF(listaNombres,listaCorreo):

    
    generarQR(nombreQR,"Hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    c.drawImage(Imagen,220,765,150,70,mask="auto")
    c.setFont('Helvetica', 14)
    Xinicial = 220
    Yinicial = 780


    for i in range(len(listaNombres)):
        Yinicial = Yinicial -20
        c.drawString(Xinicial,Yinicial,f"Nombre: {listaNombres}")
        c.drawString(Xinicial+40,Yinicial,f"Correo: {listaCorreo}")

    c.drawString(35,730,"---------------------------------------------------------------------------------------------------------")
    c.drawImage(nombreQR,220,130,100,100)

      
        #c.drawString(Xinicial,Yinicial,listaNombres[i])        
        #c.drawString(Xinicial+140,Yinicial,listaCorreo[i])
    c.save()
    print("--------Reporte generado-------")