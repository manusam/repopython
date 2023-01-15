a = int(0) #🦁Gryffindor
b = int(0) #🦅 Ravenclaw
c = int(0) #🦡 Hufflepuff
d = int(0) #🐍 Slytherin
print('P1 ¿Te gusta amanece o atardecer? \n 1) Amanecer \n 2) Anochecer')
e= int(input('que numero eliges? '))
if e == 1:
    a + 1
    b + 1
elif e == 2:
    c + 1
    d + 1
else:
    print('error')
print('P2 Cuando esté muerto, quiero que la gente me recuerde como:\n 1) Lo Bueno \n 2) El Grande \n 3) El Sabio \n 4) El malo')
f = int(input('que numero eliges? '))
if f == 1:
    c + 1
elif f == 2:
    d + +1
elif f == 3:
    a + 1
elif f == 4:
    b + 1
else:
    print('error')
print('P1 ¿Qué tipo de instrumento agrada más a tu oído? \n 1) El violín \n 2) La trompeta \n 3) El piano \n 4) El tambor')
g = int(input('que numero eliges? '))
if g == 1:
    d + 1
elif g == 2:
    c + +1
elif g == 3:
    a + 1
elif g == 4:
    b + 1
else:
    print('error')
print('Enhorabuena eres de: ')
if a >= b and a >= c and a >= d:
  print('🦁 Gryffindor!')
elif b > c and b > d and b > a:
  print('🦅 Ravenclaw!')
elif c > b and c > d and c > a:
  print('🦡 Hufflepuff!')
elif d > c and d > b and d > a:
  print('🐍 Slytherin!')
else:
  print('error')