diccionari = {"Numero": 1, "Color": "Vermell", "Ciutat":"Cervera"}

print(diccionari.keys())

k = input("Elegeix la claus a eliminar: ")
diccionari.pop(k)
print(diccionari)