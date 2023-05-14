import random

#Varibles

tienda = 0
numeropuerta = random.randint(1,5)

#code

print("Bienvenido al juego \n"
      "-------------------\n")
print("Estas en una isla solitaria")
movimiento1 = input("¿Que quieres hacer?\n"
                   "A - ir a exlorar la isla\n"
                   "B - Buscar un zona para hacer un copamento\n")
if movimiento1 == "A":
     movimiento2 = int(input("Encontraste una puerta con clave\n"
                    "pero dice que deves adivinar un numero de 1 a 5\n"))
     if movimiento2 == numeropuerta:
         print("Ganaste")
         exit()
     else:
       print("Te muriste")
       print("la clave era {} ".format(numeropuerta))
if movimiento1 == "B":
     tienda = input("Te has encontrado una tienda de campaÃ±a\n"
                    "Â¿que quieres hacer?\n"
                    "A - tomar la tienda de campaÃ±a y vivir en ella\n"
                    "B - no tomar la tienda de campaÃ±a\n")
     if tienda == "B":
            print("Te muriste por no saber donde dormir")
            exit()
     else:
      print("Has ganado")
exit()