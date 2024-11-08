resultat = 0
num1 = int(input("Fica el numero 1: "))

num2 = int(input("Fica el numero 2: "))

opcio = input("Quina operacio vols fer: ")

if opcio == '+' :
    resultat = num1 + num2
elif opcio == '-':
    resultat = num1 - num2 


print(resultat)
married = False

if num1 == num2:
    print("son iguals")
elif num1 > num2:
    print(f"el numero {num1} es mes gran que el {num2}")
else:
    print(f"el numero {num2} es mes gran que el {num1}")

if married:
    print("Esta casat")

