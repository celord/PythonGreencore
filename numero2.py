while(True):
    try:
        n = float(input("Introduce un numero: "))

        print(n)
    except:
        print("Ha ocurrido un error, introduce bien el numero")
    else:
        print("Todo ha funcionado correctamente")
        break
    finally:
        print("Fin de la iteracion")