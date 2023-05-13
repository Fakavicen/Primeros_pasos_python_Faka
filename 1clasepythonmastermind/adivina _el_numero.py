import random

#Variables

num_secrt = random.randint(1, 5)
num_user =  int(input("Introduce un numero desde 1 hasta el 5\n"))
#codigo
if num_user != num_secrt:
    print("Has adivinado el numero secrito")
    
print("No has adivinado el nuemero pero el numero secreto es {}".format(num_secrt))    