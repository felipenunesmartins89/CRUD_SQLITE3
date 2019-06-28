from insert import db_insert, db_select, db_update, db_delete
from pprint import pprint
#
# name = str(input('Digite o nome: '))
# phone = str(input('Digite otelefone: '))
# email = str(input('Digite o e-mail: '))
# db_insert(name, phone, email)


pprint(db_select('1321389310', 'phone')) #print formatado passando o telefone como parametro

