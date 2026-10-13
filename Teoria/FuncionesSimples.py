texto = "Hello World"
print(texto)
print(texto.upper()) #todo mayuscula
print(texto.lower()) #Todo minuscula
print(texto.swapcase()) # Mayusculas a minusculas y viceversa

#todo esto lo hace sin modificar la cadena original. Si quiero modificarla:
#texto = texto.upper()

texto = "Hello World"
print(texto.find("o")) #en que posicion está el caracter
print(texto.find("Wo")) # o conjunto de caracteres

print(texto.count("e")) #Para contar las veces que sale un caracter en la cadena

print(texto.count("e",10)) #puedes indicar donde quieres que empiece a buscar
print(texto.count("e",5,7)) # o entre que numeros buscar

print(texto.replace("e","*")) #sustituye un caracter por otro
print(texto.replace(" ","")) # para quitar espacios en blanco

texto = "                   Hello World   "
print(texto)                                         #Para borrar espacios de los lados (los 3 comandos sirven para verlo claro)
print(texto.strip())

print(texto.lstrip()) #Me quita solo los de un lado
print(texto.rstrip()) #Los del otro lado


codigo ="3456"
print(codigo.zfill(6)) #Rellena con 0 hasta llegar la longitud de la cadena a lo que se pide

