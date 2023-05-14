#title

title = "Bienvenido al test del gamer"
print("\n" + title + "\n" + "_" * len(title) + "\n")

#variables

points = 0

#Question

#Question1
opcion = input("1 - ¿Cual de lso suiguientes género de videojuegos te gusta más?\n"
               "A - Acción\n"
               "B - Aventuras\n"
               "C - Estrategia\n")

if opcion == "A":
    points += 1
elif opcion == "B":
    points += 2
elif opcion == "C":
    points += 3
else:
    print("Las ociones posible son A, B y C")
    exit()

#Question2
opcion = input("2 - ¿Cuál de estos juegos es conocido por su modo multijugador en línea?\n"
               "A - Call of Duty\n"
               "B - The Witcher 3: Wild Hunt \n"
               "C - Skyrim\n")

if opcion == "A":
    points += 2
elif opcion == "B":
    points += 3
elif opcion == "C":
    print += 1
else:
    print("Las ociones posible son A, B y C")
    exit()

#Question3
opcion = input("3 - ¿Cuál es la consola más vendida de todos los tiempos?\n"
               "A - PlayStation 2\n"
               "B - Xbox One\n"
               "C - Nintendo Switch\n")

if opcion == "A":
    points += 3
elif opcion == "B":
    points += 1
elif opcion == "C":
    print += 2
else:
    print("Las ociones posible son A, B y C")
    exit()

#Question4
opcion = input("4 - ¿Cuál de estos personajes es el fontanero más famoso de los videojuegos?\n"
               "A - Sonic\n"
               "B - Donkey Kong\n"
               "C - Mario\n")

if opcion == "A":
    points += 1
elif opcion == "B":
    points += 1
elif opcion == "C":
    points += 3
else:
    print("Las ociones posible son A, B y C")
    exit()

#Question5
opcion = input("5 - ¿Qué popular juego de Battle Royale fue desarrollado por Epic Games?\n"
               "A - Apex Legends\n"
               "B - PUBG\n"
               "C - Fortnite\n")

if opcion == "A":
    points += 1
elif opcion == "B":
    points += 1
elif opcion == "C":
    points += 3
else:
    print("Las ociones posible son A, B y C")
    exit()

print("Has finalizado el test del gamer. Puntos conseguidos: {}/15".format(points))