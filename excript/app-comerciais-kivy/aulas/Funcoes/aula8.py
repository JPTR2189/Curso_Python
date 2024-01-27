# DESEMPACOTAMENTO

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)


tupla = "Tupla", "Brasil", 20
lista = ["Lista", "Brasil", 20]
dic = {'nome': 'Dicionário', 'sobrenome': 'Brasil', 'idade': 20 }

pessoa(*tupla)
print('-' * 30)
pessoa(*lista)
print('-' * 30)
pessoa(**dic)
print('-' * 30)
