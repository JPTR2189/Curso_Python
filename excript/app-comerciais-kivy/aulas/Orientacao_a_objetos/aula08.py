# GETTERS E SETTERS

class Retangulo:

    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):

        if not (isinstance(num, int) and num > 0):
            raise ValueError(f"Altura inválida: {num}")

        self.altura = num

    def set_largura(self, num):

        if not (isinstance(num, int) and num > 0):

            raise ValueError(f"Largura inválida: {num}")


        self.largura = num

    def get_area(self):
        return self.altura * self.largura

r = Retangulo(largura= 5, altura= "10")
