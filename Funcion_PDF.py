from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"
nombreArchivo = ruta + "Ejemplo de funciones.pdf"

def GenerarPDF():
    c = canvas.Canvas(nombreArchivo)
    c.setFont('Helvetica', 17)
    c.drawString(240,520,"PDF generado con funciones")
    c.save()
    print("Reporte generado")