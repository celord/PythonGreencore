detonador = 1
usuarios = ['ana', 'mario']

while detonador>0:
    nuevoUsuario = input('Agregar usuarios: ')
    if nuevoUsuario == str(0):
        detonador = 0
    else:
        usuarios.append(nuevoUsuario)


    for nombres in usuarios:
        print(nombres)