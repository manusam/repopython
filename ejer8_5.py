datos=[]
a = 1
b = 0
for i in range(0,3):
    datos.append(int(input('introduzca el valor: ')))
num1 = int(input('Introduzca un valor de la lista: '))
while num1 != 999:
    for i in range(0,3):
        if datos[i] == num1:
         a = a + 1
    if a > 1:
        print('Ese valor esta dentro de la lista')
    else:
        print('Ese valor no esta en la lista')
    a = 1
    num1 = int(input('Introduzca otro valor: '))
print('Gracias por usar el programa')