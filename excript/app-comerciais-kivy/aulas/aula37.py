# OPERADORES 'IN' E 'NOT IN'

a = 10
b = 25
c = 66

num = int(input("Digite um número: "))

if num in [a, b, c]:
    print("Está contido")

else:
    print("NÃO está contido")

print("-" * 60)

# ---------------------------------------------------------------

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:

    valor = input("Digite o nome de uma cor (0 para sair): ").lower()

    if valor == '0':
        break

    elif valor in cores:
        print(f"Você digitou a cor {valor}")
        print("-" * 40)

    else:
        print("Essa cor NÃO está contida")
    print()
