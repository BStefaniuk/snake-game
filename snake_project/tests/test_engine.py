
#TESTY JEDNOSTKOWE

from game_engine.engine import move_snake, check_collision, calculate_score
from game_engine.engine import is_within_bounds
from game_engine.engine import init_game_status

def test_init_game_status_structure():
    #nowy stan gry z plansza plansza 8x8
    status = init_game_status(8,8)

    #sprawdzanie czy zwrócony słownik zawiera wymagane klucze i czy typy danych sa poprawne
    assert "snake_position" in status
    assert "fruits" in status
    assert "score" in status
    assert "game_over" in status
    assert isinstance(status["snake_position"], list)
    assert isinstance(status["fruits"], dict)


def test_move_snake_up():
    snake = [(5, 5), (5, 4)]
    new_snake = move_snake(snake, "up")
    assert new_snake[0] == (5, 6)

def test_collision_with_self():
    snake = [(5, 5), (5, 6), (5, 5)]  # Głowa trafia na ciało węża
    assert check_collision(snake) is True

def test_calculate_score():
    length = 5
    assert calculate_score(length) == 4  # 1 to długość początkowa

def test_position_within_bounds():
    position = (3, 4)
    board_size = (5, 5)
    assert is_within_bounds(position, board_size) is True

def test_position_out_of_bounds_x():
    position = (5, 2)  # poza prawą krawędzią (x >= width)
    board_size = (5, 5)
    assert is_within_bounds(position, board_size) is False

def test_position_out_of_bounds_y():
    position = (2, 5)  # poza dolną krawędzią (y >= height)
    board_size = (5, 5)
    assert is_within_bounds(position, board_size) is False

def test_position_negative_coordinates():
    position = (-1, 0)  # ujemne współrzędne
    board_size = (5, 5)
    assert is_within_bounds(position, board_size) is False

#BONUS - zbieranie punktow za owoce na planszy

def test_collect_fruit_with_bonus():
    snake_head = (4, 4)
    fruits = {(4, 4): 5, (2, 2): 3}
    score = 10

    new_score, new_fruits = collect_fruit(snake_head, fruits, score)

    assert new_score == 15
    assert (4, 4) not in new_fruits

def test_collect_fruit_no_fruit():
    snake_head = (1, 1)
    fruits = {(4, 4): 5}
    score = 10

    new_score, new_fruits = collect_fruit(snake_head, fruits, score)

    assert new_score == 10
    assert new_fruits == fruits


#PRZYSPIESZENIE

def test_speed_boost_activated():
    speed = 1.0
    boost_pressed = True

    new_speed = handle_speed_boost(speed, boost_pressed)

    assert new_speed < speed

def test_speed_boost_not_activated():
    speed = 1.0
    boost_pressed = False

    new_speed = handle_speed_boost(speed, boost_pressed)

    assert new_speed == speed


#PUNKTY ZYCIA

def test_life_lost_on_collision():
    lives = 3
    collided = True

    new_lives, game_over = update_lives(lives, collided)

    assert new_lives == 2
    assert game_over is False

def test_game_over_when_no_lives_left():
    lives = 1
    collided = True

    new_lives, game_over = update_lives(lives, collided)

    assert new_lives == 0
    assert game_over is True

def test_lives_stay_same_without_collision():
    lives = 3
    collided = False

    new_lives, game_over = update_lives(lives, collided)

    assert new_lives == 3
    assert game_over is False


