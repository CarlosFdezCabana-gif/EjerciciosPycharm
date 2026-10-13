import random

Simbolos = "1X2"

equipos =["Equipo1", "Equipo2", "Equipo3", "Equipo4,", "Equipo5", "Equipo6", "Equipo7", "Equipo8", "Equipo9", "Equipo10"
          , "Equipo11", "Equipo12", "Equipo13", "Equipo14"]

#random.shuffle(equipos) #Mezclar equipos
for i in range (len(equipos)):
    aleatorio = random.randint (0, len(equipos)- 1)
    equipos[i], equipos [aleatorio] = equipos[aleatorio], equipos[i]

print (" --- Quiniela de la Jornada --- ")

for i in range(0,len(equipos), 2):
    local  = equipos[i]
    visitante = equipos[i+1]

    resultadoSimbolo= random.randint(0,2)
    resultado = Simbolos [resultadoSimbolo]

    print ("Los resultados son:")
    print (f"{local}, vs, {visitante} -> resultado: {resultado}")

