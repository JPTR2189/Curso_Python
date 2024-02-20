# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

palavra = input("Digite a cidade que você nasceu: ").upper().strip()

if palavra[0:5] == "SANTO":
    print('-' * 30)
    print("A cidade que você nasceu começa com o nome 'Santo'")

else:
    print('-' * 30)
    print("A cidade que você nasceu NÃO começa com o nome santo")
