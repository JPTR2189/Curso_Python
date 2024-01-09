# FUNÇÕES ANINHADAS

def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()

func()
