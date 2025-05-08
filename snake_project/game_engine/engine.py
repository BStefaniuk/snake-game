"""
game_engine/engine.py

Silnik gry Snake - logika niezależna od interfejsu graficznego.
Używany do przetwarzania ruchu, kolizji, punktów i parametrów gry.

Układ współrzędnych: kartezjański (0, 0) w lewym dolnym rogu.
Oś X rośnie w prawo, oś Y rośnie w górę.
"""
import random

def init_game_status(board_size = (10,10), start_position = (5,5), lives = 3):
    fruit_x = random.randint(0, board_size[0] - 1)
    fruit_y = random.randint(0, board_size[1] - 1)
    status = {} #pusty słownik do którego dodajemy:

    status["snake_position"] = [start_position]
    status["direction"] = "right"
    status["fruits"] = {(fruit_x, fruit_y): 1}
    status["score"] = 0
    status["speed"] = 1.0
    status["lives"] = lives
    status["game_over"] = False
    status["board_size"] = board_size
    return status

def update_game_status(status, boost=False):
    snake_position = status["snake_position"]
    direction = status["direction"]
    board_size = status["board_size"]

    # oblicz nową głowę
    head_x, head_y = snake_position[0]
    if direction == "up":
        new_head = (head_x, (head_y + 1) % board_size[1])
    elif direction == "down":
        new_head = (head_x, (head_y - 1) % board_size[1])
    elif direction == "left":
        new_head = ((head_x - 1) % board_size[0], head_y)
    elif direction == "right":
        new_head = ((head_x + 1) % board_size[0], head_y)
    else:
        raise ValueError("Invalid direction")

    # sprawdź czy będzie zjedzony owoc
    score_before = status["score"]
    will_grow = new_head in status["fruits"]

    # wykonaj ruch (z rośnięciem lub nie)
    new_snake = move_snake_grow(snake_position, direction, board_size, grow=will_grow)
    status["snake_position"] = new_snake

    # kolizja z samym sobą
    if check_collision(new_snake):
        status["lives"], game_over = update_lives(status["lives"], True)
        if game_over:
            status["game_over"] = True
            return status

    # zbieranie owocu
    status["score"], status["fruits"] = collect_fruit(new_snake[0], status["fruits"], status["score"])
    # Dodanie nowego owocu w losowym miejscu, jeśli zjedzono
    if will_grow:
        while True:
            fruit_x = random.randint(0, board_size[0] - 1)
            fruit_y = random.randint(0, board_size[1] - 1)
            new_fruit_pos = (fruit_x, fruit_y)
            if new_fruit_pos not in status["snake_position"] and new_fruit_pos not in status["fruits"]:
                status["fruits"][new_fruit_pos] = 1
                break

    # zwiększenie prędkości po zdobyciu punktu
    if status["score"] > score_before:
        status["speed"] = increase_speed(status["speed"])

    # przyspieszenie na klawisz
    status["speed"] = handle_speed_boost(status["speed"], boost)

    return status

# Przesuwa węża w zadanym kierunku, układ kartezjański (bez przenikania przez ściany).
def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "up":
        new_head = (head_x, head_y + 1)
    elif direction == "down":
        new_head = (head_x, head_y - 1)
    elif direction == "left":
        new_head = (head_x - 1, head_y)
    elif direction == "right":
        new_head = (head_x + 1, head_y)
    else:
        raise ValueError("Invalid direction")
    
    return [new_head] + snake[:-1]

# sprawdzenie czy głowa koliduje z ciałem
def check_collision(snake):
    head = snake[0]
    return head in snake[1:]

# Oblicza wynik gracza na podstawie długości węża.
def calculate_score(length):
    return length - 1  # zakładamy startowa długość = 1

# Przesuwa węża z uwzględnieniem przenikania przez /ścianykrawędzie planszy (teleportacja)
def move_snake_wrap(snake, direction, board_size):
    head_x, head_y = snake[0]
    if direction == "up":
        new_head = (head_x, (head_y + 1) % board_size[1])
    elif direction == "down":
        new_head = (head_x, (head_y - 1) % board_size[1])
    elif direction == "left":
        new_head = ((head_x - 1) % board_size[0], head_y)
    elif direction == "right":
        new_head = ((head_x + 1) % board_size[0], head_y)
    else:
        raise ValueError("Invalid direction")
    return [new_head] + snake[:-1]

# Ruch z opcją rośnięcia
def move_snake_grow(snake, direction, board_size, grow):
    head_x, head_y = snake[0]
    if direction == "up":
        new_head = (head_x, (head_y + 1) % board_size[1])
    elif direction == "down":
        new_head = (head_x, (head_y - 1) % board_size[1])
    elif direction == "left":
        new_head = ((head_x - 1) % board_size[0], head_y)
    elif direction == "right":
        new_head = ((head_x + 1) % board_size[0], head_y)
    else:
        raise ValueError("Invalid direction")
    
    if grow:
        return [new_head] + snake
    else:
        return [new_head] + snake[:-1]


# Zwiększa prędkość węża o 7% po zjedzeniu owocu.
def increase_speed(current_speed):
    return current_speed * 1.07

# Sprawdza, czy dana pozycja znajduje się w granicach planszy.
def is_within_bounds(position, board_size):
    x, y = position
    width, height = board_size
    return 0 <= x < width and 0 <= y < height

#BONUS - zbieranie punktow za owoce na planszy
def collect_fruit(snake_head, fruits, score):
    if snake_head in fruits:
        score += fruits[snake_head]
        del fruits[snake_head]
    return score, fruits

#PRZYSPIESZENIE - po kliknieciu (tryb przyśpieszenia)
def handle_speed_boost(speed, boost_pressed):
    if boost_pressed:
        return max(speed * 0.8, 0.2)  # nie szybciej niż 0.2
    return speed

#PUNKTY ZYCIA - zmniejszanie żyć (aktualizacja żyć i powiedzenie czy gra się skończyła)
def update_lives(lives, collided):
    if collided:
        lives -= 1
        if lives <= 0:
            return 0, True  #nowe życia, czy gra się skończyła
    return lives, False 