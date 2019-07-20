header = document.querySelector("h1");

header.style.color = "red";

function getRandomColor() {
    letters = "0123456789ABCDEF";
    color = "#";
    for(i=0;i<6;i++){
        color += letters[Math.floor(Math.random()*16)];
    }
    return color;
}

function changeHeaderColor() {
    colorInput = getRandomColor();
    header.style.color = colorInput;
}

setInterval("changeHeaderColor()",500);
