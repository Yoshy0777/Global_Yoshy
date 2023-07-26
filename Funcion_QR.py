import qrcode

ruta = "C:/Users/FRANKILIJOSHY/Desktop/Modularidad en python/prueba funciones/"
img = qrcode.make("Ya llego su mero gallo")
nombreImagen = ruta + "miQR.png"
f = open(nombreImagen, "wb")
img.save(f)