#  Faça um algoritmo que leia três números e imprima-os em ordem crescente

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))

numeros = [num1, num2, num3]

numeros.sort()

print("-" * 30)
print(f"Os números em ordem crescente são: {numeros}")