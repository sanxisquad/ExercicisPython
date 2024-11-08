maxim = int(input('Introdueix el numero maxim el qual vols anar sumant: '))

suma = 0

for i in range(maxim+1):
    suma += i

print(f'El resultat es: {suma}')