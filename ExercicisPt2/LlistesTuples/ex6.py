numeros = [1,4,5,7,3,2,5]

numero = int(input("Introdueix el numero que desitja trobar: "))

if numero in numeros:
    index = numeros.index(numero)
    print(f"El index del numero {numero} es {index}")
else:
    print(f"El numero {numero} no esta a al llista.")
