#METODOS DE LOS OBJETOS

#Si pones un objeto seguido de un punto, python te muestra la cantidad de metodos disponibles para dicho objeto
#ejemplo:

dic = {'clave1': 'nashe', 'clave2':'agusneta'}

tupla = dic.popitem() #popitem() es un metodo de los objetos diccionarios

#https://docs.python.org/es/3.9/library/index.html aca se puede consultar la documentacion oficial

texto = f",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:_#')

print(texto)

#lstrip(x) = sirve para eliminar de un texto las palabras que se le asignen a lstrip. Si no hay nada asignado, se le

#insert(x,y) = sirve para insertar un elemento a un conjunto de elementos, usando x como posicion e y como el elemento a ingresar
#ejemplo =

frutas = ['banana', 'frutilla', 'limon']
frutas.insert(3, 'manzana')
print(frutas)

#FUNCIONES

#sirven para crear bloques de codigos que puedas ser facilmente ejecutadas a lo vario del codigo sin problema

def mi_funcion(nombre):
    '''esta funcion escribe hola y el nombre que se le de cuando se llama a la funcion'''
    print("Hola " + nombre)

mi_funcion('Thomas')

#return

#suele usarse en las funciones para que el resultado devuelto, pueda ser almacenado en una variable
#ejemplo

def multiplicar(numero1,numero2):
    return numero1 * numero2

numero = multiplicar(2,4)
print(numero)

'''
def invertir_palabra(palabra):
    return palabra[::-1].upper()
    
palabra = 'Python'

print(invertir_palabra('Python'))
'''

#FUNCIONES DINAMICAS

#Funciones con loops

def chequear_3_cifras(lista):
    
    lista_rango = []

    for n in lista:
        if n in range(100,1000):
            lista_rango.append(n)
        elif():
            pass
    else:
        return print(lista_rango)        


chequear_3_cifras([1, 222, 4, 85757557, 229, 33])

#Desempacar tuples 

precios_cafe = [('Capuccino', 1.50), ('Expresso', 2.00),('Latte', 3.50)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)
cafe, precio = cafe_mas_caro(precios_cafe)

print(f'El {cafe} es el cafe mas caro, y su precio es de {precio}')

#Interaccion entre funciones
from random import shuffle

palitos= ['-', '--', '---', '----']

def mezclar(lista):
    shuffle(lista)
    return lista

def probar_suerte():
    intento=''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado.')

    print(f'Te ha tocado {lista[intento-1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)






from random import randint

def lanzar_dados():
    return randint(1,6), randint(1,6)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    
    if int(suma_dados) <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif int(suma_dados)>6 and suma_dados<10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"



lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista.sort() #ordena la lista de menor a mayor
    lista.pop(-1) #elimina al ultimo elemento de la lista
    lista = list(set(lista)) #transforma a la lista en un set,y luego denuevo en lista. Los sets no admiten elementos repetidos, asi que de esta manera, se puede eliminar elementos repetidos de forma automatica
    return lista #nos devuelte la lista ya tuneada (?)

def promedio(lista):
    promedios = 0
    numeros = 0
    for n in lista: #en promedios, se van sumando 
        promedios +=n
        numeros += 1
        
    return promedios/numeros

import random

lista_numeros = [1, 2, 3, 4, 5, 6, 7]
lista_vacia = []
def lanzar_moneda():
    return random.choice(['Cara', 'Cruz']) #con choice, se elige de forma aleatoria uno de los dos parametros dados (cara, cruz)

def probar_suerte(resultado, lista_numeros):
    if resultado == 'Cara': #si el resultado da es cara, nos da una lista vacia
        print ('La lista se autodestruira')
        return lista_vacia #la funcion devuelve la variable lista vacia, que no tiene nada. (podemos ahorrarnos la variable si solo ponemos [] en su lugar)
    elif resultado == 'Cruz':
        print('La lista fue salvada')
        return lista_numeros #salio cruz, asi que la lista que se dio, simplemente fue la de la variable interna.and

#ARGUMENTOS INDEFINIDOS

#(*args)

#si se usa la palabra *args como argumento en una funcion, no importa la cantidad de elementos que incluya el usuario,
#la funcion seguira itinerando la cantidad de veces puestas, si necesidad de preestablecer un limite

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(2,3,4,4,5,5,4,2)) #ya no esta limitado a poder sumar solo 2 elementos, si no que suma todos los que les metamos

#(**kwargs) keywords args

#no solo podemos usar infinitos datos como con *args, si no que tambien podemos darle claves a los valores, por lo que 
#es perfecto para trabajar con diccionarios

def sumatoria(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(sumatoria(x = 1, y = 2, z= 3))#estos argumentos dados no son diccionarios, pero la funcion los transforma en unos
                                    #haciendo asi que puedas meterles argumentos compuestos para y trabajar con funciones
                                    #propias de python que sirvan para los diccionarios



def prueba(num1, num2, *args, **kwargs): #por convenio, ese seria el orden en que se ponen los argumentos

    print(f'El primer numero es {num1}')
    print(f'El segundo numero es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y': 'dos', 'z':'tres' }
prueba(20, 40, *args, **kwargs)


#ejercicio 1
def devolver_distintos(a, b, c):
    suma_total = a+b+c
    lista_numerica = [a,b,c]
    for arg in args:
        if suma_total > 15:
            return max(lista_numerica)
        elif suma_total < 10:
            return min(lista_numerica)
        else:
            lista_numerica.sort()
            return lista_numerica[1]

print(devolver_distintos(2, 11 ,1))

#ejercicio 2

def palabra_random(palabra):
    palabra = palabra.lower()
    palabra = list(set(palabra))
    palabra.sort()
    
    return palabra

print(palabra_random('supercalifragilisticoespiralidoso'))
     
#ejercicio 3

def contador_ceros(*args):
    for arg in args:
        contar = args.count(0)
        if contar == 2:
            return True
        else:
            return False

print(contador_ceros(6,0,5,1,0,3,0,1))

#Ejercicio 4

def contar_primos(numero_primo):
    
    primos = [2]
    iteracion = 3
    
    if numero_primo < 0:
        return 0
    
    while iteracion <= numero_primo:
        for n in range(3, iteracion):
            if iteracion % n == 0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))

#PROYECTO DIA 5

from random import choice

lista_palabras=['messi', 'ronaldo', 'garnacho', 'neymar', 'suarez', 'medina', 'riquelme', 'palermo']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    validez = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not validez:
        letra_elegida = input('Elige una letra: ')
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            validez = True
        else:
            print('No has elegido una letra valida.')

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias +=1
    elif letra_elegida not in palabra_oculta and letra_elegida not in letras_incorrectas:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    else:
        pass
    
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculta era {palabra}')
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('¡Felicitaciones! has encontrado la palabra')
    return True

palabra, letras_unicas = elegir_palabra(lista_palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + ' '.join(letras_incorrectas))
    print(f'Vidas = {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
