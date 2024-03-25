def ingresar_frutas():
    frutas = []
    n = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    for i in range(1, n+1):
        print(f"Ingrese los datos de la fruta {i}:")
        id_fruta = input("ID: ")
        nombre = input("Nombre: ")
        precio_unitario = float(input("Precio Unitario: "))
        cantidad = int(input("Cantidad: "))
        fruta = {'id': id_fruta, 'nombre': nombre, 'precio_unitario': precio_unitario, 'cantidad': cantidad}
        frutas.append(fruta)
    return frutas

def costo_total(frutas):
    total = sum(fruta['precio_unitario'] * fruta['cantidad'] for fruta in frutas)
    return total

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=lambda x: x['precio_unitario'])
    return fruta_barata

def main():
    frutas = ingresar_frutas()
    print("\nCosto total del salpicón:", costo_total(frutas))
    print("\nFrutas ordenadas de mayor a menor costo:")
    mostrar_frutas_ordenadas(frutas)
    print("\nFruta más barata:")
    fruta = fruta_mas_barata(frutas)
    print(f"ID: {fruta['id']}, Nombre: {fruta['nombre']}, Precio Unitario: {fruta['precio_unitario']}, Cantidad: {fruta['cantidad']}")

if __name__ == "__main__":
    main()
