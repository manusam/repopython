datos=[]
for i in range(0,15):
    datos.append(int(input('introduzca el valor:')))
for par in range(0,15):
    if datos[par] %2 == 0: 
        print(datos[par], end=' ')   
print()