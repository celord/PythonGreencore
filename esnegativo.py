#la funcion verifica si es negativo
def esneg(numero):
    #Devuelve true fal segun si es neg o no
    return (numero < 0)

lista5 = [-3,-2,0,-1,9,-5]


print(list(filter(esneg,lista5)))