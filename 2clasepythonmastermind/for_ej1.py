



#variables
text_user = input("Introduce el texto\n")
counted_commas = 0
counted_spaces = 0
counted_points = 0 

for container in text_user:
    if " " == container:
        counted_spaces += 1
    elif "." == container:
        counted_points += 1
    elif "," == container:
        counted_commas += 1
    
print("Estos son los container que estan en el texto\n Comas: {} \n Espacios: {} \n Puntos: {}\n".format(counted_commas, counted_spaces, counted_points))