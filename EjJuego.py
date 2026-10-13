import random
dado  = random.randint(1,7)
if dado in range (1,3):
    print("Has Fallado")
elif dado in range (3,5):
    print ("Herida leve")
elif dado == 5:
    print ("Herida Grave")
else:
    print ("Crítico")