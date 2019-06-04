import random


descuentos = {'blanco': 0,'amarillo': 0.10,'azul':0.15,'verde':0.30,'rojo':0.50}

totalCompras = int(input("Engrese el total de sus compras: "))

def rifaDescuento(monto):
    color, descuento =random.choice(list(descuentos.items()))
    print(color, descuento)
    print("Tiene un descuento %s " % color)
    nuevoMonto = monto - monto*descuento
    print("Ahora debe pagar %s " % nuevoMonto)


if totalCompras >100:
    print("Se merese un descuento")
    rifaDescuento(totalCompras)

elif totalCompras == 0:
    print("Favor ingrese un monto valido")

elif totalCompras < 100:
    print("Gracias por su compra!!!")
    print(" Debe pagar %s" % totalCompras)