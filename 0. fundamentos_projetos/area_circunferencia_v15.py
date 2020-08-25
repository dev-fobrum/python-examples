#! python
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[94m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio)**2


def help():
    print("É necessário informar o raio do círculo.")
    print(f'Sintaxe: {sys.argv[0]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        # sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO, 'O raio deve ser um valor númerico',
              TerminalColor.NORMAL)
        # sys.exit(errno.EINVAL)
    else:
        area = circulo(sys.argv[1])
        print('Area do circulo', area)
input('Press ENTER to exit')
