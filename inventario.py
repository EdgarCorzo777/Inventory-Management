# Importación de las funciones definidas en el archivo funciones.py
from funciones import agregar_producto, mostrar_inventario, calcular_estadisticas

<<<<<<< HEAD
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
=======
# Bucle para validar que el precio sea numérico y mayor a cero
while True:
    try:
        # Solicita el precio y lo convierte a número decimal
        precio = float(input("Ingrese el precio del producto: $"))
        if precio > 0:
            # Si el precio es válido, sale del bucle
            break
        else:
            # Si el precio es cero o negativo, muestra un mensaje y repite el bucle
            print("Error: Ingrese un precio valido.")
    except ValueError:
        # Si ingresa un dato no numérico, muestra un mensaje y repite el bucle
        print("Error: Ingresar solo valores numericos")

# Bucle para validar que la cantidad sea numérica y mayor a cero
while True:
    try:
        # Solicita la cantidad y la convierte a número entero
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad > 0:
            # Si la cantidad es válida, sale del bucle
            break
        else:
            # Si la cantidad es cero o negativa, muestra un mensaje y repite el bucle
            print("Error: Ingrese una cantidad valida.")
    except ValueError:
        # Si ingresa un dato no numérico, muestra un mensaje y repite el bucle
        print("Error: Ingresar solo valores numericos")

# Calcula el costo total multiplicando precio por cantidad
costo_total = precio * cantidad
>>>>>>> 611818f8a382edb6c7820725a60513fb86c04e30

    elif opcion == 2:
        mostrar_inventario(inventario)

<<<<<<< HEAD
    elif opcion == 3:
        calcular_estadisticas(inventario)

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Por favor, ingrese una opcion entre 1 y 4.\n")

# Objetivo de la semana: construir un sistema de gestión de inventario en Python
# aplicando listas, diccionarios, funciones, modularización y manejo de errores.
=======
# Este programa solicita el nombre, precio y cantidad de un producto. Valida que ambos
# valores sean numéricos y mayores a cero mediante bucles con manejo de excepciones.
# Luego calcula el costo total y muestra un resumen con todos los datos formateados.
>>>>>>> 611818f8a382edb6c7820725a60513fb86c04e30
