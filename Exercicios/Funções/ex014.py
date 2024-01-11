# Escreva uma função que calcule o fatorial de um número (um inteiro não negativo).
# Envie o valor do número que será calcula como argumento da função.

import math
def fatorial(num):

    if num > 0:

        for n in range(num, 0, -1):

            print(n, end='')
            print(" *" if n > 1 else f' = {math.factorial(num)}', end=' ')


fatorial(5)
