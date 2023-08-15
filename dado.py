from random import randint
#print(randint(1, 6))

def lanzar_dado():
    return randint(1, 6)

dado = lanzar_dado()
print(f"El dado ha caido en {dado}")