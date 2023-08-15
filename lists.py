colors = ['red', 'blue', 'green']

numbers = list((1, 2 , 3 , 4))

print(numbers)
print(type(numbers))

Juan = list(range(1, 10))

print(Juan)

print(len(Juan))
print(colors[2])

#Con el In le pregunto a la consola si el valor entre comillas esta en la lista
print('green' in colors)
print('violet' in colors)

#el numero en corchetes es la posicion de la lista que cambiamos por 'yellow'
print(colors)
colors[1] = 'yellow'
print(colors)
#Ahora se elimino la palbra 'blue' de la lista, y se puso la palabra 'yellow'

#para ver los comandos disponibles para la lista
#print(dir(colors))

#Agregamos el purple a la lista
colors.append('purple')
print(colors)

#Al agregar varios elementos o una lista a otra, se usa extend y no append
colorinhos = list(('black', 'orange', 'sex'))
colors.extend(colorinhos)
print(colors)

#usando el insert, se puede agregar un elemento en la posicion deseada
colors.insert(1, 'gold')
print(colors)
#Usando el len(), se puede poner un elemento al final de la lista
colors.insert(len(colors), 'pink')
print(colors)

#usando el pop, se elimina el elemento segun la posicion seleccionada
colors.pop(3)
print(colors)

#tambien sirve usar el elemento segun su nombre usando el remove
colors.remove('sex')
print(colors)

#eliminar toda la lista
#colors.clear()

#ordenados alfabeticamente
colors.sort()
print(colors)
#ordenado a la inversa del alfabeto
colors.sort(reverse=True)
print(colors)

