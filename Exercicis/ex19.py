def calNum(notes):
    sus = 0
    apro = 0
    notable = 0
    exc = 0
    Ns = []
    Na = []
    Nn = []
    Ne = []
    for nota in notes:
        if nota<5:
            sus+=1
            Ns.append(nota)
        elif 5<=nota<7:
            apro+=1
            Na.append(nota)
        elif 7<=nota<9:
            apro+=1
            notable+=1
            Na.append(nota)
            Nn.append(nota)
        else:
            apro+=1
            exc+=1
            Na.append(nota)
            Ne.append(nota)
    print()
    print("Resultats:")
    print("-"*20)
    print(f"Suspesos: ({sus}): {Ns}")
    print(f"Aprobats: ({apro}): {Na}")
    print(f"Notables: ({notable}): {Nn}")
    print(f"Excelents: ({exc}): {Ne}")
        

def introduirNotes(notes):
    cont = int(input("Introdueix el numero de notes que vols insertar: "))
    
    for i in range(cont):
        nota = -1
        while nota < 0 or nota > 10:  
            nota = float(input(f"Introdueix la nota {i + 1} (0-10): "))
            if nota < 0 or nota > 10:
                print("Error: La nota ha d'estar entre 0 i 10.")

        notes.append(nota)
def organitzarNotes(notes):
    notes_ordenades = sorted(notes)
    print()
    print("Notes organitzades (de menor a major):")
    print(notes_ordenades)
    

opcio = 0
notes = []
while(opcio!=4):
    print("Menu: ")
    print("1. Introduir notes")
    print("2. Estadistiques generals")
    print("3. Mostrar les notes organitzades en categories")
    print("4. Sortir del programa")
    opcio = int(input("Introdueix l'opcio que vols fer: "))
    match opcio:
        case 1:
            introduirNotes(notes)
        case 2:
            calNum(notes)
        case 3:
            organitzarNotes(notes)
        case 4:
            exit
