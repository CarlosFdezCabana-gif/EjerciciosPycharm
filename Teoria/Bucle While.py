for i in range (0,5):
    print (i)

print ("###")

i = 0
while i < 5:
    print (i)
    i += 1


import random
dado = 0
while dado != 6:
    dado = random.randint(1,6)
print (dado)



dado1 = 0
contador  = 0
while dado1 != 6:
    dado1 = random.randint(1,6)
    print (dado1)
    contador += 1
print ("Has tenido que tirar el dado", contador, "veces para que salga un 6")