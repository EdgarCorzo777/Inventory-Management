def agregar_producto(inventario):
    # Solicita el nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")

    # Un loop para verificar si el producto ya existe
    for i in inventario:
        if i["nombre"] == nombre_producto:
            print("El producto ya existe")
            return

    x = 1

    # Validación del precio, repite hasta que el usuario ingrese un número
    while x:
        try:
            precio_producto = input("Ingrese el precio del producto o 'salir' si desea volver al menu: ")

            if precio_producto == "salir":
                return
            else:
                precio_producto = float(precio_producto)
                if precio_producto <= 0:
                    print("Error: Ingrese un valor mayor a cero.")
                    continue
                break
        except ValueError:
            print("Error: Ingrese un valor numerico.")


    # Validación de la cantidad, repite hasta que el usuario ingrese un número
    while x:
        try:
            cantidad_producto = input("Ingrese la cantidad del producto o 'salir' si desea volver al menu: ")

            if cantidad_producto == "salir":
                return
            else:
                cantidad_producto = int(cantidad_producto)
                if cantidad_producto <= 0:
                    print("Error: Ingrese un valor mayor a cero.")
                    continue
                break
        except ValueError:
            print("Error: Ingrese un valor numerico.")

    # Construcción del diccionario con los datos del producto
    producto = {
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto
}


    # Agrega el producto a la lista del inventario
    inventario.append(producto)

def mostrar_inventario(inventario):
    # Verifica si el inventario está vacío antes de intentar mostrarlo
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
    else:
        # Recorre el inventario e imprime cada producto con su índice
        for i, p in enumerate(inventario, start=1):
            print(f"{i} Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto no encontrado")
        return

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print(f"Producto '{nombre}' actualizado correctamente.")


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto no encontrado")
        return
    
    inventario.remove(producto)
    print("Producto eliminado correctamente.")
    

def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
    else:
        valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
        unidades_totales = len(inventario)
        producto_mas_caro = inventario[0]

        for pp in inventario:
            if pp["precio"] > producto_mas_caro["precio"]:
                producto_mas_caro = pp
        
        producto_mayor_stock = inventario[0]

        for pc in inventario:
            if pc["cantidad"] > producto_mayor_stock["cantidad"]:
                producto_mayor_stock = pc


        print(f"Cantidad total de productos: {unidades_totales}")
        print(f"Valor total del inventario: ${valor_total}")
        print(f"Producto más caro: {producto_mas_caro['nombre']} - ${producto_mas_caro['precio']}")
        print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} - {producto_mayor_stock['cantidad']}")