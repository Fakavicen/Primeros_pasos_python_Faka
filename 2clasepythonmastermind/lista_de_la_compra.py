import os

#Variables

shopping_list = []
user_menu = None
added_product = None
option_not_selected = ("Seleccion no en el menu. Selecione \n")

title = "Bienvenido a la lista de la compra"

#Code 

    
os.system("cls")
print(title) 
input("Enter para continuar...\n") 
 
os.system("cls")
while user_menu != "Q":
    user_menu = input("¿Cual opcion quieres?\n"
         "A - Añadir un Producto\n"
         "Z - Elimiar el ultimo producto\n"
         "V - Ver la lista\n"
         "Q - Salir de la lista\n")
    
    os.system("cls")
    input("Enter para continuar...\n")
    os.system("cls")

    if user_menu == "A" or user_menu == "a":

        os.system("cls")

        added_product = input("¿Que deseas compra?\n")
        shopping_list.append(added_product)
        os.system("cls")
    
    elif user_menu == "Z":
       
       os.system("cls")
       input("Enter para continuar...\n")
       os.system("cls")

       user_menu = input("¿Seguro que quieres eliminar el ultimo producto? S/N\n")
      
       if user_menu == "S":

        os.system("cls")

        shopping_list.pop()
        print("Se a eliminado corectamente\n")

        os.system("cls")  
    
    elif user_menu == "V":

        os.system("cls")
        print(shopping_list)
        input("Enter para Volver al menu...\n")
        os.system("cls")

    else:
       print(option_not_selected)
else:
    os.system("cls")
    print("Gracias por usar la lista de la compra")