# VISIBILIDADE DE MEMBROS

class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.__var = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):

        if not (isinstance(num, int) and num > 0):
            raise ValueError(f"Altura inválida: {num}")

        self._altura = num
        self.__var = 456

    def set_largura(self, num):

        if not (isinstance(num, int) and num > 0):

            raise ValueError(f"Largura inválida: {num}")


        self._largura = num

    def get_area(self):
        return self._altura * self._largura

    def get_dado(self):
        return self._Retangulo__var

r = Retangulo(largura= 5, altura= 10)
r._Retangulo__var = 1
r._largura = 10
print(r.get_area())
print(r.get_dado())
