import sqlite3
from datetime import date

class crud():

    def biografia(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_biografia = f"SELECT biografia FROM admins WHERE admin_id == '{id}'"
        biografia = db.execute(pega_biografia).fetchone()[0]
        db.close()
        return biografia

    def bairro(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_bairro = f"SELECT bairro FROM admins WHERE admin_id == '{id}'"
        bairro = db.execute(pega_bairro).fetchone()[0]
        db.close()
        return bairro

    def idade(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_idade = f"SELECT idade FROM admins WHERE admin_id == '{id}'"
        idade = db.execute(pega_idade).fetchone()[0]
        db.close()
        return idade
    def pass_user(user):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_pass = f"SELECT senha FROM logins WHERE login == '{user}'"
        password = db.execute(pega_pass).fetchone()[0]
        db.close()
        return password

    def id_user(user):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_id = f"SELECT login_id FROM logins WHERE login == '{user}'"
        id = db.execute(pega_id).fetchone()[0]
        db.close()
        return id
    
    def user(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_user = f"SELECT login FROM logins WHERE login_id == '{id}'"
        user = db.execute(pega_user).fetchone()[0]
        db.close()
        return user

    def logins():
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_logins = f"SELECT login FROM logins"
        logins = db.execute(pega_logins).fetchall()
        loginList = []
        for l in logins:
            loginList.append(l[0])
        db.close()
        return loginList

    def autores():
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_autores = f"SELECT * FROM admins"
        autores = db.execute(pegar_autores).fetchall()
        db.close()
        return autores

    def postagens():
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_postagens = f"SELECT * FROM posts"
        postagens = db.execute(pegar_postagens).fetchall()
        db.close()
        return postagens
    
    def titulo(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_titulo = f"SELECT titulo FROM posts WHERE post_id == {id}"
        titulo = db.execute(pegar_titulo).fetchone()[0]
        db.close()
        return titulo

    def texto(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_texto = f"SELECT texto FROM posts WHERE post_id == {id}"
        texto = db.execute(pegar_texto).fetchone()[0]
        db.close()
        return texto
    
    def autor(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_autor = f"SELECT nome FROM admins WHERE admin_id == {id}"
        autor = db.execute(pegar_autor).fetchone()[0]
        db.close()
        return autor
    
    def data(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pegar_data = f"SELECT data FROM posts WHERE post_id == {id}"
        data = db.execute(pegar_data).fetchone()[0]
        db.close()
        return data
    
    def cadastrar_usuario(login, senha):
        db = sqlite3.connect("app/database/banco_dados.db")
        insercao = f"INSERT INTO logins (login, senha, data_criacao) VALUES ('{login}', '{senha}', '{date.today()}')"
        db.execute(insercao)
        db.commit()
        insercao2 = f"INSERT INTO admins (nome, biografia, idade, bairro) VALUES (NULL, NULL, NULL, NULL)"
        db.execute(insercao2)
        db.commit()
        db.close()
    
    def completar_cadastro(id, nome, idade, bairro, biografia):
        db = sqlite3.connect("app/database/banco_dados.db")
        completar = f"UPDATE admins SET nome = '{nome}', idade = '{idade}', bairro = '{bairro}', biografia = '{biografia}' WHERE admin_id == '{id}'"
        db.execute(completar)
        db.commit()
        db.close()
    
    def postar(titulo, texto, autor):
        db = sqlite3.connect("app/database/banco_dados.db")
        postagem = f"INSERT INTO posts (titulo, texto, data, autor) VALUES ('{titulo}', '{texto}', '{date.today()}', '{autor}')"
        db.execute(postagem)
        db.commit()
        db.close()

    def atualizar_post(id, titulo, texto):
        db = sqlite3.connect("app/database/banco_dados.db")
        atualiza_postagem = f"UPDATE posts SET titulo = '{titulo}', texto = '{texto}' WHERE post_id == '{id}'"
        db.execute(atualiza_postagem)
        db.commit()
        db.close()

    def id_autor_post(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        pega_id_autor = f"SELECT autor FROM posts WHERE post_id == {id}"
        id_autor = db.execute(pega_id_autor).fetchone()[0]
        db.close()
        return id_autor
    
    def excluir_post(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        excluir_post = f"DELETE FROM posts WHERE post_id == {id}"
        db.execute(excluir_post)
        db.commit()
        db.close()

    def excluir_autor(id):
        db = sqlite3.connect("app/database/banco_dados.db")
        excluir_login = f"DELETE FROM logins WHERE login_id == {id}"
        db.execute(excluir_login)
        excluir_autor = f"DELETE FROM admins WHERE admin_id == {id}"
        db.execute(excluir_autor)
        excluir_posts = f"DELETE FROM posts WHERE autor == {id}"
        db.execute(excluir_posts)
        db.commit()
        db.close()
