# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome: ").strip()
nome_separado = nome.split()

print('-' * 40)
print(nome.upper())
print(nome.lower())
print('-' * 40)
print(f"Seu nome há {len(nome_separado[0] + nome_separado[1])} letras")
print(f"Seu primeiro nome tem {len(nome_separado[0])} letras")
print('-' * 40)
