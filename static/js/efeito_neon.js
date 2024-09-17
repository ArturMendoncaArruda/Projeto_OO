document.querySelector('.navbar').addEventListener('mousemove', (e) => {
    const highlight = document.querySelector('.highlight');
    const navbar = document.querySelector('.navbar');
    const rect = navbar.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // Calcular a cor com base na posição do mouse
    const r = Math.min(200, Math.max(0, Math.floor(x / rect.width * 200)));
    const g = Math.min(200, Math.max(0, Math.floor(y / rect.height * 200)));
    const b = Math.min(200, Math.max(0, 255 - Math.floor((x + y) / (rect.width + rect.height) * 200)));

    // Aplicar o efeito de mudança de cor no destaque
    highlight.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

    // Aplicar o efeito neon aos links
    const neonEffect = document.querySelectorAll('.navbar a');
    neonEffect.forEach(link => {
        link.style.textShadow = `
            ${x / 10}px ${y / 10}px 10px #ff00cc,
            ${-x / 20}px ${-y / 20}px 20px #00ffcc
        `;
    });
});
