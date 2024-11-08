entrada = 0
num_secret = 4

while entrada != num_secret:
    entrada = int(input('Has de endivinar un numero del 1 al 10: '))
    if entrada < num_secret:
        print("El numero que has ficat es més petit que el numero secret")
    elif entrada > num_secret :
        print("El numero que has ficat és més gran que el número secret")

print('Felicitats crack, has endivinat el numero')