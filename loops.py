foods = ['chocolate', 'mayonese', 'ketchup', 'tangerine', 'Banana']

for food in foods:
    if food == "ketchup":
        print("aguante el ketchup viejaaa")
        break
    print(food)

for food in foods:
    if food == "mayonese":
        print("Una poronga la mayonesa")
        continue
    print(food)

#break = Deja de ejecutar el comando
#continue = sigue ejecutando el comando

for numbers in range(1, 8):
    print(numbers)

count = 4

while count <= 10:
    print(count)
    count = count + 1
    