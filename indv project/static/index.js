document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    let drawing = false;

    canvas.addEventListener('mousedown', function (event) {
        drawing = true;
        context.beginPath();
        context.moveTo(event.offsetX, event.offsetY);
    });

    canvas.addEventListener('mousemove', function (event) {
        if (drawing) {
            context.lineTo(event.offsetX, event.offsetY);
            context.stroke();
        }
    });

    canvas.addEventListener('mouseup', function () {
        drawing = false;
    });

    canvas.addEventListener('mouseleave', function () {
        drawing = false;
    });

    document.getElementById('memeForm').addEventListener('submit', function (event) {
        const memeData = canvas.toDataURL('image/png');
        document.getElementById('memeData').value = memeData;
    });
});
