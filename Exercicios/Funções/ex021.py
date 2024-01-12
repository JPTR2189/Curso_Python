# Escreva uma função que tenha definida uma função em seu escopo. Invoque a função
# aninhada, retorne algum valor, imprima esse valor na tela e finalize a aplicação.

def func():
    def func2():
        return 1

    print(func2())


func()