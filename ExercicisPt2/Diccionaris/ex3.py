productes = {"Pera": 2, "Poma": 4, "Pressic": 5}

print(productes.keys())

nom = input("Introdueix el nom de la fruita a la que li vols modificar el preu: ")
preu = int(input("Introdeuix el nou preu: "))

productes.update({nom:preu})

print(productes)