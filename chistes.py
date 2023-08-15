from random import randint

print("Buenas, ¿Quieres que te cuente un chiste?")
Respuesta = input()

if Respuesta == "si":
    num_chiste = randint (1, 3)

if Respuesta != "si":
    print("Bueno, igual te lo cuento")
    num_chiste = randint (1, 3)


if num_chiste == 1:
    print("¿Por qué los diabeticos no pueden vengarse ?") 
    print("")
    print("Porque la venganza es dulce")
if num_chiste == 2:
    print("-Querida preparate porque hoy lo vamos a hacer por la oreja")
    print("")
    print("-¿Por la oreja? Me vas a dejar sorda...")
    print("")
    print("-¿Cómo que te voy a dejar sorda?") 
    print("¿Alguna vez te deje muda? vieja conchuda y la puta que te parió!")
    print("Te venís a hacer la santa ahora y te tragaste más pijas que tu vieja y tus 2 hermanas juntas")
if num_chiste == 3:
    print("El marido en un momento reflexivo le encara a su señora y le dice:")
    print("")
    print("-Vieja, estuve pensando que si vos te murieras")
    print("no sabes como te lloraría")
    print("")
    print("-¿Ah, si?¿Y no me podes mostrar como me llorarías?")
    print("")
    print("-Primero morite vieja y la re puta madre que te parió") 
    print("y la concha de la recalcada hija de puta de tu hermana!")