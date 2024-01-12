# Escreva uma função que receba como argumento uma lista que poderá ter valores
# duplicados e retorne uma nova lista sem que haja valores iguais.
# Lista: [1,2,3,3,3,3,4,5]
# Retorno: [1, 2, 3, 4, 5]

l = [2,1,2,3,3,3,3,4,5]

def sem_repetidos(lista):
    s = set(lista)
    nova_lista = list(s)
    print(nova_lista)


sem_repetidos(l)
