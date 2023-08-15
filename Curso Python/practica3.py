#index() = para saber el indice de un caracter (index(A)), conocer que caracter hay en un indice (index[3])

mi_texto = "Esta es una prueba"
resultado = mi_texto[-2]
print(resultado)

mi_texto2 = "Esta es una prueba"
resultado2 = mi_texto2.index("s", 4 , 10)
print(resultado2)

#fragmenta texto, indicando de donde hasta donde queres recortar el texto = mi_texto[2:10]

textaco_chaval = "Aguante Hajime no ippo"
fragmento = textaco_chaval[4:8]
print(fragmento)

#Si no ponemnos un primer termino, python nos da todos los caracteres hasta el segundo numero. 
#ejemplo = 
print(textaco_chaval[:8])

#Podemos poner un tercer parametro que indique un salto entre caracteres
#Ejemplo:

print(textaco_chaval[1:8:2]) #nos da todos los caracteres del 1 al 8, pero saltandose uno.

#Si ponemos solo un tercer parametro, y que sea negativo, entonces nos sera dado el texto en forma inversa.
#Ejemplo :

print(textaco_chaval[::-1]) #nos da la frase entera pero al reves. Podemos darle parametros a los primeros 2 espacios 
#para que delimitemos que parte del texto queremos, y tambien podemos cambiar el -1 por cualquier numero negativo, para
#que ademas de darnos el texto en inversa, nos lo de con saltos de caracteres.

#upper() = convierte un texto a mayusculas
#lower() = convierte un texto a minisuculas
#split() = separa el texto en palabras o caracteres y los almacena en una lista
#join() = junta una lista de strings y los une en un solo texto
#find() = para encontrar un substring en el texto
#replace() = reemplazar un substring en el texto

multilineales = """
puedes
hacer
textos
en 
muchas
lineas
distintas
si
usas
tres
comillas
"""
# puedes multiplicar el contenido de un string como si fueran numeros
#ejemplo:

palabra = 'hola '
multiplicativo = palabra * 5
#ahora la frase sera hola cinco veces seguidas

#usando la funcion len(), se puede saber la longitud de un string
#ejemplo :

print(len(multiplicativo)) 
#da 25, porque es un string de cinco caracteres multiplicado 5 veces.

#puedes saber si una palaba se encuentra dentro de un texto usuando el comando "in"
#ejemplo:
textito = 'Imagenes de subir, imagenes de soñar llenando un lugar vacio. '
print("lugar" in textito)
print("perro" in textito)

#El primer comando da True, porque la palabra lugar se encuentra en la frase
#El segundo comando da False, porque la palabra perro no se encuentra en la frase
#este comando es un boolean, por lo que solo devuelve true o false

#podes usar el comando "not in", que funciona de manera contraria al comando "in". Dando True si no esta, y False si esta


#LISTAS

#van siempre entre corchetes []
#usar el comando len() en una lista, nos dara como resultado la cantidad de elementos dentro de esa lista

lista = [1, 2, 3, 4, 5, 6]
print(len(lista))

#Se puede cambiar el contenido de una lista a diferencia de una string
#ejemplo:

lista[0] = 22 #indico que cambie al elemento que este en la posicion 0 (el 1) por 22
print(lista)

#append() = sirve para agregar elementos a la lista

lista.append(7) #ahora el 7 esta agregado al final de la lista de forma predeterminada
print(lista)

#pop() = sirve para eliminar un elemento de la lista (si no se le da ningun parametro, elemina el ultimo elemento)

lista.pop(5)
print(lista) #eliminamos el elemento que estaba en la quinta posicion, osea el numero 6

#podes guardar el elemento elimnado en una variable, asi no se pierde
#ejemplo:

borrado = lista.pop()
print(borrado)

#sort() = ordena los elementos de una lista de forma alfabetica

listita = ['a', 'h', 'f', 'd', 'x', 'o', 'm']
listita.sort()
print(listita)

#reverse() = funciona como sort, solo que a la inversa
listita.reverse()
print(listita)

#DICCIONARIOS

#se escriben entre llaves {} y separadas con coma. Dentro se allan claves y su definicion, que se separan por un :

#diccionario = {1:'uno', 2:'dos', 3:'tres'}

#print(type(diccionario))

#Las claves no se pueden repetir, pero su valor si

cliente = {'nombre':'Jonathan', 'apellido':'Joestar', 'edad':25}
consultar = cliente['edad']
print(consultar)

#Podemos consultar el contenido de las claves usando corchetes [] y el nombre de la clave

#Se puede almacenar listas y otros diccionarios dentro de un diccionario
#Para tener el contenido exacto de una lista o diccionario, se usan [] para elegir la clave y otros [] despues para
#elegir uno de los indices de la lista
#Ejemplo:

dic = {'c1':[2, 3 ,4 ,5], 'c2':{'s1':'hola', 's2':'mundo'}}
print(dic['c1'][2]) #imprime el 4, que esta en el subindice 2 de la lista
print(dic['c2']['s2']) #imprime lo que se encuentra dentro de s2, que esta dentro de c2

#ejercicio
diccionario ={'c1':['a', 'b', 'c'],'c2':['d', 'e', 'f']}

print((diccionario['c2'][1]).upper())

#usando los corchetes y el diciconario, saque la el elemento de subindice 1 de la segunda lista, y con upper lo pase a mayuscula

#podemos agregar elementos a una lista de forma sencilla usando subindices
#ejemplo:

diccionario['c2'] = ['g', 'h', 'i'] #entre corchetes ponemos el nombre que le damos a la clave, y despues el contenido
#que se le asigna

print(diccionario)

#tambien podemos cambiar el significado de una clave, si ponemos en corchetes el nombre de la clave a cambiar

#dict.keys() = nos dice el nombre de las claves del diccionario
#dict.values() = nos dice los valores dentro del diccionario
#dict.items() = nos dice tanto las claves, como los valores asignados a las mismas

#TUPLES

#son elementos similares a las listas, pero inmutables. No hay forma de cambiar su contenido.

mi_tupla = (1, 2, 3, 4) #no es necesario los parentesis(), pero es un convenio el usarlas

#count() = sirve para saber la cantidad de elementos del mismo tipo hay en una tupla
#ejemplo

mi_tupla = (1, 2, 3, 4, 1, 1, 2, 1)

print(mi_tupla.count(1)) #me arroja un 4, porque es la cantidad de veces que se repite el parametro(1)

#index() = consultar el valor sujeto al subindice dado

#SETS

#no admite elementos repetibles
#se pueden escribir usando el comando set([]) o escribiendolo en {} sin nada mas
#los elementos de un set, no estan guardados por subindices
#no puede albergar listas o diccionarios en su interior

mi_set = set([1, 2, 3, 4, 5])
otro_set = {6, 7, 8, 9, 10}

#se puede usar el comando len para saber el tamaño del set

#union() = sirve para unir sets
setunido = mi_set.union(otro_set)
print(setunido)

#add() = añade un elemento al set
mi_set.add(21)
print(mi_set)

#remove() = elimina un elemento del set
mi_set.remove(3)
print(mi_set)

#discard() = al igual que remove, sirve para quitar un elemento del set.
#la diferencia, es que si quieres eliminar un elemento que no este en el set, no te dara error como con remove

#pop() = elimina un elemento del set de forma aleatoria

#clear() = vacia de elementos al set

#BOOLEANS

#Dan como resultado solo True o False, dependiendo del comando que se le asigne

# X > Y = X mayor a Y
# X < Y = X menor a Y
# X >= Y = X mayor o igual a Y
# X <= Y = X menor o igual a Y
# X == Y = X igual que Y
# X != Y = X diferente de Y 


redes = [ "YouTube", "Facebook", "Twitter", "Whatsapp"]

redes.sort()

print(redes)

#PROYECTO DIA 3

texto = input("Por favor ingrese un texto: ").lower()
letra1 = input("Por favor, ingrese 3 letras al azar: ").lower()
letra2 = input().lower()
letra3 = input().lower()

print(f'La letra {letra1} se repite un total de {texto.count(letra1)} de veces')
print(f'La letra {letra2} se repite un total de {texto.count(letra2)} de veces')
print(f'La letra {letra3} se repite un total de {texto.count(letra3)} de veces')

lista = texto.split()

print(f"En el texto hay una cantidad de {len(lista)} palabras")

print(f'La primera letra del texto es "{texto[0]}", y la ultima letra del texto es "{texto[-1]}"')

lista.reverse()
lista_inversa = ' '.join(lista)
print(f'El texto de forma invertida seria asi "{lista_inversa}"')

if "python" in texto:
    print('La palabra "Python" se encuentra dentro del texto')
else:
    print('No se encuentra la palabra "Python" en el texto')
