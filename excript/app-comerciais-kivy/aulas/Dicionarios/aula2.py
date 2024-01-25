# FUNÇÕES DOS DICIONÁRIOS

tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste"

}

print(tel)
print(f"O Tamanho desse dicionário é {len(tel)}")
print("-" * 40)

del(tel[36458899])

print(tel)
print(f"O Tamanho desse dicionário é {len(tel)}")
print("-" * 40)

print(tel.keys())
print(tel.values())
print("-" * 40)

print(f"Removido: '{tel.popitem()}'")
print(tel)
print(f"Removido: '{tel.popitem()}'")
print(tel)
print(f"Removido: '{tel.popitem()}'")
print("-" * 40)

tel2 = {99999999: "teste1", 55551111: "teste2"}
tel.update(tel2)
t = (10, 10, 10)
tel[t] = "eXcript"
print(tel)
