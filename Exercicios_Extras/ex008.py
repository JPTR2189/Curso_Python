# Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros

valor = float(input("Digite uma distância (m): "))

print("-" * 30)
print(f"A medida de {valor}m corresponde a:")
print("-" * 30)

print(f"Km: {valor / 1000}")
print(f"Hm: {valor / 100}")
print(f"Dam: {valor / 10}")
print(f"Dm: {valor * 10}")
print(f"Cm: {valor * 100}")
print(f"Mm: {valor * 1000}")