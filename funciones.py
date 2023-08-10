from Funcion_PDF import *
from Datos_estaticos import *
from Funcion_PDF2 import *
import datetime
listaNombres = []
listaCorreo = []
ListaClientes = []

Password = "CAML890915R77"
def menu():
    opcion = 1
    while(opcion!=0):
        print("1. Ingresar datos")
        print("2. Mostrar clientes registrados")
        print("3. Generar Ticket del cliente")
        print("4. Lista de productos")
        print("5. Agregar productos al carrito")
        print("6. Total del pago (incluye IVA)")
        print("7. Imprimir Historial")
        print("0. Salir")
        opcion = int(input("Elije una opcion: "))
        if(opcion==1):
            pedirDatos()
        elif (opcion==2):
            if not ListaClientes:
                print("No hay clientes aún. Registre uno. ")
            else:
                imprimirDatos()
        elif (opcion==3):
            if not ListaClientes:
                print("No hay clientes aún. Registre uno. ")
            else:
                select = int(input("Seleccione el cliente para imprimir su ticket: "))
                if 0 <= select <len(ListaClientes):
                    GenerarTicket(ListaClientes[select])
                else:
                    print("--- Cliente No encontrado ---")
        elif (opcion==4):
            Contra = input("Si quieres ver un producto, debes ingresar la contraseña del gerente: ")
            if (Contra==Password):
                print("----- Productos Disponibles -----")
                print("=========================================")
                Inventario()
            else:
                print("Contraseña Incorrecta, intentalo más tarde")
        elif (opcion==5):
            if not ListaClientes:
                print("No hay clientes aún. Registre uno. ")
            else:
                imprimirDatos()
                for cliente in ListaClientes:
                    CarritoCompras(cliente)
        elif (opcion==6):
            if not ListaClientes:
                print("No hay clientes aún. Registre uno")
            else:
                for cliente in ListaClientes:
                    RealizarPago(cliente)
        elif (opcion==7):
            if not ListaClientes:
                print("No hay clientes aún. Registre uno")
            else:
                HistorialPDF(ListaClientes)
            


def pedirDatos():
    listaNombres = input("Ingresa tu nombre: ")
    listaCorreo = input("Ingresa tu correo: ")
    ListaClientes.append({'Nombre':listaNombres, 'Correo':listaCorreo, 'Carrito': []})
    print("------- Cliente registrado -------")

def imprimirDatos():
    print('{:<35} {:<30}'.format(" |Nombre| ", "|Correo electrónico| "))
    for cliente in ListaClientes:
        print('{:<35} {:<30}'.format(f"{cliente['Nombre']}", f"{cliente['Correo']}"))

def Inventario():
    print('{:<10} {:<15} {:<45} {:<35}'.format("|No.|", "|Marca|", "|Nombre del producto|", "|Precio|"))
    for i,producto in enumerate(productos_disponibles):
        print('{:<10} {:<15} {:<45} {:<35}'.format(f"{i+1}.", f"{producto['Marca']}", f"{producto['NombreProducto']}", f"${producto['PrecioProducto']}"))

def CarritoCompras(cliente):
    print(f"\nCliente: {cliente['Nombre']}")
    Inventario()
    opcion2 = 1
    while opcion2 == 1:
        select = int(input("Seleccione Cualquier producto de la lista: "))-1
        if 0<= select < len(productos_disponibles):
            
            cliente['Carrito'].append(productos_disponibles[select])
            print("--- Producto Guardado con Exito ---")
            print(f"{cliente['Carrito']}")
        else:
            print("--- Producto no disponible o selección invalida ---")
        
        opcion2= int(input("¿Quieres comprar algo más? 1.Si 2.No \n"))

 
def PagoProducto(carrito):
    SubTotal = sum(producto['PrecioProducto'] for producto in carrito)
    IVA = SubTotal * 0.16
    Total = SubTotal + IVA
    return Total

def RealizarPago(cliente):
    print(f"---- Carrito de {cliente['Nombre']} ----")
    print('{:<25} {:<45} {:<35}'.format("|Marca del producto|","|Nombre del producto|","|Precio|"))
    for producto in cliente['Carrito']:
        print('{:<25} {:<45} {:<35}'.format(f"{producto['Marca']}", f"{producto['NombreProducto']}", f"${producto['PrecioProducto']}"))
                
    PagoTotal = PagoProducto(cliente['Carrito'])
    print(f"El total a pagar con todo e intereses es: ${PagoTotal}")
    print("--- Genera tu ticket para realizar el pago correspondiente ---")
            print("Tu cambio es de $0.00")
