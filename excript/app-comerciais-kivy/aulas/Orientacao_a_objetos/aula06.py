# PERSONALIZANDO O METÓDO CONSTRUTOR

class Retangulo:
    def __init__(self, largura, altura):
       self.l = largura
       self.a = altura



    def area(self):
        return self.l * self.a

r = Retangulo(7, 5)

print(r.area())
