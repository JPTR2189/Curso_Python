# Crie um algoritmo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada
import math

numero = int(input("Digite um número: "))
print('-' * 50)

print(f"O Dobro de {numero} é {numero * 2}")
print(f"O Triplo de {numero} é {numero * 3}")
print(f"A Raiz quadrada de {numero} é {math.sqrt(numero)}")
