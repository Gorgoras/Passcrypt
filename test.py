import os


def comienzo():
    account = input("Nombre de la cuenta: ")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    print("Se grabara en la cuenta " + account + ", nombre de usuario: " + username + " password: " + password + ".")

    rta = input("Es correcto? [Y/n]: ")

    while rta not in ('Y', 'n'):

        rta = input("Es correcto? [Y/n]: ")

    if rta == 'n':
        quit()


    path = os.getcwd()

    carpeta = os.path.dirname(path + "\\" + account)

    print("Intentando abrir carpeta...")
    if not os.path.exists(carpeta):
        print("No existe, creando carpeta...")
        os.makedirs(carpeta)

    existe = False
    try:
        fileConPass = open(path+ "\\" + account,'r+')
        existe = True
    except:
        fileConPass = open(path+ "\\" + account, "w")
        existe = False

    reemplazo = False
    if existe:
        rta = input("Ya existe una cuenta con ese nombre, desea reemplazarla? [Y/n]: ")
        while rta not in ('Y', 'n'):
            rta = input("Ya existe una cuenta con ese nombre, desea reemplazarla? [Y/n]: ")
        if rta == 'Y':
            reemplazo = True
        if rta == 'n':
            #logica para mostrar user y pass en el archivo actual
            quit()

    if reemplazo:
        fileConPass = open(path+ "\\" + account, "w")
    else:
        quit()

    try:
        fileConPass.write(username + ";" + password)
        print("Se guardaron los datos con exito en " + fileConPass.name)
    except:
        print("Ocurrio un error al grabar el archivo.")
    return "";


comienzo()
