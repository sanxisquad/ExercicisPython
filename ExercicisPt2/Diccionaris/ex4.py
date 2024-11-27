llista = ["Groc", "Groc", "Blau","Vermell", "Vermell","Groc"]

aparicions = {}
for paraula in llista:

    if paraula in aparicions:
        aparicions[paraula]+=1
    else:
        aparicions[paraula]=1
print(aparicions)