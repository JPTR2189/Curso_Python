# Faça um algoritmo que verifica se um determinado valor é do tipo decimal.

valor = (input("Digite um valor: "))
decimal = False

if valor.__contains__("."):
    decimal = True


print(f"É um número Decimal? ---- {decimal}")