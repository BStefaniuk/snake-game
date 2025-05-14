from flask import Flask         #tworzy server
from flask import jsonify       #zamienia na json
from flask import request           #do odczytywania danych
from flask_cors import CORS         #laczenie z backend
from snake_project.game_engine.engine import init_game_status
from snake_project.game_engine.engine import update_game_status
from snake_project.database.models import add_user

app = Flask(__name__)
CORS(app)

#inicjalizacja gry
game_status = init_game_status(
    board_size = (10,10), 
    start_position = (5,5), 
    lives = 1
)
#Klucz JSONa może być tylko tekstem
#konwersja z tuple do JSON
def convert_status_to_json_safe(status):
    # konwertujemy (2, 3): 1 → {"x": 2, "y": 3, "value": 1}
    fruits_json = []
    for (x, y), value in status["fruits"].items():
        fruits_json.append({"x": x, "y": y, "value": value})
    safe_status = dict(status)       # kopia stanu gry
    safe_status["fruits"] = fruits_json     # zamieniamy fruits na listę słowników
    return safe_status

#adresy api
#GET - pobierz plansze
@app.route("/api/game/state", methods = ["GET"])
def get_state():
    return jsonify(convert_status_to_json_safe(game_status))

#POST - wykonaj ruch i zwraca nowy stan planszy
@app.route("/api/game/move", methods = ["POST"])
def move():
    global game_status
    data = request.get_json()
    new_direction = data.get("direction")
    if new_direction:
        current = game_status["direction"]
        opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new_direction != opposite.get(current):
            game_status["direction"] = new_direction

        game_status = update_game_status(game_status)

    return jsonify(convert_status_to_json_safe(game_status))

#POST - start gry z nickiem i rozmiarem planszy 
@app.route("/api/game/init", methods = ["POST"])
def init_game():
    global game_status          #modyfikacja zmiennej spoza funkcji
    data = request.get_json()   #odczytane dane z frontendu
    nick = data.get("nick", "guest")    #domyslne
    size = int(data.get("size", 10))    #domyslne
    #nowy stan gry
    game_status = init_game_status(
        board_size = (size, size),
        start_position = (size // 2, size // 2),    #srodek planszy
        lives = 1
    )
    #zapis danych do bazy
    add_user(nick = nick, map_size = f"{size} x {size}")
    return jsonify(convert_status_to_json_safe(game_status))

if __name__ == "__main__":
    app.run(debug = True)