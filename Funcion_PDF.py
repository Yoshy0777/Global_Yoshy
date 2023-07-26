from reportlab.pdfgen import canvas
from Funcion_QR import *
from reportlab.lib.pagesizes import A4

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"
nombreArchivo = ruta + "Ejemplo de funciones.pdf"
nombreQR = ruta + "miQR.png"

def GenerarPDF(listaNombres,listaEdades):
    generarQR(nombreQR,"Hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    c.setFont('Helvetica', 17)
    Xinicial = 200
    Yinicial = 700

    c.drawString(Xinicial,Yinicial,"Edad: ")
    c.drawString(Xinicial+140,Yinicial,"Nombre: ")

    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombres)):
        c.setFont('Helvetica',20)
        Yinicial = Yinicial -20        
        c.drawString(Xinicial,Yinicial,listaEdades[i])        
        c.drawString(Xinicial+140,Yinicial,listaNombres[i])


    c.save()
    print("--------Reporte generado-------")