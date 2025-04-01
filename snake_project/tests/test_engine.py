from game_engine.engine import move_snake, check_collision, calculate_score
from game_engine.engine import is_within_bounds

def test_move_snake_up():
    snake = [(5, 5), (5, 6)]
    new_snake = move_snake(snake, "up")
    assert new_snake[0] == (5, 4)

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

