mayoriaEdad = 18

edad = int(input("Cual es su edad ? "))

if edad >= 100:
    print("Usted deberia estar muuy viejo...")

elif edad >= mayoriaEdad:
    print("Usted es mayor de edad")

elif edad <= 0:
    print("Invalida")

else:
    print("Usted es menor de edad")