"""

    Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como diccionario.
    Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

"""
from io import open



def abrirArchivo(fname):
	archivo = open(fname, 'r', encoding="utf-8")
	datos = archivo.readlines()
	archivo.close()
	return datos


def cargar_datos(datos):

	personas = {}
	for i in datos:
		personas[str(i.strip().split(':')[0])] = i.strip().split(':')[1]

	return personas

def guardar_datos(datos):
	archivo = open(fname, 'a+', encoding="utf-8")
	#archivo.write('\n')
	archivo.write(datos)
	archivo.close()

fname = 'eje5datos.txt'
guardar_datos('\n5:Ana')
dat = abrirArchivo(fname)
print(cargar_datos(dat))




