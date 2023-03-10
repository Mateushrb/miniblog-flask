import sqlite3
from app.crud import crud

db = sqlite3.connect("app/database/banco_dados.db")

consulta_logins = db.execute("SELECT * FROM logins")
for i in consulta_logins:
    print(i)

consulta_admins = db.execute("SELECT * FROM admins")
for i in consulta_admins:
    print(i)
    
consulta_posts = db.execute("SELECT * FROM posts")
for i in consulta_posts:
    print(i)

consulta = db.execute("SELECT nome FROM admins where admin_id == 1")
for i in consulta:
    print(i)

consulta = db.execute("SELECT data_criacao FROM logins")
for i in consulta:
    print(i)


    
db.close()










