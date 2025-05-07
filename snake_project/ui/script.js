const board = document.getElementById("board");
const statusText = document.getElementById("status");
const boardSize = 10;

//tworzenie planszy 
function drawEmptyBoard(){
    board.innerHTML = "";
    for (let i = 0; i < boardSize * boardSize; i++){
        const cell = document.createElement("div");
        cell.className = "cell";
        board.appendChild(cell);
    }
}

function getCellIndex(x, y){
    return y * boardSize + x;
}

//rysowanie weza i owocow
function drawGameState(state){
    drawEmptyBoard();
    const cell = document.getElementsByClassName("cell");

    state.snake_position.forEach(([x, y]) => {
        const index = getCellIndex(x, y);
        cells[index].classList.add("snake");
    });

    state.fruits.forEach(fruit => {
        const index = getCellIndex(fruit.x, fruit.y);
        cells[index].classList.add("fruit");
    });

    if(state.game_over){
        statusText.textContent = "GAME OVER";
    }else{
        statusText.textContent = `Score: ${state.score}`;
    }
}

//pobieranie stanu z backendu
async function fetchGameState(){
    const res = await fetch("http://127.0.0.1:5000/api/game/state");
    const data = await res.json();
    drawGameState(data);
}

//wysylanie kierunku do backendu
async function sendMove(direction){
    const res = await fetch("http://127.0.0.1:5000/api/game/move",{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({direction})
    });
    const data = await res.json();
    drawGameState(data);
}

//obsluga klawiszy
document.addEventListener("keydown", (e) => {
    const keyMap = {
        ArrowUp: "up",
        ArrowDown: "down",
        ArrowLeft: "left",
        ArrowRight: "right",
        w: "up",
        s: "down",
        a: "left",
        d: "right"
    };

    const direction = keyMap[e.key];
    if(direction){
        sendMove(direction);
    }
});

//start gry
fetchGameState();