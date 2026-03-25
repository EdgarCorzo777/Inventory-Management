import csv

def guardar_csv(inventario, ruta, incluir_header=True):

    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
        return
    
    if not ruta.endswith(".csv"):
        print("Error: El archivo debe tener extension .csv")
        return
    
    try:
        with open(ruta, "w", newline="") as archivo:
            escritor = csv.writer(archivo)

            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                escritor.writerow([p['nombre'], p['precio'], p['cantidad']])
            
            print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print("Error: No tienes permisos para guardar en esa ruta")


def cargar_csv(ruta):
    try:
        with open(ruta, "r") as archivo:
            lector = csv.reader(archivo)

            header = next(lector)
            if header != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el formato correcto")
                return

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
    except UnicodeDecodeError:
        print("Error: El archivo tiene caracteres no válidos.")
    except ValueError:
        print("Error: El archivo tiene valores no válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")


