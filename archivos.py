cadena1 = 'Datos' #declara cadena 1
cadena2 = 'Secretos' #declara cadena 2

#Abre archivo para escribir
archivo = open('datos1.txt','w')

#Escribe cadena1 anadiendo salto de linea
archivo.write(cadena1 + '\n')

#Escribe cadena2 en el archivo
archivo.write(cadena2 + '\n')

#cierra el archivo
archivo.close()

#Declara lista
lista = ['lunes' ,'martes', 'miercoles', 'jueves', 'viernes']

#abre archivo en modo escritura
archivo = open('datos2.txt', 'w')

#Escribe toda la lista en el archivo
archivo.writelines(lista)

#cierra el archivo
archivo.close()