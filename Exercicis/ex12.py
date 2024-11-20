suma = 0
numero = 0
while numero >=0:
    numero = int(input("Introdueix numeros per a sumar-los i introdueix un de negatiu per a mostrar el resultat acumulat: "))
 
    if numero >= 0:
        suma += numero
print(f'El numero total de numeros positius sumats es: {suma}')
