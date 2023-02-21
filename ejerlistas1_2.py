datos = []
num1 = int(input('Introduzca la cantidad de nombres: '))
a = 0
for i in range(0,num1):
    datos.append(input('introduzca un nombre: '))
print(datos, end=' ')
palabra1 = input('\nque nombre desea buscar: ')
for i in range(num1):
    if datos[i] == palabra1:
        a = a + 1
print('El nombre',palabra1,'aparece',a,'veces en la lista')