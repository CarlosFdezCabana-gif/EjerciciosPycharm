#numero del 1 al 10 y hay que adivinar segun si te has quedado corto o lejos. Decir cuantos intentos has tenido que usar

import random
numeroAle= random.randint (1, 10)
contador = 0
opcion = 0
while opcion != numeroAle:
    opcion = int(input("Intenta adivinar el numero del 1 al 10: "))
    if opcion  < numeroAle:
        print ("El numero es menor que el numero adivinar")
        contador +=1
        print("Llevas", contador, "intentos")
    elif opcion >numeroAle:
        print ("El numero es mayor que el numero adivinar")
        contador +=1
        print("Llevas", contador, "intentos")
    else:
        print ("Has Acertado")
        contador +=1

        if contador == 1:
            print ("Has acertado a la primera")
        else:
            print ("Has necesitado",contador, "Intentos")
