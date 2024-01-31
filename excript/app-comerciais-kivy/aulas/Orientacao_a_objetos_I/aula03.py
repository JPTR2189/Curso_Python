# METÓDO CONSTRUTOR

class A:

    def __init__(self):
        print(id(self))

a = A()
print(id(a))