#Entrada y salida de archivos

#E/S = entrada y salida, I/O = input y output

#open() = permite abrir un archivo de texto
#write() = permite escribir en un archivo de texto
#read() = permite leer el contenido de un archivo de texto
#close()= cierra el archivo de texto

#mi_texto = open('prueba.txt')

#una_linea = mi_texto.readline()
#print(una_linea.rstrip())

#una_linea = mi_texto.readline()
#print(una_linea.rstrip())

#una_linea = mi_texto.readline()
#print(una_linea.rstrip())

#el metodo rstrip() lo usamos en este caso para evitar el salto de linea a la hora de imprimir en pantalla el texto


#for l in mi_texto:
#    print("Aqui dice: " + l.rstrip())


#todas = mi_texto.readlines()
#todas = todas.pop() #al usar readlines, queda almacenado en una lista, por lo que se pueden usar metodos de listas
#print(todas)


#mi_texto.close()

#modos de apertura
#'r' = Solo lectura
#'w' = Solo escritura (borra el contenido original del texto)
#'a' = Solo escritura al final del texto

#ej:
#textaco = open('prueba.txt', 'w')
#textaco.write('''Esta es la primera linea
#Esta es la segunda linea
#Esta es la tercera linea
#Esta es la cuarta linea
#''')

#writelines() = Se puede pasar una lista de strings al texto

#textaco.writelines(['Hola ', 'Mundo'])



#textaco.close()

texto = open('prueba.txt', 'a')

texto.write('\nBienvenido')

texto.close()