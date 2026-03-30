def agregar_producto(inventario):
    """
    Solicita al usuario los datos de un nuevo producto y lo agrega al inventario.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorna:
        None
    """
    # Solicita el nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")

    # Verifica que el nombre no esté vacío
    if nombre_producto == "":
        print("Error: El nombre del producto no puede estar vacio.")
        return

    # Verifica si el producto ya existe en el inventario
    for i in inventario:
        if i["nombre"] == nombre_producto:
            print("El producto ya existe")
            return

    x = 1

    # Validación del precio, repite hasta que el usuario ingrese un número válido
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

    # Validación de la cantidad, repite hasta que el usuario ingrese un número válido
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
    """
    Muestra todos los productos del inventario con su índice, nombre, precio y cantidad.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorna:
        None
    """
    # Verifica si el inventario está vacío antes de intentar mostrarlo
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
    else:
        # Recorre el inventario e imprime cada producto con su índice
        for i, p in enumerate(inventario, start=1):
            print(f"{i} Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por nombre.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a buscar.

    Retorna:
        dict: El diccionario del producto si existe, None si no.
    """
    # Recorre el inventario comparando el nombre de cada producto
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente en el inventario.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float, opcional): Nuevo precio del producto. Si es None, no se modifica.
        nueva_cantidad (int, opcional): Nueva cantidad del producto. Si es None, no se modifica.

    Retorna:
        None
    """
    # Busca el producto en el inventario
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto no encontrado")
        return

    # Actualiza el precio solo si se proporcionó un nuevo valor
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    # Actualiza la cantidad solo si se proporcionó un nuevo valor
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print(f"Producto '{nombre}' actualizado correctamente.")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a eliminar.

    Retorna:
        None
    """
    # Busca el producto en el inventario
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto no encontrado")
        return

    # Elimina el diccionario del producto de la lista
    inventario.remove(producto)
    print("Producto eliminado correctamente.")


def calcular_estadisticas(inventario):
    """
    Calcula y muestra estadísticas del inventario:
    
Cantidad total de productos
Valor total del inventario
Producto(s) más caro(s)
Producto(s) con mayor stock
"""
if len(inventario) == 0:
    print("El inventario está vacío.\n")
    return

    # Valor total del inventario
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)

    # Cantidad total de productos diferentes
    unidades_totales = len(inventario)

    # ==================== PRODUCTO(S) MÁS CARO(S) ====================
    if inventario:
        precio_max = max(p['precio'] for p in inventario)
        productos_mas_caros = [p for p in inventario if p['precio'] == precio_max]

        print(f"Cantidad total de productos: {unidades_totales}")
        print(f"Valor total del inventario: ${valor_total:,.2f}")

        print("\nProducto(s) más caro(s):")
        for p in productos_mas_caros:
            print(f"  • {p['nombre']} - ${p['precio']:,.2f}")

        # ==================== PRODUCTO(S) CON MAYOR STOCK ====================
        cantidad_max = max(p['cantidad'] for p in inventario)
        productos_mayor_stock = [p for p in inventario if p['cantidad'] == cantidad_max]

        print("\nProducto(s) con mayor stock:")
        for p in productos_mayor_stock:
            print(f"  • {p['nombre']} - {p['cantidad']} unidades")
