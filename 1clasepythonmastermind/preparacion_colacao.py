
print("Me voy a la cocina")
print("Abro la nevera")

hay_leche = input("¿Hay leche? (S/N)")
hay_colacao = input("¿Hay Colacao? (S/N)")

if hay_leche != "S" or hay_colacao != "S":
    print("Voy hasta el super")
    if hay_leche != "S":
        print("Compro leche")
    if hay_colacao != "S":
        print("Compro colacao")
print("Ponemos la leche en el vaso SPonemos el colaco en el vaso Mezclamos y listo")