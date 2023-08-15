import random

def dado():
    return random.randint(1,6)

lanzar_dado = dado()
lanzar_dado2 = dado()
lanzar_dado3= dado()
print("Los dados han caido en " + str(lanzar_dado)+ ", " + str(lanzar_dado2) + " y " + str(lanzar_dado3))