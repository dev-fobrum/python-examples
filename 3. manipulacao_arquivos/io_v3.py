#! python
# -*- coding: utf-8 -*-
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

# import os
# print(os.listdir())
