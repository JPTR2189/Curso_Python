# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

salario = float(input("Digite seu salário: R$"))
aumento = (salario / 100) * 15

print("-" * 60)
print(f"Seu novo salário com aumento de 15% é: R${salario + aumento}")