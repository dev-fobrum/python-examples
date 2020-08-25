from db import nova_conexao
from mysql.connector.errors import ProgrammingError
import random

sql = 'INSERT INTO contatos(nome, tel) VALUES (%s, %s)'
args = (
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
    ('Aluno #' + str(random.randint(1, 500)), random.randint(1, 500)),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.rowcount} registros!')
