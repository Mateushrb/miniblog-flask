from flask import render_template, request, flash
from app import app
from app.crud import crud
from app.models import Postagem, User, Autor
from app.form import LoginForm
from urllib.parse import urlparse, urljoin

from flask_login import LoginManager, login_user, logout_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    name = crud.autor(id)
    login = crud.user(id)
    idade = crud.idade(id)
    bairro = crud.bairro(id)
    biografia = crud.biografia(id)
    password = crud.pass_user(login)
    user = User(id, name, idade, bairro, biografia, login, password)
    return user

@app.route("/")
@app.route("/index")
def index():
    postagens = []
    posts = crud.postagens()
    for p in posts:
        autor = crud.autor(p[4])
        post = Postagem(p[0], p[1], p[2], p[3], autor, str(p[4]))
        postagens.append(post)
    postagens.reverse()
    return render_template("index.html", postagens=postagens)

@app.route("/autores")
def autores():
    autores = []
    autors = crud.autores()
    for a in autors:
        autor = Autor(a[1], a[2], a[3], a[4])
        autores.append(autor)
    return render_template("/autores.html", autores=autores)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method=='POST':
        if request.form.get("login") in crud.logins():
            user_name = request.form.get("login")
            id = crud.id_user(user_name)
            name = crud.autor(id)
            idade = crud.idade(id)
            bairro = crud.bairro(id)
            biografia = crud.biografia(id)
            senha = crud.pass_user(user_name)
            user = User(id, name, idade, bairro, biografia, user_name, senha)
            if user and user.password == request.form.get("senha"):
                # Login and validate the user.
                # user should be an instance of your `User` class
                login_user(user)

            else:
                flash("Invalid login.")
                return render_template("login.html")
        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        def is_safe_url(target):
                    ref_url = urlparse(request.host_url)
                    test_url = urlparse(urljoin(request.host_url, target))
                    return test_url.scheme in ('http', 'https') and \
                        ref_url.netloc == test_url.netloc
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return app.abort(400)


        return app.redirect('/')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return app.redirect("/")

@app.route("/criar_conta", methods=['GET', 'POST'])
def criar_conta():
    if current_user.is_authenticated:
        return app.redirect("/conta")
    else:
        if request.method=='GET':
            return render_template("criar_conta.html")
        if request.method=='POST':
            login = request.form.get('user')
            senha = request.form.get('pass')
            token = request.form.get('token')

            logins = crud.logins()
            if login in logins:
                flash("Esse usuário já existe, crie outro.")
                return app.redirect("/criar_conta")
            else:
                if token == '2482':
                    crud.cadastrar_usuario(login, senha)
                    id = crud.id_user(login)
                    crud.completar_cadastro(id, 'Nome', 0, 'Bairro', 'Biografia')
                    flash("Usuário criado com sucesso! Faça login e complete seu cadastro!")
                    return app.redirect("/login")
                else:
                    flash("Token inválido")
                    return app.redirect("/criar_conta")
        
@app.route("/postar", methods=['GET', 'POST'])
def postar():
    if request.method == 'POST':
        titulo = request.form.get("titulo")
        texto = request.form.get("texto")
        crud.postar(titulo, texto, current_user.user_id)
        flash("Postagem realizada com sucesso!")
        return app.redirect("/")
    if current_user.is_authenticated:
        return render_template("/postagem.html")
    else:
        flash("Você precisa logar para poder postar.")
        return app.redirect("/login")
    
@app.route("/conta", methods=['GET', 'POST'])
def conta():
    if request.method == 'POST':
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        bairro = request.form.get("bairro")
        biografia = request.form.get("biografia")
        crud.completar_cadastro(current_user.user_id, nome, idade, bairro, biografia)
        flash("Cadastro atualizado com sucesso!")
        return app.redirect("/conta")
    if current_user.is_authenticated:
        return render_template("conta.html")
    else:
        flash("Você precisa logar para atualizar os dados da conta.")
        return app.redirect("/login")
    
@app.route("/editar", methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        id = request.form.get("id_postagem")
        titulo = request.form.get("titulo")
        texto = request.form.get("texto")
        if int(current_user.user_id) == crud.id_autor_post(id):
            crud.atualizar_post(id, titulo, texto)
            flash("Post atualizado com sucesso!")
            return app.redirect("/")
        else:
            flash("Você só pode alterar posts de sua autoria!")
    if current_user.is_authenticated:
            return render_template("editar.html")
    else:
        flash("Você precisa logar para editar as postagens.")
        return app.redirect("/login")

@app.route("/excluir", methods=['GET', 'POST'])
def excluir():
    if request.method == 'POST':
        id = request.form.get("id_postagem")
        if int(current_user.user_id) == crud.id_autor_post(id):
            crud.excluir_post(id)
            flash("Post excluído com sucesso!")
            return app.redirect("/")
        else:
            flash("Você só pode excluir posts de sua autoria!")
    if current_user.is_authenticated:
        return render_template("excluir.html")
    else:
        flash("Você precisa logar para excluir postagens.")
        return app.redirect("/login")