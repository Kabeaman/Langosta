#OPERADORES DE COMPARACION 

# X > Y = X mayor a Y
# X < Y = X menor a Y
# X >= Y = X mayor o igual a Y
# X <= Y = X menor o igual a Y
# X == Y = X igual que Y
# X != Y = X diferente de Y 

#Se puede almacenar las comparaciones en una variable, lo que dara como resultado True o False
#Ejemplo:

variable = 20!=5
print(variable) #devuelve "True", porque 20 es distinito de 5

#OPERADORES LÓGICOS

#and = cuando se necesitan cumplir 2 operadores logicos a la vez
#or = se cumple o uno, u otro
#not = cuando no se necesita que se cumpla 

#CONTROL DE FLUJO
#if = determina la acciona que se tiene que cumplir
#elif = significa que si la primera accion no se cumple, que se revise esta opcion 
#else = si ninguna de las acciones anteriores se cumplen, se ejecuta este codigo como ultima opcion

#LOOPS (bucles)

#for = para generar bucles con una cantidad definida de vueltas
#ejemplo=

lista = ['a', 'b', 'c', 'd']
for elemento in lista:
    print(f'numero {elemento}')

#Podemos saber el indice de cada elemento dentro de la lista, y unirlo mediante el loop al contenido de la lista
for elemento in lista:
    indice = lista.index(elemento) + 1 #se le suma uno, porque los indices empiezan en 0
    print(f"La letra {elemento} corresponde al subindice {indice}")


#iterar en una lista
objetos = [[1, 2],[3, 4], [5,6]]

for a,b in objetos: #en lugar de asignar los valores a una sola variable, se la asigno a dos, asi Python
    print(a)        #puede separar los elementos de la lista en distintas variables, e imprimirlas por separado
    print(b)

#while = para generar bucles que se repiten de forma indefinida, hasta que se cumpla alguna situacion

vidas = 5

while vidas > 0:
    print(f"Aun tienes {vidas} vidas")
    vidas = vidas -1 #puedo reemplazar el vidas = vidas-1, poniendo vidas-=1, que es lo mismo pero resumido
else:
    print("Ya no tienes mas vidas")

#pass(pasar) = mantiene el lugar del lopp while, haciendo que pueda ejecutarse codigo posterior sin dar error

#break = permite interrumpir el codigo
#ejemplo = 

nombre = input("Diga su nombre: ")

for letra in nombre:
    if letra == 'a':
        break
    print(letra)

#continue = al contrario que break, este no elimina el loop, si no que solo saltea las partes que no se cumplen

for letra in nombre:
    if letra == 'a':
        continue
    print(letra)

#RANGE

#sirve para hacer repetir un bucle una cantidad de veces determinada sin necesidad de requerir del largo de una lista
#ej:

for n in range(1, 5): #el primer termino indica desde donde parte, y el segundo en donde termina
    print(n)          #se pude poner un tercer termino para indicar los "saltos" que da en el rango

#ENUMERADOR

#enumerate = Nos facilita el acceso a los indices en una lista
#ejemplo=

listarda = ['a', 'b', 'c']
indice = 0

"""for item in lista:
    print(indice, item)
    indice += 1"""
#Todo esto es la forma de indicar un indice a un elemento de la lista, pero se puede simplificar usando enumerate

for item in enumerate(lista):
    print(item)   #Esto genera tuplas donde estan almacenados el valor del indice, y del objeto de la lista.and

for x,y in enumerate(lista):
    print(x, y)  #haciendolo de esta forma, el codigo nos imprime los dos valores por separados y no en una tupla

#ZIP

#zip = sirve para entrelazar los elementos de dos listas en tuples

nombre = ['Thomas', 'Langoni', 'Messi']
edad = [22, 20, 36]
ciudades = ['Don Torcuato', 'Boca Predio', 'Miami']

lista_tuples = list(zip(nombre, edad, ciudades)) #hay que ponerlo dentro de una lista para que pueda ser mostrado en pantalla
print(lista_tuples)

for nombre, edad, ciudades in lista_tuples:
    print(f'{nombre} tiene {edad} años y vive en {ciudades}')


uno = ['uno','um','one']
dos = ['dos','dois','two']
tres = ['tres','três','three']
cuatro = ['cuatro','quatro','four']
cinco = ['cinco','cinco','five']

numeros = list(zip(uno,dos, tres, cuatro, cinco))
print(numeros)

#MIN y MAX

#sirven para localizar los valores mas altos y bajos (respectivamente) en una coleccion de datos

lista_numeros = [1, 2, 64 ,333 ,535 ,11 ,-12, 22]
menor = min(lista_numeros)
mayor = max(lista_numeros)

print(f'El valor menor de la lista es {menor}, y el mayor es {mayor}')

#RANDOM

#biblioteca de python para traer metodos que generan aleatoriedad
#randint() = Da un numero aleatorio entre los valores dados
#uniform() = Nos da un valor decimal dentro del rango de los valores dados
#random() = No se le tiene que dar valores. Da un numero decimal entre 0 y 1
#choice() = elije un valor dentro de una lista. No tiene por que ser solo integers
#shuffle() = Mezcla los valores dentro de una lista


from random import randint
numero_random = randint(1, 14)

print(numero_random)

#Comprension de listas

#Facilita procesos que ya se vieron antes

palabra = 'python'
listaa = [letra for letra in palabra]

print(listaa)

#Tambien es valida esta forma

listous = [letra for letra in "Python"]

print(listous)

lista_numerica = [numeros for numeros in range(3,33,3)]
print(lista_numerica)

pies = [10, 20, 30, 40, 50]
metros = [n/3.281 for n in pies]

print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n%2==0]
print(valores_pares)


from random import randint
numero = randint(1, 101)
nombre_usuario  = input('Por favor, introduzca su nombre: ')
intentos = 0

print(f'Muy bien {nombre_usuario}, he elegido un numero del uno al cien, y tienes 8 intentos para adivinarlo')

while intentos <= 8:
    adivinar = int(input('Por favor, introduzca un numero: '))
    if adivinar<1 or adivinar>100:
        print('El numero elegido no está permitido.')
    if adivinar>=1 and adivinar<=100:    
        if adivinar < numero:
            print('Tu numero es menor')
        elif adivinar > numero:
            print('Tu numero es mayor')
        elif adivinar == numero:
            print(f'Felicidades, adivinaste mi numero en tan solo {intentos} intentos.')
            break
        intentos += 1
else:
    print(f'Lo siento, no haz logrado adivinar mi numero en ocho intentos. El numero era {numero}.')    

    
