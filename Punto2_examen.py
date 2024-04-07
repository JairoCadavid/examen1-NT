frutas = []


n = int(input("Ingrese el número de frutas: "))


for i in range(1, n+1):
    print(f"Ingrese los detalles de la fruta {i}:")
    id = input("ID: ")
    nombre = input("Nombre: ")
    precio_unitario = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    
    
    frutas.append({'id': id, 'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad})


costo_total = 0
for fruta in frutas:
    costo_total += fruta['precio_unitario'] * fruta['cantidad']
print(f"El costo total del salpicón es: {costo_total}")


def obtener_precio(fruta):
    return fruta['precio_unitario']

frutas.sort(key=obtener_precio, reverse=True)
print("Las frutas ordenadas de mayor a menor costo son:")
for fruta in frutas:
    print(f"{fruta['nombre']}: {fruta['precio_unitario']}")


fruta_mas_barata = min(frutas, key=obtener_precio)
print(f"La fruta más barata es: {fruta_mas_barata['nombre']} con un precio unitario de: {fruta_mas_barata['precio_unitario']}")

