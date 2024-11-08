entrada = input("Introdueix una frase: ")
contador = 0
frase = entrada


for lletres in entrada:
    
    if lletres != ' ':
        contador += 1

print(f"La frase {frase} tenia {contador} lletres")

