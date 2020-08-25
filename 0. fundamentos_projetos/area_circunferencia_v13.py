#! python
from math import pi
import sys
import errno


def circulo(raio):
    return pi * float(raio)**2


def help():
    print("É necessário informar o raio do círculo.")
    print(f'Sintaxe: {sys.argv[0]} <raio>')

    input('Press ENTER to exit')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    area = circulo(sys.argv[1])

    print('Area do circulo', area)

    input('Press ENTER to exit')
