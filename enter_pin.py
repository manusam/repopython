print('Banco falso')

pin = int(input('Ingrese su Pin: '))
while pin != 1234:
    pin = int(input('Codigo incorrecto pruebe otra vez: '))
    if pin == 1234:
        print('Pin correcto')