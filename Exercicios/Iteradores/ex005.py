# Faça um algoritmo que some a quantidade de números
# pares encontrados no intervalo entre 0 e 100

soma = 0

for num in range(0, 101):

    if num % 2 == 0:
        soma += num


print(f"A soma de todos os números PARES no intervalo de 0 a 100 é: {soma}")
