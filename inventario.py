# Importación de las funciones definidas en el archivo funciones.py
from funciones import *
from archivos import *

# Encabezado visual del programa
print("=" * 30)
print("| 📦 INVENTORY MANAGEMENT 📦 |")
print("=" * 30)
print()

opcion = 0

# Lista que almacena todos los productos del inventario
inventario = []

# Bucle principal del menú, se ejecuta hasta que el usuario elija salir
while opcion != 9:

    # Menú de opciones disponibles para el usuario
    print("""Elija la opcion deseada:
        1. Agregar producto
        2. Mostrar inventario
        3. Buscar producto
        4. Actualizar productos
        5. Eliminar productos
        6. Calcular estadisticas
        7. Guardar CSV
        8. Cargar CSV
        9. Salir
    """)

    # Validación de la entrada del menú, evita que el programa crashee con letras
    
    try:
        opcion = int(input("Ingrese la opcion (1-9): "))
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
        x = 1
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        if buscar_producto(inventario, nombre) is None:
            print("Producto no encontrado")
        else:
            while x:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))

                    if nuevo_precio <= 0:
                        print("Error: Ingrese un valor mayor a cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un valor numerico")
            
            while x:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                    if nueva_cantidad <= 0:
                        print("Error: Ingrese un valor mayor a cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un valor numerico")
        
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
        ruta = input("Ingrese la ruta donde desea guardar el archivo: (ej: productos.csv) ")
        guardar_csv(inventario, ruta)
         
    elif opcion == 8:
        ruta = input("Ingrese la ruta del archivo CSV a cargar: ")
        resultado = cargar_csv(ruta)

        if resultado is None:
            pass
        else:
            productos_cargados, errores = resultado

            opcion_carga = input("¿Deseas sobreescribir el inventario actual? (S/N): ").upper()

            if opcion_carga == "S":
                inventario.clear()
                inventario.extend(productos_cargados)
            else:
                for p in productos_cargados:
                    existe = buscar_producto(inventario, p["nombre"])

                    if existe:
                        existe["cantidad"] += p["cantidad"]
                        existe["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                    
                print(f"Productos cargados: {len(productos_cargados)}")
                print(f"Filas invalidas omitidas: {errores}")

    elif opcion == 9:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Por favor, ingrese una opcion entre 1 y 9.\n")

# Objetivo de la semana: construir un sistema de gestión de inventario en Python
# aplicando listas, diccionarios, funciones, modularización y manejo de errores.