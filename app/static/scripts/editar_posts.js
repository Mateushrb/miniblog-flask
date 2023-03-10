const postagem = document.querySelector("#postagens")

postagem.addEventListener('click', (e) => {
    if (e.target.id === 'btnEditar') {
        localStorage.id = e.path[4].childNodes[3].childNodes[3].childNodes[1].innerHTML
        localStorage.titulo = e.path[2].childNodes[1].innerHTML
        localStorage.texto = e.path[3].childNodes[3].innerHTML
        location.href = '/editar'
    }
    if (e.target.id === 'btnExcluir') {
        localStorage.id = e.path[4].childNodes[3].childNodes[3].childNodes[1].innerHTML
        location.href = '/excluir'
    }
})

