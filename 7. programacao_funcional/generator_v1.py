def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'


if __name__ == "__main__":
    generator = cores_arco_iris()

    while True:
        try:
            print(next(generator))
        except StopIteration:
            print('Lista vazia')
            break
