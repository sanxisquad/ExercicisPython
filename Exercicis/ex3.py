paraula = input("Introdueix una paraula: ")
contador = 0
vocals = 'aeiou'
for lletra in paraula.lower():
    if lletra in vocals:
        contador+=1
print(f"La paraula {paraula} te {contador} vocals")