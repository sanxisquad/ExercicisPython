num1 = int(input("Introdueix el primer numero a sumar: "))
num2= int(input("Introdueix el segon numero a sumar: "))

resultat = num1 + num2


if (resultat%2) == 0:
    print(f'El resutlat es: {resultat} i es parell.')
else:
    print(f'El resultat es: {resultat} i es imparell')