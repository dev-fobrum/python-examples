
lista_1 = [1, 2, 3]
dobro = list(map(lambda x: x * 2, lista_1))
print(dobro)

lista_2 = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26}
]

so_nomes = list(map(lambda p: p['nome'], lista_2))
print(so_nomes)

frase = list(
    map(
        lambda p: f"{p['nome']} tem {p['idade']} anos.", lista_2
    )
)

print(frase)
