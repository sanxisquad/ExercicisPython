numeros = []

for i in range(5):
    numero = int(input("Introdueix un numero a sumar: "))
    numeros.append(numero)
suma = sum(numeros)
print(f"La suma total dels numeros es: {suma}")