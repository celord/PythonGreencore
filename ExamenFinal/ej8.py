"""
Escriba un codigo que le permita al usuario ingresar una palabra
y el codigo busque palabras relacionadas en un archivo de texto,
para mostrarsela al usuario.
"""

from io import open
fname = 'listado-general.txt'
listado = open(fname, 'r', encoding="utf-8")
datos = listado.readlines()
listado.close()


def buscarPalabra(p,datos):
	for i in datos:
		i.strip().split('\n')
		if i.startswith(p):
			print(i)


p = input("Digite la palabra a buscar: ")
buscarPalabra(p,datos)