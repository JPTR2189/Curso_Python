# FUNÇÃO VARIÁDICA

def lista_de_argumentos(*args):
    print(args)


def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)


def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


lista_de_argumentos(1, 2, "Um", "Dois")
print("-" * 60)
lista_de_argumentos_associativos(um=1, dois="2", tres="3", quatro=4)
print("-" * 60)
argumentos(1, 2,True,"teste", um="1", dois="2", teste=False)
