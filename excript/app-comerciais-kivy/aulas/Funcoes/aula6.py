# FUNÇÕES - RETORNO DE VALORES MÚLTIPLOS

def potencia(num):
    quadrado = num**2
    cubo = num**3

    return quadrado, cubo


valor = 2
a, b = potencia(valor)

print(f"O Quadrado de '{valor}' é '{a}'")
print(f"O Cubo de '{valor}' é '{b}'")