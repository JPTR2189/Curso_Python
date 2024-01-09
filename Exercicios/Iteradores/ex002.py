# Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo
# que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso

inicio = int(input("Qual número você quer começar? "))
fim = int(input("Qual número você quer terminar? "))

for num in range(inicio, fim + 1):
    print(num)