import random 
Imagenes_ahorcado = ['''

 +---+
 |   |
     |
     |
     |
     |
========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''

 +---+ 
 |   |
 O   |
/|\  |
     |
     |
========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''','''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''']

listaDePalabras = "slamdunk oyasumipunpun pokemon digimon akira watamote evangelion psychopass berserk codegeass fullmetalalchemist mobpsycho hajimenoippo naruto onepiece cowboybeebop tokyorevenger onichichi komisan gintama jojos monster konosuba haikyuu drstone gantz durarara clannad Nana chainsawman kuroshitsuji beck dorohedoro overlord tokyoghoul doraemon shinchan bakuman parasyte dragonball orange nichijou kaguyasama beastars hellsing claymore magi toradora mushishi tengentoppa redline trigun hyouka paprika lovelive baccano" .split()

def obtenerPalabraAlAzar(listaDePalabras):
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(Imagenes_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(Imagenes_ahorcado[len(letrasCorrectas)])
    print()

    print("Letras incorrectas: ", end='')
    for letra in letrasCorrectas:
         print(letra, end=' ')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range (len(palabraSecreta)):
          if palabraSecreta[i] in letrasIncorrectas:
               espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios:
          print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):
     while True:
          print('Adivina una letra')
          intento = input()
          intento = intento.lower()
          if len(intento) != 1:
               print("Por favor, introduce una letra")
          elif intento in letrasProbadas:
               print("Ya has probado esa letra. Elige otra")
          elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
               print("Por favor ingresa una LETRA")
          else:
               return intento

def JugarDeNuevo():
     print("¿Quieres jugar de nuevo? (si o no)")
     return input().lower().startswith("s")


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(listaDePalabras)
juegoTerminado = False

while True:
     mostrarTablero(Imagenes_ahorcado, letrasCorrectas, letrasIncorrectas, palabraSecreta)

     intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
     
     if intento in palabraSecreta:
          letrasCorrectas = letrasCorrectas + intento
          
          encontradoTodasLasLetras = True
          for i in range (len(palabraSecreta)):
               if palabraSecreta[i] not in letrasCorrectas:
                    encontradoTodasLasLetras = False
                    break
          if encontradoTodasLasLetras:
               print('¡Si! ¡La palabra secreta es ' + palabraSecreta + '! ¡Has Ganado!')
               juegoTerminado = True
     else:
          letrasIncorrectas = letrasIncorrectas + intento 

          if len(letrasIncorrectas) == len(Imagenes_ahorcado) - 1:
               mostrarTablero(Imagenes_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
               print('Te has quedado sin intentos \ndespues de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la plabra era"' + palabraSecreta + '"')
               juegoTerminado = True
     
     if juegoTerminado:
          if JugarDeNuevo():
               letrasCorrectas = ''
               letrasIncorrectas = ''
               juegoTerminado = False
               palabraSecreta = obtenerPalabraAlAzar(listaDePalabras)
          else:
               break