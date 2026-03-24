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
while opcion != 4:

    # Menú de opciones disponibles para el usuario
    print("""Elija la opcion deseada:
        1. Agregar producto
        2. Mostrar inventario
        3. Calcular estadisticas
        4. Salir
    """)

    # Validación de la entrada del menú, evita que el programa crashee con letras
    
    try:
        opcion = int(input("Ingrese la opcion (1-4): "))
    except ValueError:
        print("Error: Ingresa un valor numerico.\n")
        continue

    # Ejecución de la función según la opción elegida
    if opcion == 1:
        agregar_producto(inventario)

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        calcular_estadisticas(inventario)

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Por favor, ingrese una opcion entre 1 y 4.\n")

# Objetivo de la semana: construir un sistema de gestión de inventario en Python
# aplicando listas, diccionarios, funciones, modularización y manejo de errores.