archivo = open('texto.txt','w')
archivo.write('Hola')
archivo.close()

archivo = open('texto.txt','r')
archivo.read()
archivo.close()

archivo = open('texto.txt','r')
for linea in archivo.readlines():
    print(linea)

archivo.close()

archivo = open("prueba.txt","a")
print(archivo.tell())
archivo.write("\nNueva linea.\nAqui\ty alla")
print(archivo.tell())
archivo.close()