IVA = 0.13
producto = input("Ingrese el Prodcuto: ")
cantidad = int(input("Ingrese la cantidad de producto: "))
precio_unitario = int(input("Ingrese el precio unitario: "))

subTotal = cantidad * precio_unitario
impuesto = subTotal * IVA
Total = subTotal + impuesto

print("Subtotal: %s" % str(subTotal))
print("Imp: %s" % str(impuesto))
print("Total: %s" % str(Total))

