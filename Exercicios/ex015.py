# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado

dias = int(input("Quantos dias o carro ficou alugado? "))
quilometros = float(input("Quantos Km o carro rodou? "))
total = (dias * 60) + (0.15 * quilometros)

print(f"O total a pagar é de R${total:.2f}")
