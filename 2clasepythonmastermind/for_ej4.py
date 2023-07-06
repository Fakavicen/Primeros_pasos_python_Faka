import os

user_menu = None
list_number = []

while user_menu != "Q":

    os.system("cls")
    input("Enter para continuar...\n")
    os.system("cls")

    user_menu = input("¿Cual opcion quieres?\n"
         "A - Añadir un numero\n"
         "V - Ver la lista de numeros\n"
         "Q - Ver el menor y el mayor numero de la lista\n")
    
    os.system("cls")
    input("Enter para continuar...\n")
    os.system("cls")

    if "A" == user_menu:
        added_product = int(input("¿Que numero deseas añadir a la lista?\n"))
        list_number.append(added_product)
        os.system("cls")

    elif user_menu == "V":

        os.system("cls")
        print(list_number)
        input("Enter para Volver al menu...\n")
        os.system("cls")

small_number = min(list_number)
big_number = max(list_number)

print("El numero mas grande es {} y el mas pequeño es {}".format(small_number, big_number))