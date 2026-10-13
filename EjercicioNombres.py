cadena = "Morales Vazquez, Jose María"
#Tengo que hacer que ponga "José María Morales Vazquez"

n = cadena.find(", ")
apellidos = cadena[:n]
nombre = cadena [n+2:]

resultado = nombre + " " + apellidos
print(resultado)


#Ahora sustituir todas las vocales por *** (cada vocal por 3*)


for vocal in "aeiouáéíóúAEIOUÁÉÍÓÚ" :
    cadena = cadena.replace(vocal,"***")
    print(cadena)