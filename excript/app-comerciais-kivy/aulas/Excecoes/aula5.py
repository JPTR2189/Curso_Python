# INSTÂNCIA DO ERRO

def erro(x):
    try:
        eval(x)

    except ValueError as e:

        print("ValueError")
        print(type(e)) # Instância da exceção
        print(e.args) # Argumentos das mensagens
        print(e) # __str__ mensagem

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except (TypeError, NameError)as e:

        print(type(e))  # Instância da exceção
        print(e.args)  # Argumentos das mensagens
        print(e)  # __str__ mensagem


# # Type Error
erro("int + int")

# # Name Error
erro("a")

# Value Error
# erro("int('a')")

# # ZeroDivision Error
# erro("10/0")
#
# # Sem Erro
# erro("10 + 10")
print("A aplicação foi finalizada")
