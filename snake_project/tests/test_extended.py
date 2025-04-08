from game_engine.engine import move_snake_wrap, increase_speed

def test_move_snake_wrap_left():
    snake = [(0, 2)] #krawedz lewa
    new_snake = move_snake_wrap(snake, "left", (5, 5))
    assert new_snake[0] == (4, 2) #pojawia sie po prawej

def test_move_snake_wrap_right():
    snake = [(4,3)] #krawedz prawa
    new_snake = move_snake_wrap(snake, "right", (5,5))
    assert new_snake[0] == (0,3) #pojawia sie po lewej

def test_move_snake_wrap_up():
    snake = [(3,4)] #krawedz gorna
    new_snake = move_snake_wrap(snake, "up", (5, 5))
    assert new_snake[0] == (3, 0) #pojawia sie na dole

def test_move_snake_wrap_down():
    snake = [(2,0)] #krawedz dolna
    new_snake = move_snake_wrap(snake, "down", (5,5))
    assert new_snake[0] == (2,4) #pojawia sie na gorze

def test_calculate_speed_increase():
    speed = 1.0
    new_speed = increase_speed(speed)
    assert round(new_speed, 3) == 1.07  # +7% speedu
