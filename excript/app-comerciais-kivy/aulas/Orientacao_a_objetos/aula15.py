# MÉTODO ESTÁTICO

class MetodoEstatico:
    @staticmethod
    def func1():
        print("func1()")

    @staticmethod
    def func2(x, y):
        print(f"Função 'func2' invocada.\nParams=({x},{y})")

    @staticmethod
    def func3(a, b, c):

        info = f"""
        Nome: {MetodoEstatico.func3.__name__}
        Quantidade: {MetodoEstatico.func3.__code__.co_argcount}
        Args: {MetodoEstatico.func3.__code__.co_varnames}
        """

        print(info)

    # func1 = staticmethod(func1)
    # func2 = staticmethod(func2)
    # func3 = staticmethod(func3)


me = MetodoEstatico()

me.func1()
print(30 * '-')
me.func2(100, 200)
print(30 * '-')
me.func3(5, 10, 15)
