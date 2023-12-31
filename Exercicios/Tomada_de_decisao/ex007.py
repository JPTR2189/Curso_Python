# Faça um algoritmo que peça dois números. Primeiro,
# imprima o maior e, em seguida, o menor.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

numeros = [num1, num2]

print("-" * 30 )
print(f"O Maior número é '{max(numeros)}'")
print(f"O Menor número é '{min(numeros)}'")