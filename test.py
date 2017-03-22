import os

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

carpeta = os.path.dirname(path+account)

if not os.path.exists(carpeta):
    os.makedirs(carpeta)

existe = False
try:
    fh = open(path+account,'r')
except:
    fh = open(path+account,'w')
    existe = False

