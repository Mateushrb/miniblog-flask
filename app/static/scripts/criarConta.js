const formCriaConta = document.querySelector("#formCriaConta");
const login = document.querySelector("#login");
const senha = document.querySelector("#password");
const passConf = document.querySelector("#passConf");
const token = document.querySelector("#token");
const btnCriar = document.querySelector("#btnCriar");

function principal() {
    if (login.value.length == 0) {
        alert("O campo de usuário não pode ficar em branco.");
    } else if (senha.value.length == 0) {
        alert("Você precisa digitar uma senha.");
    } else if (passConf.value.length == 0) {
        alert("Confirme sua senha para proseguir.");
    } else if (senha.value != passConf.value) {
        alert("As senhas não são iguais.");
    } else if (token.value.length == 0) {
        alert("Não tem um token? Peça um ao administrador do sistema.");
    } else {
        formCriaConta.submit();
    }
}

token.addEventListener("keydown", (e) => {
    if (e.keyCode == 13) {
        principal();
        e.preventDefault;
    }
})

btnCriar.addEventListener('click', () => {
    principal();
})

