# Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

def is_palindromo(string):
    crescente = list()
    decrescente = list()

    for pos in range(0, len(string)):
        crescente.append(string[pos])

    for pos in range(len(string) -1, -1, -1):
        decrescente.append(string[pos])

    if crescente == decrescente:
        print("A Palavra é um palíndromo!")

    else:
        print("A Palavra não é um palíndromo!")


is_palindromo("arara")
