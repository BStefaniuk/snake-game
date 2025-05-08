const board = document.getElementById("board");
const statusText = document.getElementById("status");
const boardSize = 10;
let moveInterval = null;
let direction = "right";


//tworzenie planszy 
function drawEmptyBoard(){
    board.innerHTML = "";
    for (let i = 0; i < boardSize * boardSize; i++){
        const cell = document.createElement("div");
        cell.className = "cell";
        board.appendChild(cell);
    }
}

function getCellIndex(x, y) {
    return (boardSize - 1 - y) * boardSize + x;
}

//rysowanie weza i owocow
function drawGameState(state){
    drawEmptyBoard();
    const cells = document.getElementsByClassName("cell");

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
    currentState = data;
    direction = data.direction;
    drawGameState(data);

    moveInterval = setInterval(sendMove, 1000 / data.speed);
}

//wysylanie kierunku do backendu
let currentState = null; // przechowujemy ostatni stan gry

async function sendMove(){
    if (currentState?.game_over) return;

    const res = await fetch("http://127.0.0.1:5000/api/game/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ direction })
    });
    const data = await res.json();
    currentState = data;
    drawGameState(data);

    if (data.game_over) {
        clearInterval(moveInterval); // zatrzymane ruchu
    } else {
        //nowy interwal z ustawieniem predkosci
        clearInterval(moveInterval);
        moveInterval = setInterval(sendMove, 1000 / data.speed);
    }
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
    const newDir = keyMap[e.key]; // klawisz na kierunek 'ArrowUp' -> 'up'
    if (newDir && currentState) {
        //przeciwny kierunek
        const opposite = {
            up: "down",
            down: "up",
            left: "right",
            right: "left"
        };

        //jak nowy kierunek nie jest przeciwny
        if (newDir !== opposite[currentState.direction]) {
            direction = newDir;
        }
    }
});
//start gry
fetchGameState();