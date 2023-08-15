from random import randint

adivinacion = int(input('Decime en que numero del 1 al 6 va a caer el dado: '))

dado = randint(1,6)

print(dado)

if adivinacion == dado:
    print('¡Felicidades! Ganaste')
else: print('Que pelotudo que sos, mogolico matate')
