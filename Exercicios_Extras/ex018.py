# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan


angulo = radians((float(input("Digite o valor do ângulo: "))))

cos = cos(angulo)
sen = sin(angulo)
tan = tan(angulo)

print("-" * 40)
print(f"O Cosseno desse ângulo é: {cos:.2f}")
print(f"O Seno desse ângulo é: {sen:.2f}")
print(f"A Tangente desse ângulo é: {tan:.2f}")
