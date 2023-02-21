print('PAR E IMPAR')
par = int(input('Escriba un numero par: '))
if par % 2 == 1:
    print('Ese numero no es par \nSi quiere intentarlo una vez mas vuelva a ejecutar el programa')
else:
    impar = int(input('Escriba un numero impar: '))
    if impar % 2 == 0:
        print('Ese numero no es impar \nSi quiere intentarlo una vez mas vuelva a ejecutar el programa')
    else:
        print('Gracias por tu aportacion')