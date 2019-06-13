"""
Modo sólo escritura posicionándose al final del archivo (a).
En este caso se crea el archivo, si no existe, pero en caso
de que exista se posiciona al final, manteniendo el contenido original.
Y agregar texto a su criterio
"""
def prepararArchivo(a):
	try:
		f = open(a,'a+')
		return f
	except:
		print('Error')

def agregarTexto(t):
	a = prepararArchivo('ej7.txt')
	a.write(t)
	a.close()

agregarTexto('Agreagado texto al final\n')

