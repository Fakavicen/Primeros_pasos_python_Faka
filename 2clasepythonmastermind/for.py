
vocales = ["a", "e", "i", "o", "u"]
frase = input("Escribe tu frase\n")
vocales_encontrada = 0

for letra in frase:
    letra in vocales
    if letra in vocales:
        print("He encontrado una {} ".format(letra))
        vocales_encontrada += 1

print("Vocales encontradas: {}".format(vocales_encontrada))