# INSTRUÇÃO BREAK

print("Antes de entrar no laço")
for item in range(10):
    print(item)
    if item == 6:
        print("A condição estabelecida retornou TRUE")
        break

print("Depois de entrar no laço")