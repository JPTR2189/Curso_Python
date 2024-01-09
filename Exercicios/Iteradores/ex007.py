# Faça um algoritmo que calcule os número primos num
# intervalo pré-determinado pelo usuário:

inicio = int(input("Digite um número para começar: "))

while inicio < 1:
    inicio = int(input("Digite um número para começar: "))

fim = int(input("Digite um número para terminar: "))

for num in range(inicio, fim + 1):

    if num < 2:
        continue

    if num != 2 and num % 2 == 0:
        continue

    if num != 3 and num % 3 == 0:
        continue

    if num != 5 and num % 5 == 0:
        continue

    if num != 6 and num % 6 == 0:
        continue

    if num != 7 and num % 7 == 0:
        continue

    if num != 8 and num % 8 == 0:
        continue

    if num != 9 and num % 9 == 0:
        continue

    if num != 10 and num % 10 == 0:
        continue

    print(num)