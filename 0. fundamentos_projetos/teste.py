# Lista com pares
lista = [i for i in range(0, 15) if i % 2 == 0]
print('Lista com valores pares: ', lista, '\n')

# Dicionário x * 2 = y somente com ímpares
dicionario = {i: i * 2 for i in range(10) if i % 2 != 0}
print('Dicionário com valores ímpares e seus dobros:', dicionario, end='\n\n')

print('Ou em um for')
for valor, dobro in dicionario.items():
    print(f'{valor} * 2 = {dobro}')
