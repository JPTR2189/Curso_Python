# Faça um algoritmo que leia três números e imprima na tela o maior deles

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))

numeros = [num1, num2, num3]

print("-" * 30)
print("O Maior número digitado foi:", max(numeros))
