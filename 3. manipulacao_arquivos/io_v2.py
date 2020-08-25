#! python
# -*- coding: utf-8 -*-
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')

arquivo.close()

# import os
# print(os.listdir())
