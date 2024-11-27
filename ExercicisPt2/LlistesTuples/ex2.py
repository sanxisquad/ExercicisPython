import random

numeros = []
parells = []
imparells = []
div = []

for i in range(10):
    rand= random.randint(1,100)
    numeros.append(rand)
for i in range(len(numeros)):
    
    if numeros[i] % 2 ==0:
        parells.append(numeros[i])
    else:
        imparells.append(numeros[i])
    if numeros[i] % 5 == 0:
        div.append(numeros[i])

print(f"Parells: {parells}")
print(f"Imparells: {imparells}")
print(f"Divisibles de 5: {div}")