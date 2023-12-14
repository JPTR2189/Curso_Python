# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

preco = float(input("Digite o preço do produto: R$"))
desconto = (preco / 100) * 5

print("-" * 70)
print(f"O preço do produto com o desconto de 5% aplicado é: R${preco - desconto}")
