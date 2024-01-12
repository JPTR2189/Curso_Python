# Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros
# e imprima na telas os números primos contidos nessa lista.

def primos(*params):
    lista = list(params)
    maior = max(lista)
    menor = min(lista)

    for num in range(menor, maior + 1):

        if num < 2:
            continue

        if num != 2 and num % 2 == 0:
            continue

        if num != 3 and num % 3 == 0:
            continue

        if num != 5 and num % 5 == 0:
            continue

        if num != 6 and num % 6 == 0:
            continue

        if num != 7 and num % 7 == 0:
            continue

        if num != 8 and num % 8 == 0:
            continue

        if num != 9 and num % 9 == 0:
            continue

        if num != 10 and num % 10 == 0:
            continue

        print(num)


primos(1,2,3,4,5,6,7,8,9,10)