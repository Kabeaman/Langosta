myStr = "Praise the sun"

print(dir(myStr))

#upper = Transforma todo a mayusculas
print(myStr.upper())
#swapcase= transforma las mayusculas en minusculas y viceversa
print(myStr.swapcase())
#split= Transforma el string en una lista 
print(myStr.split())
#capitalize= transforma la primera letra del texto en mayuscula
print(myStr.capitalize())
#replace = reemplaza la palabra del texto marcado por otra
print(myStr.replace('sun', 'moon'))

#prueba de usar varios comandos a la vez
print((myStr.replace('sun', 'moon').upper().split()))

#count = cuenta la cantidad de X asignadas en la variable
print(myStr.count('s'))

#find= la posicion exacta la primera variable que se busca 
print(myStr.find('h'))

#len= longitud de la variable
print(len(myStr))

#index= indice del caracter X
print(myStr.index('i'))

print(myStr.isnumeric()) #para saber si es numerico
print(myStr.isalpha())  #para saber si es alfa-numerico

#buscar que caracter esta en la posicion asignada
print(myStr[7])

print("We " + myStr)
print("We {0}".format(myStr))
#la "f" indica que lo que esta entre llaves debe ser interpretado como una variable existente
print(f"We {myStr}")
