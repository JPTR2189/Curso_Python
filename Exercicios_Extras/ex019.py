# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

print("-" * 40)
print(f"O Aluno escolhido foi '{choice(alunos)}'")