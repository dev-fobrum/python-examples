from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'SELECT nome, tel FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print('Nome\t\tTelefone')
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    # for contato in cursor.fetchall():
    #     print('\t'.join(str(campo) for campo in contato))
