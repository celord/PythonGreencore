"""
Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
"""


class Espejo(object):

	def __init__(self, cadena):
		self.cadena = cadena
		self.espejo = ' '.join(cadena.split()[::-1])


	def __str__(self):
		return  'Frase original: {}\nFrase Espejo: {}'.format(self.cadena, self.espejo)


cadena = "Mi Diario Python"
a = Espejo(cadena)
print(a)


