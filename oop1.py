class Person(object):
    "Clase Representa una persona"
    def __init__(self,identificacion,nombre,apelllido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apelllido = apelllido
    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion), self.apelllido, self.nombre)