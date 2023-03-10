import sqlite3
from app.crud import crud

db = sqlite3.connect("app/database/banco_dados.db")
query = f"SELECT * FROM logins"
resultado = db.execute(query).fetchall()
db.close()
print(resultado)

print(crud.autores())
#print(crud.excluir_autor(3))
#print(crud.logins())
#print(crud.autor(4))
