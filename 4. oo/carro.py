class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0

    def acelerar(self, delta=5):
        if self.velocidade + delta < 180:
            self.velocidade += delta
            return self.velocidade
        else:
            return self.velocidade_maxima

    def frear(self, delta=5):
        if self.velocidade - delta > 0:
            self.velocidade -= delta
            return self.velocidade
        else:
            return 0


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
