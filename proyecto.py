'''
Universidad Fidelitas
Programación Básica

Proyecto: Sistema de estadía y servicios de un hospital privado
Autores : Brandon Sánchez Porras, Evan Marín Jimenez
'''

roomCost = 0
serviceCost = 0
drugsCost = 0
totalBill = 0


def login():
    user1 = "Admin1"
    user2 = "Admin2"

    password1 = "Sanchez"
    password2 = "Marin"

    print("Bienvenid@ al sistema de estadía y servicio del Hospital #####")

    while True:
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if user == user1 and password == password1:
            print("Bienvenid@,", user1)
            break
        elif user == user2 and password == password2:
            print("Bienvenid@,", user2)
            break
        else:
            print("El nombre de usuario o contraseña ingresado es incorrecto")
            continue


def menu():
    print("Estadia en el Hospital (a)")
    print("Servicio del Hospital  (b)")
    print("Farmacia               (c)")
    print("Cajas                  (d)")

    while True:
        answer = ""
        answer = input("En qué le podemos ayudar? (a,b,c,d) > ")
        if answer == "Estadia en el Hospital" or answer == "a":
            roomChooser()
            break
        elif answer == "Servicio del Hospital" or answer == "b":
            service()
            break
        elif answer == "Farmacia" or answer == "c":
            drugs()
            break
        elif answer == "Cajas" or answer == "d":
            checkout()
            break
        else:
            print("La opción seleccionada no existe, por favor intente de nuevo")
            continue


def rooms():
    print("Contamos con habitaciones muy bien equipadas para las necesidades de los pacientes.")
    print("A continuacion se muestran las habitaciones disponibles:")

    for i in range(0, 30, 3):
        print(i)


def roomChooser():
    room = ""
    # while room not in range(0,30,3):
    while True:
        rooms()
        room = int(input("Seleccione un número de habitación: "))
        if room in range(0, 30, 3):
            print("Perfecto!")
            break
        else:
            print(
                "La habitación seleccionada no se encuentra disponible, por favor intente de nuevo.")
            continue


def service():
    print("WIP")


def drugs():
    print("WIP")


def checkout():
    print("WIP")


# ------------------MAIN-------------------

login()
menu()
