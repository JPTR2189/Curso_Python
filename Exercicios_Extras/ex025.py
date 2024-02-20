# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome: ").strip().upper()

if "SILVA" in nome:
    print('-' * 30)
    print("Você tem 'Silva' no nome")

else:
    print('-' * 30)
    print("Você não tem 'Silva no nome'")
