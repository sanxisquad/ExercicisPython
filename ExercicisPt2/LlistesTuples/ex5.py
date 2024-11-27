numeros = [1,2,3,4,5,6,7,8,9]
numeros_rev=[]

for i in range(len(numeros)-1,-1,-1):
    numeros_rev.append(numeros[i])

print(f"Llista normal: {numeros}")
print(f"Llista reverse: {numeros_rev}")
