# OBJETO CLASSE

class MinhaClasse:
    membro_cls = 50

    def __init__(self):
        self.membro_inst = -10


    def func(self):
        print(self.membro_inst)# Membro instância
        print(self.membro_cls) # Instância classe
        print(MinhaClasse.membro_cls) # Objeto Classe



i1 = MinhaClasse()
i2 = MinhaClasse()

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

i1.membro_cls = 1000
print('-' * 15)

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

MinhaClasse.membro_cls = 1000
print('-' * 15)

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)


# i1.membro_inst = 10
#
# print(f"I1: {i1.membro_inst}")
# print(f"I2: {i2.membro_inst}")

# MinhaClasse.membro_cls = 9
# print("-" * 20)

# print(f"I1: {i1.membro_cls}")
# print(f"I2: {i2.membro_cls}")

