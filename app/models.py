class Autor():
    def __init__(self, nome, idade, bairro, biografia):
        self.nome = nome
        self.idade = idade
        self.bairro = bairro
        self.biografia = biografia

class Postagem():
    def __init__(self, id, titulo, texto, data, autor, autor_id):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.data = data
        self.autor = autor
        self.autor_id = autor_id

class User():
    user_id = 0
    def __init__(self, user_id, name, idade, bairro, biografia, login, password):
        self.user_id = user_id
        self.name = name
        self.idade = idade
        self.bairro = bairro
        self.biografia = biografia
        self.login = login
        self.password = password
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.user_id)