from Funcion_PDF import *
from Datos_estaticos import *
listaNombres = []
listaCorreo = []
ListaClientes = []
IVA = 0.16
Password = "CAML890915R77"
def menu():
    opcion = 1
    while(opcion!=0):
        print("1. Ingresar datos")
        print("2. Imprimir datos")
        print("3. Denerar PDF (Ticket)")
        print("4. Generar QR")
        print("5. Lista de productos")
        print("6. Agregar productos al carrito")
        print("7. Mostrar el Carrito de Compras")
        print("8. Pagar el total (incluye IVA)")
        print("9. Imprimir Todos los clientes registrados")
        print("0. Salir")
        opcion = int(input("Elije una opcion: "))
        if(opcion==1):
            pedirDatos()
        elif (opcion==2):
            imprimirDatos()
        elif (opcion==3):
            GenerarPDF(listaNombres,listaCorreo)
        elif (opcion==5):
            Contra = input("Si quieres ver un producto, debes ingresar la contraseña del gerente: ")
            if (Contra==Password):
                print("----- Productos Disponibles -----")
                print("=========================================")
                Inventario()
            else:
                print("Contraseña Incorrecta, intentalo más tarde")
        elif (opcion==6):
            CarritoCompras()
        elif (opcion==7):
            MostrarCarrito()
        elif (opcion==8):
            TotalPagar = CaluloTotal()
            PagoTotal(TotalPagar)
            


def pedirDatos():
    listaNombres.append(input("Ingresa tu nombre: "))
    listaCorreo.append(input("Ingresa tu correo: "))
    ListaClientes.append((listaNombres, listaCorreo))
    print("--------- Guardado ---------")

def imprimirDatos():
    for i in range(len(listaNombres)):
        print(f"Nombre: {listaNombres[i]}    Correo: {listaCorreo[i]}")

def Inventario():
    print("- No. --- Marca --- ---- Nombre del producto ------- --- Precio ---")
    for i, (Marca,NombreProducto,PrecioProducto) in enumerate(zip(Marca,NombreProducto,PrecioProducto),1):
        print(f"  {i}.-      {Marca}      {NombreProducto}       ${PrecioProducto}")

def CarritoCompras():
    print("Selecciona uno de los siguientes productos ")
    print("-------------------------------------------------")
    Carrito = []
    Inventario()
    opcion = 1
    while opcion == 1:
        select = int(input("Elige un producto: "))
        if select < 1 or select > len(NombreProducto):
            print("Opcion invalida o producto no disponible. Por favor, elija un producto que este disponible")
        else:
            Carrito.append((Marca[select-1], NombreProducto[select-1], PrecioProducto[select-1]))
            print("----- Producto agregado al carrito -----")
        opcion = int(input("¿Desea elegir algún otro producto? 1.Si 2.No"))
    return Carrito
    
def MostrarCarrito():
    Seleccionado = CarritoCompras()
    print("--- Carrito de Compras ---")
    for Marca, NombreProducto, PrecioProducto in Seleccionado:
        print(f"{Marca}    {NombreProducto}    ${PrecioProducto}")

def CaluloTotal(Seleccionado):
    Seleccionado = CarritoCompras()
    TotalPagar = sum(PrecioProducto for _, PrecioProducto in Seleccionado)
    return TotalPagar
    
def PagoTotal(TotalPagar):
    print(f"El total a pagar es de: ${TotalPagar}")
    UsuarioPago = float(input("Ingrese la cantidad a pagar"))
    CalculoIVA = TotalPagar * IVA
    TotalPagoIVA = TotalPagar + CalculoIVA
    if UsuarioPago > TotalPagoIVA:
        Cambio = UsuarioPago - TotalPagoIVA
        print("--- ¡Pago realizado con exito! ---")
        print(f"Tu cambio es de: ${Cambio}")
    else:
        if UsuarioPago == TotalPagoIVA:
            print("--- ¡Pago realizado de forma exitosa! ---")
            print("Tu cambio es de $0.00")