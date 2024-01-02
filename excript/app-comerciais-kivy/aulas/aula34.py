# QUANTIDADE DE ELEMENTOS (LISTA)

lista = ["Ana", "Bruna", "Carla", "Eduardo"]

print(f"O Tamanho dessa lista é '{len(lista)}'")
print(f"O Primeiro elemento dessa lista é '{lista[0]}'")
print(f"O Último elemento dessa lista é '{lista[-1]}'")

print("-" * 40)

lista.insert(2, 'Ana')
lista.append("Ana")

print(f"O nome 'Ana' está presente {lista.count('Ana')} vezes na lista")
print(f"Eduardo está na posição '{lista.index('Eduardo')}' da lista")
print(f"Ana está na posição '{lista.index('Ana')}' da lista")
