# Faça um algoritmo que imprima os números primos entre 0 e 100

print("Números primos de 0 a 100: ")

for num in range(1, 101):

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

    print(num)
    