# Faça um algoritmo que peça um valor numérico. Em seguida,
# verifique se o número é inteiro ou decimal.

valor = input("Digite um número: ")
decimal = False

if valor.__contains__("."):
    decimal = True



print("É um número inteiro? ----- ", valor.isdecimal())
print("É decimal ----- ", decimal)
