#! python
from math import pi
import sys


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    area = circulo(sys.argv[1])

    print('Area do circulo', area)

    input('Press ENTER to exit')
