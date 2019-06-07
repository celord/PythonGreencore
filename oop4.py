class Vehiculo():

    def __init__(self,color,ruedas,transmision):
        self.color=color
        self.ruedas=ruedas
        self.transmision=transmision

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilidrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilidrada = cilidrada
        self.transmision = "automatica"

    
    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilidrada)
    
coche=Coche("azul",150,4,1200)
print(coche)
vehiculo=Vehiculo("rojo",4,"manual")
print(vehiculo)