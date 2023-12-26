# Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não

charactere = input("Digite um caractere: ").upper()

vogais = ['A', 'E', 'I', 'O', 'U']

print("É uma vogal? ----- ", charactere in vogais)