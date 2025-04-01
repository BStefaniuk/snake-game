#BONUS - zbieranie punktow za owoce na planszy

def collect_fruit(snake_head, fruits, score):
    if snake_head in fruits:
        score += fruits[snake_head]
        del fruits[snake_head]
    return score, fruits



#PRZYSPIESZENIE

def handle_speed_boost(speed, boost_pressed):
    if boost_pressed:
        return max(speed * 0.8, 0.2)  # nie szybciej niż 0.2
    return speed



#PUNKTY ZYCIA

def update_lives(lives, collided):
    if collided:
        lives -= 1
        if lives <= 0:
            return 0, True
    return lives, False
