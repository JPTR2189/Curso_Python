# ITERANDO STRINGS

# Exemplo 1

# s = 'Iterando Strings'
# for c in s:
#     print(c)


# Exemplo 2

# s = 'Iterando Strings'
# indice = 0
#
# while indice < len(s):
#     print(indice, "-", s[indice])
#     indice += 1

# Exemplo 3

for pos, c in enumerate('Iterando Strings'):
    print(f"{pos} - {c}")