from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos(nome, tel) VALUES (%s, %s)'
args = ('Fernando', '43999887766')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Novo registro incluido. ID: ', cursor.lastrowid)
