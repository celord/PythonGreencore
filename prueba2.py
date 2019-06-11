def entradaProducto():
    entrada = ""
    entrada = input(("Introduce un nombre de producto (0 finalizada) #{}: ".format(len(productos) + 1))).strip()
    if entrada == "":
        print("\tEl producto no puede ser vacio")
    if entrada in productos:
        print("\tEste pruducto ya existe")

    return entrada

def entradaExistensia():
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Introduce la cantidad en stock: "))
        except:
            print("\tError no es un entero")

        return numero
#dic que conti los productos
productos={}
#lista que contendra todos los productos con una cantidad menor a la media
menores=[]
print("\tIntroduce los productos")
print("...................")

while True:
    producto = entradaProducto()
    if producto == "0":
        break
    existencia = entradaExistensia()
    productos[producto] = existencia

if len(productos):
    print("\tListado de productos ananidos")
    print("................................")
    #mostramos lo productos y obtenemos la suma total
    suma = 0
    for i in productos:
        suma += productos[i]
        print("Producto '{}' Cantidad: {}".format(i, productos[i]))
    #solo mostramos la media si hay mas de u producto

    if len(productos) > 1:
        #Calculamos el promedio
        promedio = float(suma / len(productos))
        print("\nEl promedio es: {}".format(promedio))
        print("\nlos productos con cantidad inferior al promedio son: ")
        print("......................................................")
        #buscamos los productos con cantidad inferior a la media
        menores = list(filter(lambda x: productos[x] < promedio, productos))
        for i in menores:
            print("Producto: '{}'".format(i))