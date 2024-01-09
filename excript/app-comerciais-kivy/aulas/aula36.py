# OPERADORES 'IN' E 'NOT IN'

t = 1, 2, 3, 4, 5, 6

print(2 in t)
print(2 not in t)

print("-" * 30)

print(3 in range(4, 10))
print(3 not in range(4,10))

print("-" * 30)

lista = list(range(2, 8))

if 5 in lista:
    print(f"Contido")

else:
    print("Não contido")

if 0 in lista:
    print(f"Contido")

else:
    print("Não contido")