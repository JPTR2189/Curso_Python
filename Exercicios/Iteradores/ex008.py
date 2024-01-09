# Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o mesmo
# possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:

inicio = int(input("Digite um número para começar: "))
fim = int(input("Digite um número para terminar: "))

num1 = int(input("Digite um número para ser ignorado: "))
num2 = int(input("Digite outro número para ser ignorado: "))
num3 = int(input("Digite outro número para ser ignorado: "))


for num in range(inicio, fim + 1):

    if num == num1 or num == num2 or num == num3:
        continue

    else:
        print(num)
        