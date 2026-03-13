# Solicita al usuario el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

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

# Muestra un resumen con el nombre, precio, cantidad y total
print(f"\nProducto: {nombre} | Precio: ${precio:.3f} | Cantidad: {cantidad} | Total: ${costo_total:.3f}")

# Este programa solicita el nombre, precio y cantidad de un producto. Valida que ambos
# valores sean numéricos y mayores a cero mediante bucles con manejo de excepciones.
# Luego calcula el costo total y muestra un resumen con todos los datos formateados.