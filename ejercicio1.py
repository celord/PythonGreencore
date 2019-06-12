"""
Transforma cada fila en un diccionario y lo agrege a una lista

"""
from io import open

fname = 'personas.txt'
f = open(fname,'r', encoding="utf-8")
lineas = f.readlines()
f.close()

personas = []
for linea in lineas:
    campos = linea.replace("\n","").split(':')
    persona = {'id':campos[0],'nombre':campos[1],
                'apellido':campos[2], 'fecha':campos[3]}
    personas.append(persona)


for p in personas:
    print("(id={}) {} => {}".format(p['id'], p['nombre'],
                               p['apellido'],p['fecha']) )