const id_post = document.querySelector("#id_postagem")
const excluir = document.querySelector("#excluir")
const formExcluir = document.querySelector("#formExcluir")

id_post.value = localStorage.id

excluir.addEventListener('click', () => {
    localStorage.clear()
    formExcluir.submit()
})