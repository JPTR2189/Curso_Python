#  Faça um programa que leia um número Inteiro
#  qualquer e mostre na tela a sua tabuada

numero = int(input("Digite um número inteiro: "))

print("-"  * 20)
print(f"A tabuada de {numero} é: ")
print("-"  * 20)

for indice in range(0, 11):
    print(f"{indice} x {numero} = {indice * numero}")