from backend.excel import obtenerLibro, guardarHoja

libro = obtenerLibro()
titulo_hoja = "Productos"

def inicializarHoja():
    hoja = libro.create_sheet(title=titulo_hoja)

    hoja.column_dimensions["A"].width = 15
    hoja.column_dimensions["B"].width = 25
    hoja.column_dimensions["C"].width = 15
    hoja.column_dimensions["D"].width = 15

    cabeceras = ("Id", "Nombre", "Precio", "Cantidad")

    hoja.append(cabeceras)

    guardarHoja(hoja)

    return hoja

def obtenerHojaDeProductos():
    if titulo_hoja in libro.sheetnames:
        return libro[titulo_hoja]
    else:
        return inicializarHoja()