maxim = int(input("Introdueix el numero maxim: "))

for i in range(maxim+1):
    
    parell = i % 2

    if parell == 0:
        print(f"El numero {i} es parell")
    