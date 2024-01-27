<<<<<<< HEAD
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Exemplo de uso:
numero = 100
if is_prime(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
=======
# ARQUIVO USADO EXCLUSIVAMENTE PARA TESTES

help(dir())
>>>>>>> aulas-python
