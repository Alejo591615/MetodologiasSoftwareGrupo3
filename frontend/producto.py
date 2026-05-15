from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["ID", "Nombre", "Precio", "Stock"]

def listarProductos():
    productos = Producto.listarProductos()
    
    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))    

def consultarProducto():
    id = input("Ingrese el ID del producto: ")
    
    producto = Producto.consultarProducto(id)
    
    if producto == None:
        print(f"Producto con ID {id} no existe")
        return
    
    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid")) 

def mostrarMenuDeProductos():
    separador = "--------------------------------------------------"
    bienvenida = "Alejandro y Leonardo"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
    }
    solicitud = "Ingrese una opción: "
    salida = False
    
    while True: 
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar producto\n3. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False
        
        if opcion == "3":
            limpiar()
            break
    
        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opcion: "
            limpiar()
            opciones.get(opcion)()
        else:
            solicitud = "Opción no válida. Ingrese una nueva opción: "
            limpiar()