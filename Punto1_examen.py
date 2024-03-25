import random

inventario = []

def generar_id():
    return random.randint(1, 100)

def registrar_producto():
    print("Registro de Producto")
    nombre = input("Ingrese el nombre del producto: ")

    while True:
        precio_str = input("Ingrese el precio unitario del producto: ")
        if not all(char.isdigit() or char == '.' for char in precio_str):
            print("Precio inválido. Ingrese solo valores numéricos.")
        else:
            try:
                precio = float(precio_str)
                break
            except ValueError:
                print("Precio inválido. Ingrese solo valores numéricos.")

    descripcion = input("Ingrese la descripción del producto: ")
    casa = input("Ingrese la casa a la que pertenece el producto (Drama, Accion, Superheroes, etc): ")
    referencia = input("Ingrese la referencia del producto (código alfanumérico): ")
    pais_origen = input("Ingrese el país de origen del producto: ")
    garantia_extendida = input("El producto tiene garantía extendida (true/false): ").lower() == "true"

    while True:
        ubicacion = input("Ingrese la ubicación del producto (A, B, C o D): ").upper()
        if ubicacion not in ['A', 'B', 'C', 'D']:
            print("Ubicación no válida. Por favor ingrese A, B, C o D.")
        else:
            unidades_existentes = sum(producto['unidades_compradas'] for producto in inventario if producto['ubicacion'] == ubicacion)
            nuevas_unidades = int(input(f"Ingrese el número de unidades compradas del producto para la ubicación {ubicacion}: "))
            if unidades_existentes + nuevas_unidades > 50:
                print(f"No hay suficiente espacio en la ubicación {ubicacion} para almacenar {nuevas_unidades} unidades. Solo se almacenarán {50 - unidades_existentes} unidades.")
                nuevas_unidades = 50 - unidades_existentes
                ubicacion_resto = input("Ingrese la ubicación para almacenar las unidades restantes: ").upper()
                while ubicacion_resto not in ['A', 'B', 'C', 'D']:
                    print("Ubicación no válida. Por favor ingrese A, B, C o D.")
                    ubicacion_resto = input("Ingrese la ubicación para almacenar las unidades restantes: ").upper()

                unidades_resto = nuevas_unidades - (50 - unidades_existentes)
                producto_resto = {
                    'id': generar_id(),
                    'nombre': nombre,
                    'precio': precio,
                    'ubicacion': ubicacion_resto,
                    'descripcion': descripcion,
                    'casa': casa,
                    'referencia': referencia,
                    'pais_origen': pais_origen,
                    'unidades_compradas': unidades_resto,
                    'garantia_extendida': garantia_extendida
                }
                inventario.append(producto_resto)
                break
            else:
                break

    producto = {
        'id': generar_id(),
        'nombre': nombre,
        'precio': precio,
        'ubicacion': ubicacion,
        'descripcion': descripcion,
        'casa': casa,
        'referencia': referencia,
        'pais_origen': pais_origen,
        'unidades_compradas': nuevas_unidades,
        'garantia_extendida': garantia_extendida
    }
    inventario.append(producto)

    print("Producto registrado con éxito.")


def mostrar_todos_los_productos():
    if not inventario:
        print("No hay productos registrados.")
    else:
        print("Listado de Productos:")
        for producto in inventario:
            print("ID:", producto['id'])
            print("Nombre:", producto['nombre'])
            print("Precio unitario:", producto['precio'])
            print("Descripción:", producto['descripcion'])
            print("Casa:", producto['casa'])
            print("Referencia:", producto['referencia'])
            print("País de Origen:", producto['pais_origen'])
            print("Unidades Compradas:", producto['unidades_compradas'])
            print("Garantía Extendida:", producto['garantia_extendida'])
            print("")

def buscar_producto_por_nombre(nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            print("ID:", producto['id'])
            print("Nombre:", producto['nombre'])
            print("Precio unitario:", producto['precio'])
            print("Descripción:", producto['descripcion'])
            print("Casa:", producto['casa'])
            print("Referencia:", producto['referencia'])
            print("País de Origen:", producto['pais_origen'])
            print("Unidades Compradas:", producto['unidades_compradas'])
            print("Garantía Extendida:", producto['garantia_extendida'])
            print("")
            break
    else:
        print("Producto no encontrado")

def modificar_unidades_compradas(nombre, nuevas_unidades):
    for producto in inventario:
        if producto['nombre'] == nombre:
            if nuevas_unidades <= producto['unidades_compradas']:
                producto['unidades_compradas'] = nuevas_unidades
                print("Número de unidades compradas actualizado con éxito.")
            else:
                print("El nuevo número de unidades compradas no puede ser mayor al número inicial.")
            break
    else:
        print("Producto no encontrado")

def eliminar_producto(nombre):
    for i, producto in enumerate(inventario):
        if producto['nombre'] == nombre:
            print("ID:", producto['id'])
            print("Nombre:", producto['nombre'])
            confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ")
            if confirmacion.lower() == 's':
                del inventario[i]
                print("Producto eliminado con éxito.")
            break
    else:
        print("Producto no encontrado")

def mostrar_menu():
    print("1. Registrar un producto")
    print("2. Mostrar todos los productos en bodega")
    print("3. Buscar y mostrar un producto por nombre")
    print("4. Modificar el número de unidades compradas de un producto")
    print("5. Eliminar un producto del inventario")
    print("6. Salir")

def principal():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_todos_los_productos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto_por_nombre(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a modificar: ")
            nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
            modificar_unidades_compradas(nombre, nuevas_unidades)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "6":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    principal()

    

