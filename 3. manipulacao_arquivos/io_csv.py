import csv

with open('desafio-ibge.csv') as ibge_data:
    for data in csv.reader(ibge_data):
        print(f'Nome origem: {data[3]} - Código destino: {data[8]}')

input()
