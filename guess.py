a = int(1)
b = int(0)
while b != 6 or a != 4:
    a = a + 1
    b = int(input('Cual es el numero: '))
if a == 4 and b != 6:
    print ('numero de intentos sobrepasado')
else:
    print ('numero acertado')