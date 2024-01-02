# MODIFICANDO UMA LISTA

lista = ["bbb", "ccc", "ddd"]

lista.append("eee")
lista.insert(0, "aaa")

print(lista)
print('-' * 50)

lista.pop()
lista.pop(1)

print(lista)
print("-" * 50)

lista = ["aaa", "bbb", "ccc", "ddd", "eee"]

del [lista[::2]]

print(lista)

lista.clear()

print("-" * 50)
print(lista)