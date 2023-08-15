#Una variable es donde se guarda (y se recupera) 
#datos que se utilizan en un programa

name = "Ash"
surname = " Ketchum"
print (name + surname)

#Tambien se pueden agrupar en una misma linea de codigo,
#y no precisamente una abajo de la otra
nombre, apellido = "Ash", "Ketchum"

print (nombre, apellido)

#Sensitive case 
#mismo dato, pero la diferencia de la minuscula lo convierten en variables distintas
sun = "Solaire"
Sun = "Solaire"

print (sun)

#Conventiones
dark_souls = "Artorias" #Snake case
darkSouls = "Manus"     #Camel case
DarkSouls = "Gwyn"      #Pascal case

#Constante (todo en mayuscula)
PI = 3.1416
MY_NAME = "Kabeaman"


#Las variables pueden ser reasignadas, empezo como "artorias" y acabo como "Sif"
dark_souls = "Artorias" 
dark_souls = "Sif"

