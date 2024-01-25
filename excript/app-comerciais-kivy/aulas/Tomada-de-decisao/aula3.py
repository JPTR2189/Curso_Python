# BLOCOS DE INSTRUÇÃO

num1 = int(input("Digite um número: "))

if num1 > 10:
    print("O número é maior do que 10!")

    if num1 <= 15:
        print("O número é maior do que 10 e menor igual a 15")

    else:
        if num1 <= 50:
            print("O número é maior do que 10 e menor igual a 50")

        else:
            print("O número é maior do que 50")




else:
    if num1 > 5:
        print("O número é menor igual a 10 mas maior do que 5!")

        if num1 == 7:
            print("O número é igual a 7")

    else:
        print("O número é menor igual a 5")