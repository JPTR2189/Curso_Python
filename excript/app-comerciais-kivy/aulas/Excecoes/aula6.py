# BLOCO ELSE

def erro(x):
    try:
        eval(x)

    except ValueError as e:

        print(type(e))

    except ZeroDivisionError:
        print("ZeroDivisionError")

    except (TypeError, NameError)as e:
        print(type(e))

    else:
        print("Nenhuma exceção ocorreu")


# # Type Error
erro("int + int")

# # Name Error
erro("a")

# Value Error
erro("int('a')")

# ZeroDivision Error
erro("10/0")

# # Sem Erro
erro("10 + 10")

print("A aplicação foi finalizada")
