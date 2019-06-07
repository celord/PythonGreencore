lista = [1,2,3,4,5]

try:
    lista[10]
except IndexError:
    print("No existe ese elemento")