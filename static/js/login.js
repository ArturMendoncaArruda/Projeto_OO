document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const username = document.getElementById('id_username');
    const password = document.getElementById('id_password');
    const togglePassword = document.getElementById('togglePassword');
    const messageDiv = document.getElementById('login-message');



    // Mostrar/Ocultar Senha
    if (togglePassword) {
        togglePassword.addEventListener('click', function() {
            const type = password.type === 'password' ? 'text' : 'password';
            password.type = type;
            // Atualiza o ícone do botão
            this.innerHTML = type === 'password' ? '<i class="bx bx-show-alt"></i>' : '<i class="bx bx-low-vision"></i>';
        });
    }


 
});
