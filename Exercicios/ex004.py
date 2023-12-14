# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

entrada = input("Digite Algo: ")
capitalizada = False

print(f"O tipo primitivo desse valor é {entrada.__class__}")
print(f"Só tem espaços? {entrada.isspace()}")
print(f"É um número? {entrada.isnumeric()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"É alfanumérico? {entrada.isalnum()}")
print(f"Está em maiúsculas? {entrada.isupper()}")
print(f"Está em minúsculas? {entrada.islower()}")

if entrada[0] == entrada.capitalize()[0]:
    capitalizada = True
    print(f"Está capitalizada? {capitalizada} ")
else:
    print(f"Está capitalizada? {capitalizada}")
