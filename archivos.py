import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        ruta (str): Ruta donde se guardará el archivo CSV.
        incluir_header (bool): Si es True, escribe el encabezado nombre,precio,cantidad.

    Retorna:
        None
    """
    # Verifica que el inventario no esté vacío antes de guardar
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
        return

    # Verifica que la ruta tenga extensión .csv
    if not ruta.endswith(".csv"):
        print("Error: El archivo debe tener extension .csv")
        return

    try:
        # Abre el archivo en modo escritura
        with open(ruta, "w", newline="") as archivo:
            escritor = csv.writer(archivo)

            # Escribe el encabezado si se indicó
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            # Escribe cada producto como una fila en el CSV
            for p in inventario:
                escritor.writerow([p['nombre'], p['precio'], p['cantidad']])

            print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: No tienes permisos para guardar en esa ruta")


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV y los retorna como lista de diccionarios.

    Parámetros:
        ruta (str): Ruta del archivo CSV a cargar.

    Retorna:
        tuple: (lista de productos válidos, cantidad de filas inválidas omitidas)
        None: Si ocurrió un error al abrir o leer el archivo.
    """
    # Verifica que la ruta tenga extensión .csv
    if not ruta.endswith(".csv"):
        print("Error: El archivo debe tener extension .csv")
        return

    try:
        # Abre el archivo en modo lectura
        with open(ruta, "r") as archivo:
            lector = csv.reader(archivo)

            # Lee y valida el encabezado
            header = next(lector)
            if header != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el formato correcto")
                return

            productos = []
            errores = 0

            # Recorre cada fila y valida su contenido
            for fila in lector:

                # Verifica que la fila tenga exactamente 3 columnas
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    # Convierte precio a float y cantidad a int
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Verifica que no sean negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                except ValueError:
                    # Si la conversión falla, cuenta como fila inválida
                    errores += 1
                    continue

                # Agrega el producto válido a la lista
                productos.append({
                    "nombre": fila[0],
                    "precio": precio,
                    "cantidad": cantidad
                })

            return productos, errores

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
    except UnicodeDecodeError:
        print("Error: El archivo tiene caracteres no válidos.")
    except ValueError:
        print("Error: El archivo tiene valores no válidos.")
    except Exception as e:
        print(f"Error inesperado: {repr(e)}")