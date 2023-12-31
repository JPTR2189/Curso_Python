# Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mês correspondente. Por exemplo,
# se for informado o número 2, o algoritmo deverá exibir: fevereiro. O algoritmo também deve validar se a entrada está correta

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro","Novembro", "Dezembro"]

mes = int(input("Digite um mês do ano (em um número): "))


if type(mes) != int or 1 < mes > 12:
    print("-" * 30)
    print(f"Digite um mês válido!")

else:
    print("-" * 30)
    print(f"Você escolheu o mês '{meses[mes - 1]}'")

