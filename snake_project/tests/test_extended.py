from game_engine.engine import move_snake_wrap, calculate_speed

def test_move_snake_wrap_left():
    snake = [(0, 2)]
    new_snake = move_snake_wrap(snake, "left", (5, 5))
    assert new_snake[0] == (4, 2)

def test_move_snake_wrap_up():
    snake = [(3, 0)]
    new_snake = move_snake_wrap(snake, "up", (5, 5))
    assert new_snake[0] == (3, 4)

def test_calculate_speed_increase():
    speed = 1.0
    new_speed = calculate_speed(speed)
    assert round(new_speed, 3) == 1.07  # +7%
