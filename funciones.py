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
                precio_producto = int(precio_producto)
                if precio_producto < 0:
                    print("Error: Ingrese un valor mayor a cero.")
                    return
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
                if cantidad_producto < 0:
                    print("Error: Ingrese un valor mayor a cero.")
                    return
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

def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
    else:
        precio_total = sum(p['precio'] * p['cantidad'] for p in inventario)
        cantidad_total = len(inventario)

        print(f"Valor total del inventario: ${precio_total}")
        print(f"Cantidad total de productos: {cantidad_total}")