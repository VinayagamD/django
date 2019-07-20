//Restart Game Button
restart = document.querySelector("#b");
// Grab all squares
let squares = document.querySelectorAll("td");

// Clear all squares
function clearBoard() {
    for (let i = 0; i < squares.length; i++) {
        squares[i].textContent="";
    }
}

restart.addEventListener("click",clearBoard);
// Check the square marker
function changeMarker(){
    switch (this.textContent) {
        case "":
            this.textContent = "X";
            break;
        case "X":
            this.textContent = "O";
            break;
        default:
            this.textContent ="";
    }
}

for(let i =0 ; i< squares.length; i++){
    squares[i].addEventListener("click",changeMarker);
}

// For loop to add event listener to all squares
