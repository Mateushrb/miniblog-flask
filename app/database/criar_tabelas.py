import sqlite3
def criar_tabela():
    db = sqlite3.connect("banco_dados.db")
    db.execute("""CREATE TABLE IF NOT EXISTS logins
                        (login_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login TEXT NOT NULL UNIQUE,
                        senha TEXT NOT NULL,
                        data_criacao DATE NOT NULL)""")
    db.commit()
    
    db.execute("""CREATE TABLE IF NOT EXISTS admins
                        (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        nome TEXT,
                        idade INTEGER,
                        bairro TEXT,
                        biografia TEXT,
                        FOREIGN KEY (admin_id) REFERENCES logins(login_id))""")
    db.commit()
    
    db.execute("""CREATE TABLE IF NOT EXISTS posts
                        (post_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        texto TEXT NOT NULL,
                        data DATE NOT NULL,
                        autor INTEGER NOT NULL,
                        FOREIGN KEY (autor) REFERENCES admins(admin_id))""")
    db.commit()
    
    db.close()

criar_tabela()