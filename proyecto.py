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
        global user
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
            print("La habitación seleccionada no se encuentra disponible, por favor intente de nuevo.")
            continue


def continuar():
    cont = int(input("Desea realizar otro trámite? (0 = no, 1 = sí) > "))
    if cont == 0:
        checkout()
    else:
        menu()


def service():
    answer = ''
    global costoCita
    global detallesCita

    print('Consulta General      (a) ₡30000')
    print('Revision Dental       (b) ₡40000')
    print('Electroencefalograma  (c) ₡150000')
    print('Electrocardiograma    (d) ₡150000')
    print('Revisión ginecologica (e) ₡30000')

    answer = input('En que podriamos ayudarle? (a,b,c,d,e)').lower()

    if answer == 'a':
        costoCita = 30000
        print('Necesitaremos algunos datos')
        name = input('Ingrese su nombre:')
        last_name = input('Ingrese su primer apellido:')

        print('Bienvenido', name, last_name)

        print("------+---------")
        print(" Dia  | Horario ")
        print("-----+----------")
        print('(a)Lunes  | 1pm')
        print('(b)Martes | 8am')
        print('(c)Viernes| 10am')
        print('(d)Sabado | 5pm')
        print("------+---------")

        cita = input('Ingrese el dia de la cita: (a,b,c,d)')

        while True:
            if cita == 'a':
                print('Perfecto')
                print('Su cita quedaria para el Lunes a la 1pm')
                detallesCita = f"Consulta General | {last_name}, {name} Lunes 1:00 PM"
                break

            elif cita == 'b':
                print('Perfecto')
                print('Su cita quedaria para el Martes a las 8am')
                detallesCita = f"Consulta General | {last_name}, {name} Martes 8:00 AM"
                break

            elif cita == 'c':
                print('Perfecto')
                print('Su cita quedaria para el Viernes a las 10am')
                detallesCita = f"Consulta General | {last_name}, {name} Viernes 10:00 AM"
                break

            elif cita == 'd':
                print('Perfecto')
                print('Su cita quedaria para el Sabado a las 5pm')
                detallesCita = f"Consulta General | {last_name}, {name} Sábado 5:00 PM"
                break
            else:
                print("La opción seleccionada no existe, por favor intente de nuevo")
                continue
    elif answer == 'b':
        costoCita = 40000
        print('Necesitaremos algunos datos')
        name = input('Ingrese su nombre:')
        last_name = input('Ingrese su primer apellido:')

        print('Bienvenido', name, last_name)

        print("------+---------")
        print(" Dia  | Horario ")
        print("-----+----------")
        print('(a)Lunes  | 1pm')
        print('(b)Martes | 8am')
        print('(c)Viernes| 10am')
        print('(d)Sabado | 5pm')
        print("------+---------")

        cita = input('Ingrese el dia de la cita: (a,b,c,d)')

        while True:
            if cita == 'a':
                print('Perfecto')
                print('Su cita quedaria para el Lunes a la 1pm')
                detallesCita = f"Revisión Dental | {last_name}, {name} Lunes 1:00 PM"
                break

            elif cita == 'b':
                print('Perfecto')
                print('Su cita quedaria para el Martes a las 8am')
                detallesCita = f"Revisión Dental | {last_name}, {name} Martes 8:00 AM"
                break

            elif cita == 'c':
                print('Perfecto')
                print('Su cita quedaria para el Viernes a las 10am')
                detallesCita = f"Revisión Dental | {last_name}, {name} Viernes 10:00 AM"
                break

            elif cita == 'd':
                print('Perfecto')
                print('Su cita quedaria para el Sabado a las 5pm')
                detallesCita = f"Revisión Dental | {last_name}, {name} Sábado 5:00 PM"
                break
            else:
                print("La opción seleccionada no existe, por favor intente de nuevo")
                continue
    elif answer == 'c':
        costoCita = 150000
        print('Necesitaremos algunos datos')
        name = input('Ingrese su nombre:')
        last_name = input('Ingrese su primer apellido:')

        print('Bienvenido', name, last_name)

        print("------+---------")
        print(" Dia  | Horario ")
        print("-----+----------")
        print('(a)Lunes  | 1pm')
        print('(b)Martes | 8am')
        print('(c)Viernes| 10am')
        print('(d)Sabado | 5pm')
        print("------+---------")

        cita = input('Ingrese el dia de la cita: (a,b,c,d)')

        while True:
            if cita == 'a':
                print('Perfecto')
                print('Su cita quedaria para el Lunes a la 1pm')
                detallesCita = f"Electroencefalograma | {last_name}, {name} Lunes 1:00 PM"
                break

            elif cita == 'b':
                print('Perfecto')
                print('Su cita quedaria para el Martes a las 8am')
                detallesCita = f"Electroencefalograma | {last_name}, {name} Martes 8:00 AM"
                break

            elif cita == 'c':
                print('Perfecto')
                print('Su cita quedaria para el Viernes a las 10am')
                detallesCita = f"Electroencefalograma | {last_name}, {name} Viernes 10:00 AM"
                break

            elif cita == 'd':
                print('Perfecto')
                print('Su cita quedaria para el Sabado a las 5pm')
                detallesCita = f"Electroencefalograma | {last_name}, {name} Sábado 5:00 PM"
                break
            else:
                print("La opción seleccionada no existe, por favor intente de nuevo")
                continue
    elif answer == 'd':
        costoCita = 150000
        print('Necesitaremos algunos datos')
        name = input('Ingrese su nombre:')
        last_name = input('Ingrese su primer apellido:')

        print('Bienvenido', name, last_name)

        print("------+---------")
        print(" Dia  | Horario ")
        print("-----+----------")
        print('(a)Lunes  | 1pm')
        print('(b)Martes | 8am')
        print('(c)Viernes| 10am')
        print('(d)Sabado | 5pm')
        print("------+---------")

        cita = input('Ingrese el dia de la cita: (a,b,c,d)')

        while True:
            if cita == 'a':
                print('Perfecto')
                print('Su cita quedaria para el Lunes a la 1pm')
                detallesCita = f"Electrocardiograma | {last_name}, {name} Lunes 1:00 PM"
                break

            elif cita == 'b':
                print('Perfecto')
                print('Su cita quedaria para el Martes a las 8am')
                detallesCita = f"Electrocardiograma | {last_name}, {name} Martes 8:00 AM"
                break

            elif cita == 'c':
                print('Perfecto')
                print('Su cita quedaria para el Viernes a las 10am')
                detallesCita = f"Electrocardiograma | {last_name}, {name} Viernes 10:00 AM"
                break

            elif cita == 'd':
                print('Perfecto')
                print('Su cita quedaria para el Sabado a las 5pm')
                detallesCita = f"Electrocardiograma | {last_name}, {name} Sábado 5:00 PM"
                break
            else:
                print("La opción seleccionada no existe, por favor intente de nuevo")
                continue
    elif answer == 'e':
        costoCita = 30000
        print('Necesitaremos algunos datos')
        name = input('Ingrese su nombre:')
        last_name = input('Ingrese su primer apellido:')

        print('Bienvenido', name, last_name)

        print("------+---------")
        print(" Dia  | Horario ")
        print("-----+----------")
        print('(a)Lunes  | 1pm')
        print('(b)Martes | 8am')
        print('(c)Viernes| 10am')
        print('(d)Sabado | 5pm')
        print("------+---------")

        cita = input('Ingrese el dia de la cita: (a,b,c,d)')

        while True:
            if cita == 'a':
                print('Perfecto')
                print('Su cita quedaria para el Lunes a la 1pm')
                detallesCita = f"Revisión ginecológica | {last_name}, {name} Lunes 1:00 PM"
                break

            elif cita == 'b':
                print('Perfecto')
                print('Su cita quedaria para el Martes a las 8am')
                detallesCita = f"Revisión ginecológica | {last_name}, {name} Martes 8:00 AM"
                break

            elif cita == 'c':
                print('Perfecto')
                print('Su cita quedaria para el Viernes a las 10am')
                detallesCita = f"Revisión ginecológica | {last_name}, {name} Viernes 10:00 AM"
                break

            elif cita == 'd':
                print('Perfecto')
                print('Su cita quedaria para el Sabado a las 5pm')
                detallesCita = f"Revisión ginecológica | {last_name}, {name} Sábado 5:00 PM"
                break
            else:
                print("La opción seleccionada no existe, por favor intente de nuevo")
                continue

    continuar()


def drugs():
    print("WIP")


def checkout():
    print("WIP")


# ------------------MAIN-------------------

login()
menu()
