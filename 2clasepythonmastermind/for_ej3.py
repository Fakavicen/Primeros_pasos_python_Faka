import os
table_number = int(input("Introduce el numero de la tabla que quieres\n"))
multiplication_number = int(input("Introduce hasta cual tabla quieres que se multiplique\n"))
input("Enter para continuar...\n")
os.system("cls")
for container in range(1, multiplication_number + 1):
    print("{} x {} = {}".format(table_number, container, (table_number*container)))