document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');
    const messageDiv = document.getElementById('login-message');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Previne o comportamento padrão de envio do formulário

        const usuarioNome = document.getElementById('usuario_nome').value;
        const usuarioSenha = document.getElementById('usuario_senha').value;

        fetch('http://127.0.0.1:8000/login/', { // URL da API de login
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({
                usuario_nome: usuarioNome,
                usuario_senha: usuarioSenha
            })
        })
        .then(response => response.json().then(data => ({status: response.status, body: data}))) // Corrigido aqui
        .then(({status, body}) => {  // Aqui você pode acessar status e body
            if (status === 200) {
                messageDiv.innerHTML = `<div class="alert alert-success">${body.message}</div>`;
                // Redireciona para a página de estatísticas
                window.location.href = '/stats-page/';
            } else {
                messageDiv.innerHTML = `<div class="alert alert-danger">${body.message}</div>`;
            }
        })
        .catch(error => {
            messageDiv.innerHTML = `<div class="alert alert-danger">Erro: ${error.message}</div>`;
        });
    });
});
