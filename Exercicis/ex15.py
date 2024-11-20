def es_primer(numero):
    contador = 0
    if numero < 2:

        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

for n in range(15):
    print(f'El numero {n} es numero prim? {es_primer(n)}')