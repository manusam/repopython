import random
datos = []
for i in range(0,10):
    datos.append(random.randint(1,10))
for i in range(0,10):
    print('-valor','[',i + 1,']')
    print(' -valor normal:',datos[i],'\n -valor al cuadrado:',datos[i]**2,'\n -valor al cubo:',datos[i]**3)    