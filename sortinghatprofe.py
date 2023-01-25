gryffindor = int(0) #🦁Gryffindor
ravenclaw = int(0) #🦅 Ravenclaw
hufflepuff = int(0) #🦡 Hufflepuff
slytherin = int(0) #🐍 Slytherin
error = int(0)
print('P1 ¿Te gusta amanece o atardecer? \n 1) Amanecer \n 2) Anochecer')
e= int(input('que numero eliges? '))
if e == 1:
    gryffindor += 1
    ravenclaw += 1
elif e == 2:
    hufflepuff += 1
    slytherin += 1
else:
    error = error + 1

print('P2 Cuando esté muerto, quiero que la gente me recuerde como:\n 1) Lo Bueno \n 2) El Grande \n 3) El Sabio \n 4) El malo')
f = int(input('que numero eliges? '))
if f == 1:
    hufflepuff += 1
elif f == 2:
    slytherin += 1
elif f == 3:
    gryffindor += 1
elif f == 4:
    ravenclaw += 1
else:
    error = error + 1
print('P1 ¿Qué tipo de instrumento agrada más a tu oído? \n 1) El violín \n 2) La trompeta \n 3) El piano \n 4) El tambor')
g = int(input('que numero eliges? '))
if g == 1:
    slytherin += 1
elif g == 2:
    hufflepuff += 1
elif g == 3:
    gryffindor += 1
elif g == 4:
    ravenclaw += 1
else:
    error = error + 1
print('Enhorabuena eres de: ')
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
   print('🦁 Gryffindor!')
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print('🦅 Ravenclaw!')
elif hufflepuff > ravenclaw and hufflepuff > gryffindor and hufflepuff > slytherin:
    print('🦡 Hufflepuff!')
elif slytherin > ravenclaw and slytherin > hufflepuff and slytherin > gryffindor:
    print('🐍 Slytherin!')
else:
    print('---Varias casas---\n')
    print('  Lista de puntos\n','------------------')
    print(' [ Gryffindor =', gryffindor,']' ,'\n','------------------') 
    print(' [ Ravenclaw  =', ravenclaw,']' ,'\n','------------------')
    print(' [ Hufflepuff =', hufflepuff,']' ,'\n','------------------')
    print(' [ Slytherin  =', slytherin,']' ,'\n','------------------')