letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

nif  = input("Introduce una nif")
if len(nif) !=9:
    print("La longitud no es valida")

#elif nif[-1] not in letras and nif [-1] not in letras.lower():

elif nif[-1].isdigit():
    print("El ultimo caracter no es valido")


else:
    if nif[:-1]isdigit():
        print("El numero es valido")

 else:
        print("Seguimos haciendo pruebas...")