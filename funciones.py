def agregar_producto(inventario):
    # Solicita el nombre del producto sin validación, acepta cualquier texto
    nombre_producto = input("Ingrese el nombre del producto: ")

    x = 1

    # Validación del precio, repite hasta que el usuario ingrese un número
    while x:
        try:
            precio_producto = int(input("Ingrese el precio del producto: $"))
            break
        except ValueError:
            print("Error: Ingrese un valor numerico.")

    # Validación de la cantidad, repite hasta que el usuario ingrese un número
    while x:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numerico.")

    # Construcción del diccionario con los datos del producto
    producto = {}
    producto["nombre"] = nombre_producto
    producto["precio"] = precio_producto
    producto["cantidad"] = cantidad_producto

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
    # Calcula el valor total multiplicando precio por cantidad de cada producto
    precio_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    # Suma la cantidad total de unidades en el inventario
    cantidad_total = sum(p['cantidad'] for p in inventario)
    print(f"Valor total del inventario: ${precio_total}")
    print(f"Cantidad total de productos: {cantidad_total}")