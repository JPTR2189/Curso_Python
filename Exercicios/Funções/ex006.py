# Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos. Invoque a primeira função de ``func1()`` e a
# segunda de ``func2()``. Em seguida, invoque os parâmetros da segunda função de x e y. Some x e y e retorne o resultado. Em func1(),
# ao receber o resultado, retorne-o também como valor de retorno da função. Por fim, imprima na tela o valor que foi calculado por
# func2(), retornado para func1() e retornado a quem invocou a função inicialmente:

def func1(a, b):
    def func2(a, b):
        return a + b

    return func2(a, b)


print(func1(3, 2))


