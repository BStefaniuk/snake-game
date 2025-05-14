const board = document.getElementById("board");
const statusText = document.getElementById("status");
const timerText = document.getElementById("timer");
const gameTitle = document.getElementById("game-title");

let boardSize = 10;
let moveInterval = null;
let direction = "right";
let currentState = null; // przechowujemy ostatni stan gry
let isPaused = false;
let pausedTime = 0;
let pauseStartedAt = null;


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
        cells[index]?.classList.add("snake");
    });

    state.fruits.forEach(fruit => {
        const index = getCellIndex(fruit.x, fruit.y);
        cells[index]?.classList.add("fruit");
    });

    if(state.game_over){
        statusText.textContent = "GAME OVER";
        stopGameTimer();
    }else{
        statusText.textContent = `Score: ${state.score}`;
    }
}

function startGameTimer() {
    gameStartTime = Date.now();
    timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
    const now = Date.now();
    const elapsed = Math.floor((now - gameStartTime - pausedTime) / 1000);
    timerText.textContent = `Czas gry: ${elapsed}s`;
}

function stopGameTimer(){
    clearInterval(timerInterval);
}

function pauseGame() {
    isPaused = true;
    pauseStartedAt = Date.now();
    clearInterval(moveInterval);
    clearInterval(timerInterval);
}

function resumeGame() {
    isPaused = false;
    pausedTime += Date.now() - pauseStartedAt;
    timerInterval = setInterval(updateTimer, 1000);
    moveInterval = setInterval(sendMove, 1000 / currentState.speed);
}

//pobieranie stanu z backendu
async function fetchGameState(){
    const res = await fetch("http://127.0.0.1:5000/api/game/state");
    const data = await res.json();
    currentState = data;
    boardSize = data.board_size[0];
    board.style.gridTemplateColumns = `repeat(${boardSize}, 30px)`;
    board.style.gridTemplateRows = `repeat(${boardSize}, 30px)`;
    direction = data.direction;

    drawGameState(data);
    drawEmptyBoard();

    gameTitle.style.display = "block";
    board.style.display = "grid";
    statusText.style.display = "block";
    timerText.style.display = "block";

    startGameTimer();
    moveInterval = setInterval(sendMove, 1000 / data.speed);
}

//wysylanie kierunku do backendu

async function sendMove(){
    if (isPaused || currentState?.game_over) return;

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

    if(e.key === "p" || e.key === "P"){
        if (!currentState?.game_over) {
            if (isPaused) resumeGame();
            else pauseGame();
        }
        return;
    }

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

document.getElementById("start-button").addEventListener("click", async () => {
    const nick = document.getElementById("nickname").value.trim();
    const size = parseInt(document.getElementById("board-size").value);

    if( !nick || isNaN(size) || size < 5 || size > 25){
        alert("Podaj nick i rozmiar planszy z zakresu 5-25");
        return;
    }

    const res = await fetch("http://127.0.0.1:5000/api/game/init", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ nick: nick, size: size})
    });

    const data = await res.json();
    currentState = data;
    direction = data.direction;

    document.getElementById("start-screen").style.display = "none";
    fetchGameState();
});