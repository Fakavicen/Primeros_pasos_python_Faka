import random, os 

#Variable

life_pikachu = 80
life_squirtle = 90

#Constant

EARLY_LIFE_PIKACHUk = life_pikachu
EARLT_LIFE_SQUIORTLE = life_squirtle

while life_pikachu > 0 and life_squirtle > 0:

    #Turno de pikachu
    print("Turno de pikachu\n")
    pikachu_attack = random.randint(1, 2)
    if pikachu_attack == 1:
      #Bola voltio
      print("Pikachu ataca con Bola Voltio\n")
      life_squirtle -= 10
    else:
      #Onda Trueno
      print("Pikachu ataca Onda Trueno\n")
      life_squirtle -= 11

      #negative life
    if life_pikachu < 0:
       life_pikachu = 0

    if life_squirtle < 0:
        life_squirtle = 0 

    #Bar life 

    pikachu_bar_life = int(life_pikachu * 10 / EARLY_LIFE_PIKACHUk)
    print("Pikachu:  [{}{}] ({}/{})\n".format("*" * pikachu_bar_life, " " * (10 - pikachu_bar_life) , life_pikachu, EARLY_LIFE_PIKACHUk))

    squirtle_bar_life = int(life_squirtle * 10 / EARLT_LIFE_SQUIORTLE)
    print("Squirtle: [{}{}] ({}/{})\n".format("*" * squirtle_bar_life, " " * (10 - squirtle_bar_life), life_squirtle, EARLT_LIFE_SQUIORTLE))

    input("Enter para continuar...\n")
    os.system("cls")

    #Turno de Squirtle
    print("Turno Squirtle\n")

    squirtle_attack = None
    while squirtle_attack != "P" and squirtle_attack != "A" and squirtle_attack != "B":
        squirtle_attack = input("¿Que ataque deseas ralizar? Placaje, Pistola Agua, Burbuja, nada\n")
    
    if squirtle_attack == "P":
        print("Squirtle ataca con Placaje\n")
        life_pikachu -= 10
    elif squirtle_attack == "A":
        print("Squirtle ataca con Pistola de Agua\n")
        life_pikachu -= 12
    elif squirtle_attack == "B":
       print("Squirtle ataca con Burbuja\n")
       life_pikachu -= 9
    elif squirtle_attack == "N":
       print("No ataco")

      #negative life
    if life_pikachu < 0:
       life_pikachu = 0

    if life_squirtle < 0:
        life_squirtle = 0 

    #Bar life 

    pikachu_bar_life = int(life_pikachu * 10 / EARLY_LIFE_PIKACHUk)
    print("Pikachu:  [{}{}] ({}/{})\n".format("*" * pikachu_bar_life, " " * (10 - pikachu_bar_life) , life_pikachu, EARLY_LIFE_PIKACHUk))

    squirtle_bar_life = int(life_squirtle * 10 / EARLT_LIFE_SQUIORTLE)
    print("Squirtle: [{}{}] ({}/{})\n".format("*" * squirtle_bar_life, " " * (10 - squirtle_bar_life), life_squirtle, EARLT_LIFE_SQUIORTLE))

    input("Enter para continuar...\n")
    os.system("cls")

if life_pikachu > life_squirtle:
 
 print("pikachu gana!")

else:
 print("Squirtle gana!")