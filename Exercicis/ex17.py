import random

def llençar_dau():
    return random.randint(1,6)

cops = int(input('Quants cops vols llençar el dau: '))

for i in range(1,cops+1):

    print(f"El resultat del llençament {i} ha sigut: {llençar_dau()}")