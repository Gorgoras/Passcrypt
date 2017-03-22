<<<<<<< HEAD
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




#def ensure_dir(file_path):
#    directory = os.path.dirname(file_path)
#    if not os.path.exists(directory):
#        os.makedirs(directory)

=======
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




#def ensure_dir(file_path):
#    directory = os.path.dirname(file_path)
#    if not os.path.exists(directory):
#        os.makedirs(directory)

>>>>>>> 24f76d62dbfedf799817c26aa151ab6c6af97afb
