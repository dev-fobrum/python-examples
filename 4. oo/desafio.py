class ClasseSimples():
    quantidade = 0

    def __init__(self):
        self.contador()

    @classmethod
    def contador(cls):
        cls.quantidade += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples(),
             ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.quantidade)
