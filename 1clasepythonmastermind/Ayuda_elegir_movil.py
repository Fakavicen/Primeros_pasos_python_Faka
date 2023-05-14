
#Variables

option = "NAME"
perfectly_mobile = "ninguno"

#Code

option = input("¿ios o Android?\n"
               "A - Android\n"
               "I - ios\n")
if option == "A": 
   option = input("¿Tienes dinero?S/N")

   if option == "S":
        option = input("¿Te importa la cámara del movil? S/N")

        if option == "S":
         perfectly_mobile = "Google Pixel Supercamara"

        elif option == "N":
         perfectly_mobile = "Xiaomi economico"

   else:
    perfectly_mobile = "anfroid Chino $100"

elif option == "I":
    option = input("¿Tienes dinero?\n"
                   "S/N")

    if option == "S":
     perfectly_mobile = "iPhone 14 pro max"

    else:
       perfectly_mobile = "IPhone SE Gen 2"

print("Tu movil ideal es {}".format(perfectly_mobile))