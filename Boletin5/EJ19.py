#Pedir y comprobar una fecha con el formato requerido

fecha = input("Introduce una fecha con el siguiente formato: DD/MM/YYYY: ")

if len(fecha) !=10:
    print("Formato invalido. La longitud no es correcta")
elif fecha[2]!="/" or fecha[5]!="/":
    print("Formato invalido. Falta alguna / o no estan en su sitio")
else:
    dia = fecha[:2]
    mes = fecha[3:5]
    anno = fecha[6:]
    if dia.isdigit() and mes.isdigit() and anno.isdigit():
        dia = int(dia)
        mes = int(mes)
        anno = int(anno)
        if dia == 0 or dia > 31 or mes == 0 or mes > 12:
            print("El dia o mes no son validos")
        else:
            if dia == 31 and (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes== 11):
                print("Ese mes no puede tener 31 dias")
            elif mes == 2 and dia==30:
                print("Febrero no puede tener 30 dias")
            elif mes == 2 and dia==29:
                if anno%4 and (anno%100 != 0 or anno%400 == 0):
                    print("Fecha Valida, Año Bisiesto")
                else:
                    print("NO puede tener 29 dias si no es año bisiesto")
            else:
                print("Fecha Correcta")
    else:
        print("Formato invalido. Hay algun caracter incorrecto")