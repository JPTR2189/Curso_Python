# ARQUIVO USADO EXCLUSIVAMENTE PARA TESTES

class objeto_classe:
    membro_cls = 0
    def __init__(self):
        self.membro_inst = 10

a = objeto_classe()
b = objeto_classe()

print(dict(a.__dict__))
print(a.membro_cls)


objeto_classe.membro_cls2 = 100
a.membro_cls2 = 200

print('-' * 20)

print(a.membro_cls2)
print(b.membro_cls2)