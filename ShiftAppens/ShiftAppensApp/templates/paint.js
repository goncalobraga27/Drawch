window.onload = function() {
    // Obtenha o elemento canvas
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');

    // Defina o tamanho do canvas
    canvas.width = 600;
    canvas.height = 400;

    // Variáveis para armazenar o estado do desenho
    var painting = false;
    var lastX = 0;
    var lastY = 0;

    // Função para desenhar na tela
    function draw(e) {
        if (!painting) return;
        context.lineWidth = 5; // Defina a largura da linha
        context.lineCap = 'round'; // Defina o estilo da ponta da linha
        context.strokeStyle = '#000'; // Defina a cor da linha
        context.beginPath();
        context.moveTo(lastX, lastY); // Mova o cursor para a posição anterior
        context.lineTo(e.offsetX, e.offsetY); // Desenhe uma linha até a nova posição
        context.stroke();
        lastX = e.offsetX;
        lastY = e.offsetY;
    }

    // Evento de pressionar o botão do mouse
    canvas.addEventListener('mousedown', function(e) {
        painting = true;
        lastX = e.offsetX;
        lastY = e.offsetY;
        draw(e);
    });

    // Evento de soltar o botão do mouse
    canvas.addEventListener('mouseup', function() {
        painting = false;
    });

    // Evento de mover o mouse
    canvas.addEventListener('mousemove', draw);

    // Limpar o canvas
    document.getElementById('clear').addEventListener('click', function() {
        context.clearRect(0, 0, canvas.width, canvas.height);
    });
};
