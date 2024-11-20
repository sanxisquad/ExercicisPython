def contar_paraules(frase):
    paraules = frase.split()
    contador = len(paraules)
    return contador

frase = input('Introdueix una frase: ')

print(f'La frase "{frase}" te {contar_paraules(frase)} paraules.')


