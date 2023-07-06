import string

text_user = input("Introduzca un texto\n")
upper_case_counter = 0
capital_letters = string.ascii_uppercase



for container in text_user:
    if container in capital_letters:
        upper_case_counter =+ 1

print("En el texto hay {} mayusculas".format(upper_case_counter))