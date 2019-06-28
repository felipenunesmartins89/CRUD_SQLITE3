"""
DML - Manipulação de dados
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""

import sqlite3


# sql = """
# CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL)"""
#
# cur.execute(sql)
# con.commit()
# con.close()


#comita e fecha o código, decorador
def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator


@commit_close
def db_insert(name, phone, email):
    return """
    INSERT INTO users(name, phone, email)
        VALUES ('{}', '{}', '{}')
    """.format(name, phone, email)

@commit_close
def db_update(name, email):
   return  """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email ='{}'
    """.format(email)

def db_select(field, data):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = """
    SELECT id, name, phone, email
    FROM users
    WHERE {}={}
    """.format(field, data)
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data



#cur.execute(db_insert('webnets', '1321389310', 'contato@webnets.com.br'))
#cur.execute(db_update('fernando', 'contato@webnets.com.br'))
#cur.execute(db_delete('contato@webnets.com.br'))







