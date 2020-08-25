#!python


def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == "__main__":
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro(5), triplo(5))
