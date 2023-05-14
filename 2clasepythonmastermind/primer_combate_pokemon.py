import random

#Variable

life_pikachu = 80
life_squirtle = 90

#Constant

EARLY_LIFE_PIKACHUk = life_pikachu
EARLT_LIFE_SQIORTLE = life_squirtle

while life_pikachu > 0 and life_squirtle > 0:

    #Turno de pikachu
    print("Turno de pikachu")
    pikachu_attack = random.randint(1, 2)
    if pikachu_attack == 1:
      #Bola voltio
      print("Pikachu ataca con Bola Voltio")
      life_squirtle -= 10
    else:
      #Onda Trueno
      print("Pikachu ataca Onda Trueno")
      life_squirtle -= 11


    print("La vida de pikachu es: {}, la vida de Squirtle es: {}".format(life_pikachu, life_squirtle))
    input("Enter para continuar...")



    #Turno de Squirtle
    print("Turno Squirtle")

    squirtle_attack = None
    while squirtle_attack != "P" and squirtle_attack != "A" and squirtle_attack != "B":
        squirtle_attack = input("¿Que ataque deseas ralizar? Placaje, Pistola Agua, Burbuja\n")
    
    if squirtle_attack == "P":
        print("Squirtle ataca con Placaje")
        life_pikachu -= 10
    elif squirtle_attack == "A":
        print("Squirtle ataca con Pistola de Agua")
        life_pikachu -= 12
    elif squirtle_attack == "B":
       print("Squirtle ataca con Burbuja")
       life_pikachu -= 9


    print("La vida de pikachu es: {}, la vida de Squirtle es: {}".format(life_pikachu, life_squirtle))
    input("Enter para continuar...")



if life_pikachu > life_squirtle:
 print("pikachu gana!")

else:
 print("Squirtle gana!")