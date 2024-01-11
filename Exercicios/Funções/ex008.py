# Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados
# a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:

def func(**params):
    z = zip((params.keys()), (params.values()))
    d = dict(z)
    print(d)


func(a=1, b=2, c=3, d=4)