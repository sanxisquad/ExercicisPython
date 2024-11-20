print('Hauras d introduir 3 numero per a saber quin es el mes gran')

num1 = int(input('Introdueix el numero 1: '))
num2 = int(input('Introdueix el numero 2: '))
num3 = int(input('Introdueix el numero 3: '))
gran = 0


gran = num1

if num2 > gran:
    gran = num2
if num3 > gran:
    gran = num3
print(f'El numero mes gran dels 3 és: {gran}')
