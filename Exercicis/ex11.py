numero = int(input('Introdueix un numero per a saber si es primer o no: '))
1
contador = 0
for i in range(1,numero):

    d = numero % i

    if d == 0:
        contador += 1
if contador <3 :
    print('El numero es primer')
else:
    print('El numero no es primer')      
