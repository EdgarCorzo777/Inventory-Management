# Solicita al usuario el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Bucle infinito para validar que precio y cantidad sean valores numéricos
while True:
    try:
        # Solicita el precio y lo convierte a número decimal
        precio = float(input("Ingrese el precio del producto: $"))
        # Solicita la cantidad y la convierte a número entero
        cantidad = int(input("Ingrese la cantidad del producto: "))
        # Si ambos valores son válidos, sale del bucle
        break
    except ValueError:
        # Si ingresa un dato no válido, muestra un mensaje y repite el bucle
        print("Error: Ingresar solo valores numericos")

# Calcula el costo total multiplicando precio por cantidad
costo_total = (precio * cantidad)

# Muestra un resumen con el nombre, precio, cantidad y total
print(f"\nProducto: {nombre} | Precio: ${precio:.3f} | Cantidad: {cantidad} | Total: ${costo_total:.3f}")

# Este programa solicita el nombre, precio y cantidad de un producto. Valida que el precio
# y la cantidad sean valores numéricos mediante un bucle con manejo de excepciones. Luego
# calcula el costo total y muestra un resumen con todos los datos formateados.