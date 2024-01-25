# DESEMPACOTAMENTO

lista = [11, 10, 12]
tupla = 11, 10, 12

def func(a, b, c):
    print(a)
    print(b)
    print(c)


lista.sort()
func(*lista)

print("-" * 20)

lista_tupla = [*tupla]
lista_tupla.sort()
func(*lista_tupla)

print('-' * 20)

func(**dict(zip(('b', 'a', 'c'), tupla)))
