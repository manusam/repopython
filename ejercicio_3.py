print('PAR E IMPAR')
par = int(input('Escriba un numero par: '))
impar = int(input('Escriba un numero impar: '))
if par % 2 == 1 or impar % 2 == 0:
    if par % 2 == 1:
        print('Ese numero no es par')
    if impar % 2 == 0:
        print('Ese numero no es impar')
    print('Si quiere intentarlo una vez mas vuelva a ejecutar el programa')
else:
    print('Gracias por tu aportacion')