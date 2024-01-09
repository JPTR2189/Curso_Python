# ITERANDO LISTAS

numeros = [100, 200, 300, 400, 500, 600, 700]

for i in range(len(numeros)):

    numeros[i] += 1000

print(numeros)

print('-' * 50)

for pos, num in enumerate(numeros):
    numeros[pos] += 100

print(numeros)
