'''
Universidad Fidelitas
Programación Básica

Proyecto: Sistema de estadía y servicios de un hospital privado
Autores : Brandon Sánchez Porras, Evan Marín Jimenez
'''


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
        answer = input("En qué le podemos ayudar? (a,b,c,d) > ").lower()
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
    global roomList
    roomList = []

    print("Contamos con habitaciones muy bien equipadas para las necesidades de los pacientes.")
    print("A continuacion se muestran las habitaciones disponibles:")

    for i in range(1, 30, 3):
        roomList.append(i)

    print("-------------+-------------")
    print("  Habitación | Costo       ")
    print("-------------+-------------")
    for i in range(len(roomList)):
        print(f"{str(roomList[i]).zfill(2)}           |  ₡{roomList[i] * 10000}")
    print("-------------+-------------")


def roomChooser():
    room = 0
    # while room not in range(0,30,3):
    while True:
        rooms()
        room = int(input("Seleccione un número de habitación: "))
        if room in roomList:
            print(f"Perfecto! El total por la habitación es de ₡{room * 10000}")
            global roomCost
            roomCost = room * 10000
            continuar()
            break
        else:
            print(
                "La habitación seleccionada no se encuentra disponible, por favor intente de nuevo.")
            continue


def continuar():
    cont = int(input("Desea realizar otro trámite? (0 = no, 1 = sí) > "))
    if cont == 0:
        checkout()
    else:
        menu()


def service():
    print("WIP")


def drugs():
    print("WIP")


def checkout():
    print("WIP")


# ------------------MAIN-------------------

login()
menu()
