# Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima
# na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:

def func(a, b, c):
    lista = [a, b, c]
    lista.sort()
    media = sum(lista) / len(lista)
    print(lista)
    print(f"A média de '{a}', '{b}' e '{c}' é igual a {media} ")


func(4, 1, 7)