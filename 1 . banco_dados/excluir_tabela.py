from db import nova_conexao
from mysql.connector import ProgrammingError

excluir_email = """
    DROP TABLE IF EXISTS emails
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_email)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
