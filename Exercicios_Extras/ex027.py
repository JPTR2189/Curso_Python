# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ")
nome_separado = nome.split()

print('-' * 30)
print("Prazer em te conhecer!")
print('-' * 30)
print(f"Seu primeiro nome é '{nome_separado[0]}'")
print(f"Seu último nome é '{nome_separado[len(nome_separado) - 1]}'")
