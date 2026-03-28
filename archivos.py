import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    # validar inventario vacío
    if not inventario:
        print("\n Inventario vacío, no se puede guardar\n")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            # encabezado
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # escribir datos
            for producto in inventario:
                writer.writerow([
                    producto["product"],
                    producto["price"],
                    producto["quantity"]
                ])

        print(f"\n Inventario guardado en: {ruta}\n")

    except Exception as e:
        print(f"\n Error al guardar archivo: {e}\n")


def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            
            # leer encabezado
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("\n Encabezado inválido\n")
                return []

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    producto = {
                        "product": nombre,
                        "price": precio,
                        "quantity": cantidad,
                        "total_cost": precio * cantidad
                    }

                    inventario.append(producto)

                except ValueError:
                    errores += 1

        print(f"\n Productos cargados: {len(inventario)}")
        print(f" Filas inválidas omitidas: {errores}\n")

        return inventario

    except FileNotFoundError:
        print("\n Archivo no encontrado\n")
        return []

    except Exception as e:
        print(f"\n Error al leer archivo: {e}\n")
        return []