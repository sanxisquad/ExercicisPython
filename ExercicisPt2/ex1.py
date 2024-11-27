notes_valors = []
valors = []
print("Entrada: ")
cont = int(input("Introdueix el numero de notes: "))
nota_ponderada = 0
total_valors = 0

for i in range(cont):
    nota = float(input(f"Introdueix la nota {i+1} (0-10): "))
    valor = float(input(f"Introdueix el valor de la nota {i+1} (0-1): "))

    notes_valors.append((nota,valor))
    nota_ponderada +=nota*valor
    total_valors+=valor

print("\nNotes i valors entrats: ")
for nota , valor in notes_valors:
    print(f"La nota: {nota} te el seguent valor: {valor}")

if(total_valors!=0):
    mitja_ponderada =nota_ponderada/total_valors
    print(f"\nLa mitjana ponderada es: {mitja_ponderada}")
else:
    print("\nError: Els valors totals són 0, no es pot calcular la mitjana ponderada.")

