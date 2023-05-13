edad = int(input(' Ingrese su edad: '))
tipo_de_credencial = input('Ingrese su tipo de credencial (E  de Estudainte/ P de Pensionado/'
                           ' F Familia Numerosa/ N Nada): ')

if (25 <= edad <= 35 and tipo_de_credencial == 'E') or\
        edad<=10 or\
        (edad >= 64 and tipo_de_credencial == 'P') or\
        (tipo_de_credencial == 'F'):
    print(' obtienes un descuento del 50% ')
else:
    print(' no obtiene el descuento ')