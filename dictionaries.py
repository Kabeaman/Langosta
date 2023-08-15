#Es un tipo de dato que nos ayuda a definir datos a partir de claves y valores

product = {
    "name": "Book",
    "price" : 3,
    "quantity" : 25
}

person = {
    "first_name": "Thomas",
    "second_name": "Martin",
    "last_name": "Alfaro"
}


print(type(person))

#imprime solo las palabras claves de el dictionarie "person"
print(person.keys())

#person.clear limpia los elementos internos de "person"

#Una lista con dos dictionaries
bosses = [
    {"Burgo": 'Tauro demon', "Izalith": 'Lecho del caos'},
    {"Muro de lothric": 'Vordt', "Castillo": 'Principes gemelos'}
]

print(bosses)
