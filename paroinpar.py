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

# par = ((2, 4, 6, 8 ,10 , 12, 14, 16, 18))
# impar = ((3, 5, 7 ,9 ,11, 13, 15, 17))


print('Muy bien, ' + Nombre + ', los dados han sido lanzados ')

# while intentos < 1:
#     print('¿par o impar?')
#     resultado = input()
#     resultado = ((par, impar))

#     intentos = intentos + 1

#     if sumadados == par and resultado == par:
#         resultado == sumadados
#     if sumadados == impar and resultado == impar:
#         resultado == sumadados
#     if sumadados == impar and resultado == par:
#         resultado != sumadados
#     if sumadados == par and resultado == impar:
#         resultado != sumadados
   
# if resultado == sumadados:
#     print('¡Buen trabajo, ' + Nombre + '! ¡Has adivinado!')

# if resultado != sumadados:
#     print('Mala suerte, intentalo denuevo')

if sumadados % 2 == 0:
    par = True
else: par = False
    


while intentos < 1:
    resultado = int(input('Elija 0 para par y 1 para impar' ))
    if par and resultado == 0:
        print("Bien ahí, pa")
    elif par == False and resultado == 2:
        print("Bien ahí, pa")
    else:
        print("Mala suerte, incorrecto")
    
    intentos +=1