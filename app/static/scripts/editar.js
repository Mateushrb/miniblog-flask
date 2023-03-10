const id_post = document.querySelector("#id_postagem")
const titulo = document.querySelector("#titulo")
const texto = document.querySelector("#texto")
const atualizar = document.querySelector("#atualizar")
const formEditar = document.querySelector("#formEditar")

id_post.value = localStorage.id
titulo.value = localStorage.titulo
texto.value = localStorage.texto

atualizar.addEventListener('click', () => {
    localStorage.clear()
    formEditar.submit()
})