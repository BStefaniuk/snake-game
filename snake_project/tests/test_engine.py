from game_engine.engine import move_snake, check_collision, calculate_score

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
