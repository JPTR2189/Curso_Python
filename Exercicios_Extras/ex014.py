# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit

temperatura = float(input("Digite a temperatura: °C "))
temperatura_convertida = (temperatura * 9/5) + 32

print("-" * 60)
print(f"A temperatura de {temperatura}°C corresponde a {temperatura_convertida}°F")