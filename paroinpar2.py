from random import randint

intentos = 0

print('Buenas, ¿podria decirme su nombre?')

Nombre = input()

def lanzar_dado():
    return randint(1, 6)

dado1 = lanzar_dado()
dado2 = lanzar_dado()
dado3 = lanzar_dado()

sumadados = dado1 + dado2 + dado3

def par():
    if sumadados % 2 == 0:
        par = True
    if sumadados %2 != 0:
        par = False

def impar():
    if sumadados %2 != 0:
        impar = True
    if sumadados %2 == 0:
        impar = False
    
