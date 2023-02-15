datos = []
for i in range(0,5):
    datos.append(int(input('Cual es su nota: ')))
print(datos, end =' ')
print('\n','nota media',((sum(datos))/(len(datos))),'\nnota maxima',max(datos),'\nnota minima',min(datos))