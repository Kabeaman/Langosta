#x = int(input())

#if x < 30:
#    print("X es menor que 30")
#elif x == 30:
#    print("damn, adivinaste el valor de X")
#else:
#    print("X es mayor que 30")


# un "=" es para asignar
# dos "==" es para igualar
print ("Inserte el nombre de usuario.")
user = str(input())

print("Inserte la contraseña.")
password = str(input())

if user == "kabeaman":
    if password == "manaos12":
        print("El acceso ha sido autorizado")
    else:
        print("El acceso ha sido denegado")
else:
    print("Nombre de usario incorrecto")