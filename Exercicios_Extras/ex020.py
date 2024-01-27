# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import choice

aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3° aluno: ")
aluno4 = input("Digite o nome do 4° aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = list()

while len(ordem) !=  len(alunos):

        escolhido = choice(alunos)

        if escolhido not in ordem:

            ordem.append(escolhido)






print("-" * 40)
print(f"A Ordem de apresentação é '{ordem}'")