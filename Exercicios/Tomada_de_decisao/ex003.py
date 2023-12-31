# Faça um algoritmo que leia dois números e imprima o maior.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2:
    print(f"O número '{num1}' é maior que o número '{num2}'")

if num2 > num1:
    print(f"O número '{num2}' é maior que o número '{num1}'")
