# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input("Digite um número: "))
numeros = []

unidade = 0
dezena = 0
centena = 0
milhar = 0


for numero in num:
    numeros.append(numero)

numeros.reverse()

for pos,numero in enumerate(numeros):
    if pos == 0:
        unidade = numero

    if pos == 1:
        dezena = numero

    if pos == 2:
        centena = numero

    if pos == 3:
        milhar = numero





print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
