texto ="Hola mundo" +"cruel"
texto = "Hola Mundo"
texto = "Al recreo"

print(texto)
print()



texto = "Hola mundo"
print (texto)
print(texto[::-1]) #truco para obtener la cadena al reves

print(len(texto)) #Para ver la longitud de la cadena. ( Si tiene 16 caracteres, el ultimo es el 15) Se comienza desde 0
                  #print (texto[16]) # da error por esto mismo

for indice in range(len(texto)): # Para indicar en que posicion y en que caracter hay en cada espacio
    print("En la posicion", indice, "aparece el caracter",texto[indice])

print ()

for indice in range(len(texto)-1,-1,-1): # Para indicar en que posicion y en que caracter hay en cada espacio de final a principio
    print("En la posicion", indice, "aparece el caracter",texto[indice])


for letra in texto: #Forma mas facil de mostras caracter a caracter una cadena en lineas distintas
    print(letra)
