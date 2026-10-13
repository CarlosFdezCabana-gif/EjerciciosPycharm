import random

for _ in range(14):
    resultado = random.randint(1,7)
    if resultado == 5 or resultado == 6:
        print ("  X  ")
    elif resultado == 7:
        print ("2")
    else:
        print ("   1")