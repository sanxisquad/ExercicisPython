def afegirProducte():
    print("\n\nPer afegir el producte primer haureu d'introduir el nom i despres el preu.")
    nom = input("\nIntrodueix el nom del producte que voleu afegir: ")
    preu = int(input("Introdueix el preu del producte: "))
    productes[nom]=preu


def mostrarProductes():
    print("\n\nA continuacio es mostraran tots els productes introduits. ")
    print(productes)

def calcularTotal():
    total = len(productes)
    print(f"\n\nEn total hi ha {total} productes")


def buscarProductes():
    nom = input("Introdueix el nom del producte que vols trobar: ")

    if nom in productes:
        print(f"El preu del producte '{nom}' és: {productes[nom]}€")
    else:
        print(f"El producte '{nom}' no es troba en la llista.")

productes = {}
opcio = 0
while opcio!=5:
    print("Menu d'opcions: ")
    print("1. Afegir producte")
    print("2. Mostrar productes")
    print("3. Calcular total")
    print("4. Buscar producte")
    print("5. Sortir del programa")
    opcio = int(input("Introdueix l'accio que vols efectuar: "))
    
    match opcio:
        case 1:
            afegirProducte()
        case 2:
            mostrarProductes()
        case 3:
            calcularTotal()
        case 4:
            buscarProductes()
        case 5:
            break
