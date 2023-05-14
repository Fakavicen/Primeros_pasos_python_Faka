from random import randint

#Variable

life_pikachu = 80
life_squirtle = 90

while life_pikachu > 0 and life_squirtle > 0:

    #Turno de pikachu
    print("Tuno de pikachu")
    pikachu_attack = random.radiant(1, 2)
    if pikachu_attack == 1:
      #Bola voltio
      print("Pikachu ataca con Bola Voltio")
      life_squirtle -= 10
    else:
      #Onda Trueno
      print("Pikachu ataca Onda Trueno")
      life_squirtle -= 11



 



































if life_pikachu > life_squirtle:
 print("pikachu gana!")

else:
 print("Squirtle gana!")