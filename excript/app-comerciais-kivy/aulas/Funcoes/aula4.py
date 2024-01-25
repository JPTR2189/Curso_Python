# FUNÇÕES - PARÂMETROS NOMEADOS

def dados_pessoais(nome, sobrenome, idade, sexo):
    print(f"Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nSexo: {sexo}")


dados_pessoais("João", "Pedro", 24, "M")
print("-" * 30)
dados_pessoais(sexo="F", nome="Pedro", idade="32", sobrenome="Correia")
