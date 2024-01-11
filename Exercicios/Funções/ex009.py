# def func(a, b, c, d)
#     print(a+b+c+d)
# lista = 1,2,3,4

# Invoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:

def func(a, b, c, d):
    print(a+b+c+d)


lista = 1,2,3,4

func(*lista)