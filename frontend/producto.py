from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["ID", "Nombre", "Precio", "Stock"]

def solicitarProducto():
    nombre = input("Ingrese un nombre: ")
    id = input(f"Ingrese el ID de {nombre}: ")
    precio = input(f"Ingrese el precio de {nombre}: ")
    stock = input(f"Ingrese el stock de {nombre}: ")
    
    return (id, nombre, precio, stock)

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

def agregarProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Producto.crearProducto(*nuevo_producto)
    
    if producto_creado:
        print("Producto agregado exitosamente")
    else:
        print("Error agregando el producto")

def actualizarProducto():
    nuevo_producto = solicitarProducto()
    producto_actualizado = Producto.actualizarProducto(*nuevo_producto)
    
    if producto_actualizado:
        print("Producto actualizado exitosamente")
    else:
        print("Error: verifique que el producto con ese ID si existe")

def eliminarProducto():
    id = input("Ingrese el ID del producto: ")

    producto_eliminado = Producto.eliminarProducto(id)
    
    if producto_eliminado:
        print("Producto eliminado exitosamente")
    else:
        print("Error: verifique que el producto con ese ID si existe")

def mostrarMenuDeProductos():
    separador = "--------------------------------------------------"
    bienvenida = "Alejandro y Leonardo"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
        "3": agregarProducto,
        "4": eliminarProducto,
        "5": actualizarProducto,
    }
    solicitud = "Ingrese una opción: "
    salida = False
    
    while True: 
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar producto\n3. Agregar producto\n4. Eliminar producto\n5. Actualizar producto\n6. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False
        
        if opcion == "6":
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