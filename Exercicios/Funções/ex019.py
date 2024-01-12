#  Escreva uma função que imprima somente os números pares
# Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Saída: [2, 4, 6, 8]

def pares(lista):
    for num in lista:
        if num % 2 == 0:
            print(num)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares(lista)