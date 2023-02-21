respuesta1 = input('Desea jugar: ')
if respuesta1 == 'si':
    for tabla in range(1,11,1):
        print('\n--tabla de multiplicar del', tabla,'--')
        print('==============================')
        for multi in range(1,11,1):
            print('      ',tabla,'*',multi, '=' ,tabla*multi)
        print('==============================')
elif respuesta1 == 'no':
    print('\n--Hasta luego--\n')
else:
    print('\n--respuesta no valida--\n')