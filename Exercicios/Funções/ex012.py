# Escreva uma função que multiplique todos os números de uma lista.
# Lista: (1, 2, 3, 4, 5)
# Multiplicação: 120

def multiplica(lista):

    total = 1
    for pos, num in enumerate(lista):

        if pos <= len(lista) - 1:

            total *= num

    print(total)


lista = [1, 2, 3, 4, 5]

multiplica(lista)