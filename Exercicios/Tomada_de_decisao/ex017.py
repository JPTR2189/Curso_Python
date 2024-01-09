# Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano. Por exemplo, se o usuário digitar
# a data 10/8 a mesma será inválida. Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.

data = str(input("Digite uma data (DD/MM/AA): "))

if data[0:3] .__contains__("/") and data[3:6] .__contains__("/"):
    print(30 * "-")
    print("Data VÁLIDA!")

else:
    print(30 * "-")

    print("Data INVÁLIDA!")