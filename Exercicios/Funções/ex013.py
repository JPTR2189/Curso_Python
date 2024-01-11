# Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. Não utilize a função
# interna do Python que faz inverção, crie o algoritmo que faça a inversão.

# Lista: "1234abcd"
# Saída: "dcba4321"

def inverte(lista):

    for c in range(len(lista) - 1, -1, -1):

        print(lista[c], end='')


lista = [1, 2, 3, 4, 5, 6]

inverte(lista)