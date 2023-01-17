a = int(1)
b = int(0)
while b != 6:
    a = a + 1
    b = int(input('Cual es el numero: '))
    print(a)
    if a == 4:
        print('numero de intentos sobrepasado')
        b = 6
if a == 4:
    print('')
else:
    print('numero correcto')