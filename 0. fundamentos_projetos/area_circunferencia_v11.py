#! python
from math import pi
import sys


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo.")
        print(f'Sintaxe: {sys.argv[0]} <raio>')

        input('Press ENTER to exit')
    else:
        area = circulo(sys.argv[1])

        print('Area do circulo', area)

        input('Press ENTER to exit')
