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

    if not ruta.endswith(".csv"):
        print("Error: El archivo debe tener extension .csv")
        return

    try:
        with open(ruta, "r") as archivo:
            lector = csv.reader(archivo)

            header = next(lector)
            if header != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo no tiene el formato correcto")
                return
            
            productos = []
            errores = 0

            for fila in lector:
                if len(fila) != 3:
                    errores += 1
                    continue  

                try:
                    precio = float(fila[1])
                    cantidad = int(fila[2])
    
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue
        
                except ValueError:
                    errores += 1
                    continue

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
        print(f"Error inesperado: {e}")


