#importa modulo pickle
import pickle
#Declara lista
lista =['Perl', 'Python', 'Ruby']
#abre archivo binario para escribir
archivo=open('lenguajes.dat','wb')
#Escribe lista en archivo
pickle.dump(lista,archivo)
archivo.close()
#Borra de memoria la lista
del lista
#Abre archivo binario para leer
archivo = open('lenguajes.dat','rb')
#carga lista desde archivo
lista = pickle.load(archivo)
#muestra lista
print(lista)
#cierra archivo
archivo.close()