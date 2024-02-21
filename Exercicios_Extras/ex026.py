# Faça um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra "A", em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").lower().strip()
letras = []

print('-' * 30)
print(f"A letra 'A' aparece {frase.count('a')} vezes")

for pos, letra in enumerate(frase):
    if letra == 'a':
        print(f"A primeira letra 'A' apareceu na posição {pos + 1}")
        break

for letra in frase:

    letras.append(letra)

letras_reverse = list(reversed(letras))

for pos, l in enumerate(letras_reverse):

    if l == 'a':
        print(f"A última letra  'A' apareceu na posição {len(letras) - pos}")
        break
