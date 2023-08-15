import random

intentosRealizados = 0

print('Hola, ¿cómo te llamas?')

Nombre = input()

numero = random.randint(1, 20)

print('Bueno, ' + Nombre + ', estoy pensando entre un numero del 1 al 20')

while intentosRealizados < 5:
    print('intenta adivinar')
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion > numero:

         print('Tu estimacion es muy alta')

    if estimacion < numero:
        
        print('Tu estimacion es muy baja')

    if estimacion == numero:
        break
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + Nombre + '! ¡Has adivinado mi número en ' +
intentosRealizados + ' intentos!')

if estimacion != numero:
    print('Sos horrible, dedicate a otra cosa')
 