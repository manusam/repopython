GRYFFINDOR = int(0) #🦁Gryffindor
RACENCLAW = int(0) #🦅 Ravenclaw
HUFFLEPUFF = int(0) #🦡 Hufflepuff
SLYTHERIN = int(0) #🐍 Slytherin
error = int(0)
print('P1 ¿Te gusta amanece o atardecer? \n 1) Amanecer \n 2) Anochecer')
e= int(input('que numero eliges? '))
if e == 1:
    GRYFFINDOR += 1
    RACENCLAW += 1
elif e == 2:
    HUFFLEPUFF += 1
    SLYTHERIN += 1
else:
    error = error + 1

print('P2 Cuando esté muerto, quiero que la gente me recuerde como:\n 1) Lo Bueno \n 2) El Grande \n 3) El Sabio \n 4) El malo')
f = int(input('que numero eliges? '))
if f == 1:
    HUFFLEPUFF += 1
elif f == 2:
    SLYTHERIN += 1
elif f == 3:
    GRYFFINDOR += 1
elif f == 4:
    RACENCLAW += 1
else:
    error = error + 1
print('P1 ¿Qué tipo de instrumento agrada más a tu oído? \n 1) El violín \n 2) La trompeta \n 3) El piano \n 4) El tambor')
g = int(input('que numero eliges? '))
if g == 1:
    SLYTHERIN += 1
elif g == 2:
    HUFFLEPUFF += 1
elif g == 3:
    GRYFFINDOR += 1
elif g == 4:
    RACENCLAW += 1
else:
    error = error + 1
print('Enhorabuena eres de: ')
if GRYFFINDOR >= RACENCLAW and GRYFFINDOR >= HUFFLEPUFF and GRYFFINDOR >= SLYTHERIN:
   print('🦁 Gryffindor!')
elif RACENCLAW >= HUFFLEPUFF and RACENCLAW >= SLYTHERIN:
    print('🦅 Ravenclaw!')
elif HUFFLEPUFF >= RACENCLAW:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')
