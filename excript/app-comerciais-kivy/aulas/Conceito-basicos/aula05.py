# Módulo da Divisão (Resto da Divisão)

print("*" * 20)
print("RESTO DA DIVISÃO")
print("*" * 20)
print()
print(3 % 2)
print(7 % 3.1)
print(900 % 100)

print()

print("-" * 30)
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
print("-" * 30)

print()

divisao = num1 / num2
resto = num1 % num2

print(f"'{num1}' divido por '{num2}' é igual a '{divisao}'")
print(f"O Resto da divisão entre '{num1}' e '{num2}' é '{resto}'")
