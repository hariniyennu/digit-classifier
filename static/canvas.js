let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

let drawing = false;

canvas.onmousedown = () => drawing = true;
canvas.onmouseup = () => drawing = false;
canvas.onmousemove = function(event) {
    if (!drawing) return;
    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.arc(event.offsetX, event.offsetY, 10, 0, Math.PI * 2);
    ctx.fill();
};

function clearCanvas() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    document.getElementById("result").innerText = "";
}

function predictDigit() {
    canvas.toBlob(blob => {
        let formData = new FormData();
        formData.append("image", blob, "digit.png");
        fetch("/predict", { method: "POST", body: formData })
            .then(response => response.json())
            .then(data => document.getElementById("result").innerText = "Predicted Digit: " + data.digit);
    });
}

// function downloadCanvasImage() {
//     let canvas = document.getElementById("canvas");
//     let link = document.createElement("a");
//     link.download = "canvas_image.png";
//     link.href = canvas.toDataURL("image/png");
//     link.click();
// }
