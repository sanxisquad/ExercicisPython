def calculadora (num1,num2,operacio):
    if operacio == '+':
        resultat = num1 + num2
    elif operacio == '-':
        resultat = num1 - num2
    elif operacio == 'x':
        resultat = num1 * num2
    elif operacio == '/':
        resultat = num1 / num2
    else:
        resultat = 'Operació no trobada'
    return resultat
num1 = int(input('Fica el numero 1: '))
num2 = int(input('Fica el numero 2: '))
operacio = input('Indica la operació que vols realitzar: ')

print(f'El resultat de l operacio es {calculadora(num1,num2,operacio)}.')