#  Escreva uma função que aceite Strings e calcule a quantidade de letras
#  em mauisculas e minúsculas que a String possui.

def calcula_letras(string):
    maiuscula = 0
    minuscula = 0

    for letra in string:
        if letra == letra.upper():
            maiuscula += 1

        elif letra == letra.lower():
            minuscula += 1


    print(f"Na palavra '{string}' há {maiuscula} letras maiúsculas")
    print(f"Na palavra '{string}' há {minuscula} letras minúsculas")

calcula_letras("Abacaxi")
