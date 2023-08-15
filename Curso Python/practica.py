#print('A' '\tB' '\tC' '\nD' '\t E' '\t F' '\nG''\tH' '\tI')

#print('Tu edad es de ' + input('Dime tu edad: ') + ' años')

#proyecto 1
#print('El nombre de tu nueva cerveza es ' + '\"'+input("Nombre de un color en ingles: ") + ' '+ input('Nombre de una ciudad: ') + '\"')

#edad = input('dime tu edad: ')
#print('tu edad es ' + edad)
#print(type(edad))
#nueva_edad = int(edad) + 1
#print (nueva_edad)

#proyecto 2

#Nombre = input('Ingrese su nombre: ')
#Monto = float(input('Cantidad de dinero generada: '))

#print (f'El monto por comision del señor {Nombre} es de ${round((Monto*13)/100)}')

#nombre = input('Introduce tu nombre: ')

#if 't' or 'T' in nombre:
#    print('Bien ahi, papa')
#else: print('Pedazo de boludooo')

#dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}

#dic['c3'] = 'g'

#print(dic)

#texto = input('Escriba su texto aqui: ')
#lista_letras = input('Escribe la primera letra: ')
#lista_letras2 = input('Escribe la segunda letra: ')
#lista_letras3 = input('Escribe la tercera letra: ')

#texto = texto.lower()
#lista_letras = lista_letras.lower()


#print ('La letra ' + str(lista_letras) + ' se repite un total de '+ str(texto.count(lista_letras)) + ' veces.')
#print ('La letra ' + str(lista_letras2) + ' se repite un total de '+ str(texto.count(lista_letras2)) + ' veces.')
#print ('La letra ' + str(lista_letras3) + ' se repite un total de '+ str(texto.count(lista_letras3)) + ' veces.')

#palabras = texto.split()

#print('El texto tiene' + ' ' + str(len(palabras)) + ' ' + 'de palabras')

#print('La primera letra del texto es '+texto[0] +' y la última es '+ texto[-1])

#palabras.reverse()
#texto_invertido = ' '.join(palabras)
#print('El texto invertido se veria asi ' +'\"' + str(texto_invertido) + '\"')

#if 'python' in texto:
#    print('La palabra Python se encuentra en su texto')
#else: print('La palabra Python no se encuentra en el texto')

#from random import *

#numero_aleatorio = randint(1, 101)
#nombre_usuario = input('Por favor diga su nombre: ')
#intentos = 0
#print(f'Bueno, {nombre_usuario}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número')

#while intentos <= 8:
#    numero_usuario = int(input('Introduzca un numero: '))
#    if int(numero_usuario) > 100 or int(numero_usuario) < 1:
#       print('El numero elegido no está permitido.')
#    elif int(numero_usuario) < 100 or int(numero_usuario) > 1:  
#        if int(numero_usuario) > int(numero_aleatorio):
#            print('Su respuesta es incorrecta, su numero es mayor al numero secreto')
#        elif int(numero_usuario) < int(numero_aleatorio):
#            print('Su respuesta es incorrecta, su numero es menor al numero secreto')
#        elif int(numero_usuario) == int(numero_aleatorio):
#            print(f'¡FELICIDADEs!, Has ganado en solo {intentos} intentos')
#            break
#    intentos = intentos + 1   
#else:
#    print('No lograste encontrar el numero en los 8 intentos disponible, pedazo de pete.')

from random import randint

def lanzar_dados():
    return randint(1,6)

dado1 = lanzar_dados()
dado2 = lanzar_dados()


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1+dado2
    if suma_dados <= 6:
        print(f'La suma de tus dados es {suma_dados}. Lamentable')
    elif suma_dados > 6 and suma_dados < 10:
        print(f'La suma de tus dados es {suma_dados}. Tienes buenas chances')
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")



