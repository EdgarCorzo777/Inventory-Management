# Importación de las funciones definidas en el archivo funciones.py
from funciones import *

# Encabezado visual del programa
print("=" * 30)
print("| 📦 INVENTORY MANAGEMENT 📦 |")
print("=" * 30)
print()

opcion = 0

# Lista que almacena todos los productos del inventario
inventario = []

# Bucle principal del menú, se ejecuta hasta que el usuario elija salir
while opcion != 7:

    # Menú de opciones disponibles para el usuario
    print("""Elija la opcion deseada:
        1. Agregar producto
        2. Mostrar inventario
        3. Buscar producto
        4. Actualizar productos
        5. Eliminar productos
        6. Calcular estadisticas
        7. Salir
    """)

    # Validación de la entrada del menú, evita que el programa crashee con letras
    
    try:
        opcion = int(input("Ingrese la opcion (1-7): "))
    except ValueError:
        print("Error: Ingresa un valor numerico.\n")
        continue

    # Ejecución de la función según la opción elegida
    if opcion == 1:
        agregar_producto(inventario)

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre = input("Digite el nombre del producto a buscar: ")
        resultado = buscar_producto(inventario, nombre)
        if resultado:
            print(f"Producto encontrado: {resultado['nombre']} | Precio: ${resultado['precio']} | Cantidad: {resultado['cantidad']}")
        else:
            print("Producto no encontrado.")

    elif opcion == 4: 
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        if buscar_producto(inventario, nombre) is None:
            print("Producto no encontrado")
        else:
            nuevo_precio_input = input("Ingrese el nuevo precio o Enter para dejarlo igual: ")
            nueva_cantidad_input = input("Ingrese la nueva cantidad o Enter para dejarla igual: ")
        
            nuevo_precio = int(nuevo_precio_input) if nuevo_precio_input != "" else None
            nueva_cantidad = int(nueva_cantidad_input) if nueva_cantidad_input != "" else None
        
            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        if buscar_producto(inventario, nombre) is None:
            print("Producto no encontrado")
        else:
            eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 7:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Por favor, ingrese una opcion entre 1 y 7.\n")

# Objetivo de la semana: construir un sistema de gestión de inventario en Python
# aplicando listas, diccionarios, funciones, modularización y manejo de errores.