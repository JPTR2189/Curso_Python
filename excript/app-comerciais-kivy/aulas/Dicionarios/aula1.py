# DICIONÁRIOS

d1 = {}
print(type(d1))

d2 = dict()
print(type(d2))

print("-" * 40)

d1["aaa"] = 1000
d1["bbb"] = 2000
d1["ccc"] = 3000

print(d1)

print(f"A chave de 'aaa' é {d1['aaa']}")

print("-" * 40)

d2 = {1.1: "teste1", 2.2: "teste2", 3: "teste3"}

print(d2)
print(f"O Valor de '2.2' é '{d2[2.2]}'")