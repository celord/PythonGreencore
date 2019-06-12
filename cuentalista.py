#cuenta elementos de lista
cadenaPalabras = 'it was the best of times it was the worst of time'
cadenaPalabras += ' it was the age of wisdom it was the age of foolishness'

listaPalabas = cadenaPalabras.split()

frecuenciaPalabras = []

for w in listaPalabas:
    frecuenciaPalabras.append(listaPalabas.count(w))

print('Cadena\n' + cadenaPalabras + '\n')
print('Lista\n' + str(listaPalabas) + '\n')
print('Frecuencias \n' + str(frecuenciaPalabras)+ '\n')
print('Pares\n' + str(zip(listaPalabas, frecuenciaPalabras)))