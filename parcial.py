productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    'FS1230HD': ['Acer', 15.6, '4GB', 'DD', '500GB', 'Intel Core i3', 'integrada']
}


stock = {
    '8475HD': [387990, 10], 
    '2175HD': [327990, 4], 
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], 
    '123FHD': [290890, 32], 
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 
    'UWU131HD': [349990, 1], 
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    marca_lower = marca.lower()
    stock_total = 0
    
    for modelo, info in productos.items():
        if info[0].lower() == marca_lower:  # info[0] es la marca
            stock_total += stock[modelo][1]  # stock[modelo][1] es la cantidad
    
    print(f"El stock es: {stock_total}")



def busqueda_precio(precio_min, precio_max):
    computadores = []
    for codigo, datos_computador in stock.items():
        precio = datos_computador[0]
        stock = datos_computador[1]

        if precio_min <= precio <= precio_max and stock > 0:
            if codigo in productos:
                marca = productos[codigo][0]
                resultado = f"{marca}{codigo}"
                






while True:
    try:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = int(input("Elije una opcion"))
        if opcion == 1:
            marca= input("Cual es la marca?:")
            stock_marca(marca)
        elif opcion == 2:
            precio_min = int(input("Cual es el precio minimo?:\n"))
            precio_max = int(input("Cual es el precio maximo?:\n"))
            busqueda_precio(precio_min, precio_max)
        elif opcion == 3:
            print()
        elif opcion == 4:
            print("Adios")
            break
        else:
            print("Esa opcion no existe")
            continue
    except ValueError: 
        print("Error")
        break
