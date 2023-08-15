from numpy import negative

n1 = float(input("a: ") )
n2 = float(input("b: ") )
n3 = float(input("c: ") )

invariable1 = 4 
invariable2 = 2
invariable3 = -1

part1 = n2 * invariable3
part2 = n2 * n2
part22 = invariable1 * n1 * n3
part222 = part2 - part22
part3 = n1 * invariable2

if part222 == negative:
    numeroloco = part222 * invariable3
    raiz = pow(float(numeroloco),0.5)
    raizparcial1 = part1 + float(raiz) 
    raizparcial2 = part1 - float(raiz)
    raiz1 = raizparcial1 / part3
    raiz2 = raizparcial2 / part3

    print("Las raices de esta ecuacion son: " + str(round(raiz1, 3 )) + "i y " + str(round(raiz2,3)) +"i")

if part222 != negative:
    raiz = pow(float(part222),0.5)

    raizparcial1 = part1 + raiz
    raizparcial2 = part1 - raiz

    raiz1 = raizparcial1 / part3
    raiz2 = raizparcial2 / part3

    print("Las raices de esta ecuacion son: " + str(round((raiz1, 3))) + " y " + str(round(raiz2, 3)))
