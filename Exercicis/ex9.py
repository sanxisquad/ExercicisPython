
paraules = input("Introdueix les paraules que vulguis i si vols sortir escriu sortir: ")

while paraules.lower() != 'sortir':
    print(f"La paraula introduida es {paraules} ")
    paraules = input("Introdueix les paraules que vulguis i si vols sortir escriu sortir: ")
    
print('Tancant programa...')