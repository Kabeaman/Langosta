hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minEvento = min + dura 
horaEvento = hora

if minEvento / 60 >= 1:
    horaReal = horaEvento + 1
    minReales = minEvento % 60
    print(str(horaReal) + ':' + str(minReales))
elif minEvento / 60 < 1:
    minReales = minEvento
    horaEvento = hora
    print(str(hora) + ':' + str(minReales))
