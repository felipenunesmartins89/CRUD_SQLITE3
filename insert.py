import sqlite3
con = sqlite3.connect('base.db')
cur = con.cursor()

# sql = """
# CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL)"""
#
# cur.execute(sql)
# con.commit()
# con.close()

def db_insert (name, phone, email):
    return """
    INSERT INTO users(name, phone, email)
        VALUES ('{}', '{}', '{}')
    """.format(name, phone, email)

def db_update(name, email):
   return  """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

def db_delete(email):
    return """
    DELETE FROM users WHERE email ='{}'
    """.format(email)

#cur.execute(db_insert('webnets', '1321389310', 'contato@webnets.com.br'))
#cur.execute(db_update('fernando', 'contato@webnets.com.br'))
cur.execute(db_delete('contato@webnets.com.br'))

con.commit()
print('Ação feita com sucesso')
con.close()






