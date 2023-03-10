let passBoolean = 0
const showPassword = document.querySelector("#mostrarSenha");
const password = document.querySelector("#senha");
const logar = document.querySelector("#logar");

const entrar = document.querySelector("#entrar");
entrar.innerHTML = '';

const inputLogin = document.querySelector("#login");
const inputSenha = document.querySelector("#senha");
const btnEntrar = document.querySelector("#btnEntrar");

const login = document.querySelector("#login");
const senha = document.querySelector("#senha");

showPassword.addEventListener('click', () => {
    if (passBoolean == 0) {
        showPassword.value = "Ocultar senha";
        password.type = "text";
        passBoolean = 1;
    } else {
        showPassword.value = "Mostrar senha";
        password.type = "password";
        passBoolean = 0;
    }
})

function principal() {
    if (login.value.length == 0) {
        alert("O campo de login não pode ficar em branco.");
    } else if (senha.value.length == 0) {
        alert("O campo da senha não pode ficar em branco.");
    } else {
        logar.submit();
    }
}

btnEntrar.addEventListener('click', () => {
    principal();
})

senha.addEventListener("keydown", (e) => {
    if (e.keyCode == 13) {
        principal();
        e.preventDefault;
    }
})