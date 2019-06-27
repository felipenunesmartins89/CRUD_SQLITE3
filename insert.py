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
    """

    """


cur.execute(db_insert('webnets', '1321389310', 'contato@webnets.com.br'))
con.commit()
print('Dados inseridos com sucesso')
con.close()






