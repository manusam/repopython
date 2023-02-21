datos=[]
for i in range(0,10):
    datos.append(int(input('introduzca el valor:')))
for par in range(0,10):
    if datos[par] %2 == 0: 
        print(datos[par])