from servicios import *
from archivos import *

opcion = 0

# Lista que almacena todos los productos del inventario
inventario = []

while opcion != 9:

    # Encabezado visual del programa
    print("=" * 30)
    print("| 📦 INVENTORY MANAGEMENT 📦 |")
    print("=" * 30)

    # Menú de opciones disponibles para el usuario
    print("""
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
            print("Producto no encontrado.")
        else:
            # Validación del nuevo precio
            while x:
                try:
                    nuevo_precio_input = input("Ingrese el nuevo precio o 'salir' para volver al menu: ")

                    if nuevo_precio_input == "salir":
                        break

                    nuevo_precio = float(nuevo_precio_input)
                    if nuevo_precio <= 0:
                        print("Error: Ingrese un valor mayor a cero.")
                        continue
                    break
                except ValueError:
                    print("Error: Ingrese un valor numerico.")

            # Solo pide la cantidad si no se ingresó 'salir' en el precio
            if nuevo_precio_input != "salir":
                # Validación de la nueva cantidad
                while x:
                    try:
                        nueva_cantidad_input = input("Ingrese la nueva cantidad o 'salir' para volver al menu: ")

                        if nueva_cantidad_input == "salir":
                            break

                        nueva_cantidad = int(nueva_cantidad_input)
                        if nueva_cantidad <= 0:
                            print("Error: Ingrese un valor mayor a cero.")
                            continue
                        break
                    except ValueError:
                        print("Error: Ingrese un valor numerico.")

                # Solo actualiza si no se ingresó 'salir' en la cantidad
                if nueva_cantidad_input != "salir":
                    actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == 5:
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        if buscar_producto(inventario, nombre) is None:
            print("Producto no encontrado.")
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

        if resultado != None:
            productos_cargados, errores = resultado

            opcion_carga = input("¿Deseas sobreescribir el inventario actual? (S/N): ").upper()

            if opcion_carga == "S":
                # Reemplaza el inventario completo con los productos cargados
                inventario.clear()
                inventario.extend(productos_cargados)
                accion = "Reemplazo"

            else:
                # Fusiona los productos cargados con el inventario actual
                print("Politica de fusion: se actualiza cantidad sumando y se actualiza el precio si difiere.")
                for p in productos_cargados:
                    existe = buscar_producto(inventario, p["nombre"])
                    if existe:
                        # Si el producto ya existe, suma cantidad y actualiza precio
                        existe["cantidad"] += p["cantidad"]
                        existe["precio"] = p["precio"]
                    else:
                        # Si no existe, lo agrega al inventario
                        inventario.append(p)
                accion = "Fusion"

            # Resumen de la operación de carga
            print(f"Accion realizada: {accion}")
            print(f"Productos cargados: {len(productos_cargados)}")
            print(f"Filas invalidas omitidas: {errores}")

    elif opcion == 9:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Por favor, ingrese una opcion entre 1 y 9.\n")