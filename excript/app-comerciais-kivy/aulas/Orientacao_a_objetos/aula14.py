# METÓDOS DE CLASSE

class Bichos:
    qnt_bichos = 0
    def __init__(self):
        self.add_bicho()

    def __del__(self):
        self.del_bicho()
        if self.qnt_bichos == 0:
            print("Todos os bichos foram mortos!")

    @classmethod
    def add_bicho(cls):
        cls.qnt_bichos += 1

    @classmethod
    def del_bicho(cls):
        cls.qnt_bichos -= 1

    # add_bicho = classmethod(add_bicho)
    # del_bicho =classmethod(del_bicho)


b1 = Bichos()
print(Bichos.qnt_bichos)
b2 = Bichos()
print(Bichos.qnt_bichos)
b3 = Bichos()
print(Bichos.qnt_bichos)

del(b1)
print(Bichos.qnt_bichos)
del(b2)
print(Bichos.qnt_bichos)
del(b3)
print(Bichos.qnt_bichos)
