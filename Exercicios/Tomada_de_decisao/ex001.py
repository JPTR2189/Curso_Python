# Faça um algoritmo que leia um número e mostre
# se o mesmo é positivo, negativo ou zero

num = int(input("Digite um número: "))
print("-" * 20)


if num < 0:
    print(f"'{num}' é NEGATIVO")

elif num > 0:
    print(f"'{num}' é POSITIVO")