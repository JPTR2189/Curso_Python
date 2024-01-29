# TRATAMENTO DE EXCEÇÕES MÚLTIPLAS 1

def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")

# Type Error
erro("int + int")

# Name Error
erro("a")

# Value Error
erro("int('a')")

# ZeroDivision Error
erro("10/0")

# Sem Erro
erro("10 + 10")
print("A aplicação foi finalizada")