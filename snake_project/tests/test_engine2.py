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
