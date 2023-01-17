import random

a= input('escriba su pregunta: ')
b= random.randint(1,9)
if b==1:
    print('Sí definitivamente.')
elif b == 2:
    print('Es decididamente así.')
elif b == 3:
    print('Sin duda.')
elif b == 4:
    print('Respuesta confusa, intenta otra vez.')
elif b == 5:
    print('Pregunta de nuevo más tarde.')
elif b == 6:
    print('Mejor no decirte ahora.')
elif b == 7:
    print('Mis fuentes dicen que no.')
elif b == 8:
    print('Las perspectivas no son tan buenas.')
elif b == 9:
    print('Muy dudoso')