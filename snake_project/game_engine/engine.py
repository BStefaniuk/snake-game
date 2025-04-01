def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == "up":
        new_head = (head_x, head_y - 1)
    elif direction == "down":
        new_head = (head_x, head_y + 1)
    elif direction == "left":
        new_head = (head_x - 1, head_y)
    elif direction == "right":
        new_head = (head_x + 1, head_y)
    else:
        raise ValueError("Invalid direction")
    
    return [new_head] + snake[:-1]

def check_collision(snake):
    head = snake[0]
    return head in snake[1:]

def calculate_score(length):
    return length - 1  # zakładamy startowy długość = 1

def move_snake_wrap(snake, direction, board_size):
    head_x, head_y = snake[0]
    if direction == "up":
        new_head = (head_x, (head_y - 1) % board_size[1])
    elif direction == "down":
        new_head = (head_x, (head_y + 1) % board_size[1])
    elif direction == "left":
        new_head = ((head_x - 1) % board_size[0], head_y)
    elif direction == "right":
        new_head = ((head_x + 1) % board_size[0], head_y)
    else:
        raise ValueError("Invalid direction")
    return [new_head] + snake[:-1]

def calculate_speed(current_speed):
    return current_speed * 1.07

def is_within_bounds(position, board_size):
    x, y = position
    width, height = board_size
    return 0 <= x < width and 0 <= y < height
