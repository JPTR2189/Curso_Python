# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar

dinheiro = float(input("Digite quanto dinheiro você tem na carteira: R$"))

print("-" * 60)
print(f"Com R${dinheiro} você pode comprar U$ {dinheiro / 4.914:.2f}")