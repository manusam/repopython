datos = []
num1 = 1
while num1 >= 0:
    num1= int(input('introduzca un valor positivo: '))
    datos.append(num1)
datos.remove(num1)
print(datos, end=' ')