# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input("Digite o valor do Cateto Oposto: "))
cateto_adjacente = float(input("Digite o valor do Cateto Adjacente: "))
hipotenusa = (cateto_oposto**2 + cateto_adjacente **2) ** 0.5


print(f"O valor da Hiptenusa é: {hipotenusa:.2f}")
