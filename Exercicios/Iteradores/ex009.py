# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar
# uma letra. Caso a letra seja o "q" finalize a aplicação. Do contrário, imprima novamente a
# mesma frase até que o caractere "q" seja enviado:

print("Estou em looping")

letra = input("Digite uma letra: ").lower()

while letra != 'q':

    letra = input("Digite uma letra: ").lower()

print("O Programa foi finalizado!")