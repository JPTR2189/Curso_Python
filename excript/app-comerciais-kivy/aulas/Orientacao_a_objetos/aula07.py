# ENCAPSULAMENTO

class Retangulo:
    def __init__(self, largura, altura):
       self.l = largura
       self.a = altura



    def area(self):
        return self.l * self.a

r = Retangulo(10, 5)
r.l = "teste"

print(r.area())
