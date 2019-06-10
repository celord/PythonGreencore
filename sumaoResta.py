def sumaOResta(a,b,c):
    if c == 1:
        return a + b
    if c == 0:
        return a - b
    if c == 2:
        return a * b
    if c == 3:
        return a / b

while True:
    c = input("Seleccione una operacion: Suma[s] , Resta[r], Multiplicacion[m], Division[d]")
    if ( c == 's') or (c == 'r') or (c == 'm') or (c == 'd'):
        break
    else:
        print('Error solo se puede sumar, restar, multiplicar o dividir')

while True:
    try:
        a = int(input("Ingrese primer valor"))
        break

    except ValueError:
        print("Valor incorrecto")

while True:
    try:
        b = int(input("Ingrese segundo valor"))
        break

    except ValueError:
        print("Valor incorrecto")


if c == 's':
    print(sumaOResta(a,b,1))

if c == 'r':
    print(sumaOResta(a,b,0))
if c == 'm':
    print(sumaOResta(a,b,2))
if c == 'd':
    try:

        print(sumaOResta(a,b,3))
    except ZeroDivisionError:
        print("No se puede dividir entro 0")
