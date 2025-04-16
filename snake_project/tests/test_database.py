from snake_project.database.db import get_db
from snake_project.database.models import users
from snake_project.database.models import games
from snake_project.database.models import (
    add_game, add_user, update_user_data, delete_user, 
    get_user, get_user_games, get_users_list, get_games_list, 
    get_top_score, delete_all_users, delete_all_games
    )

def test_connection():
    db = get_db()
    print("test polaczenia")
    
    assert db is not None

#Create

def test_add_user():
    add_user("user1", score=50, map_size="20x20")
    found_user = get_user("user1")

    assert found_user is not None
    assert found_user["score"] == 50
    assert found_user["map_size"] == "20x20"

def test_add_game():
    add_game("user1", "2025-04-14", 60.5, 200)
    games_for_user = get_user_games("user1")

    assert any(game["score"] == 200 for game in games_for_user)

#Read

def test_get_user():
    add_user("toread", score=10)
    user = get_user("toread")

    assert user is not None
    assert user["nick"] == "toread"

def test_get_user_games():
    add_user("gamer", score = 0)
    add_game("gamer", "2025-04-16", 30, 100)
    result = get_user_games("gamer")

    assert isinstance(result, list)
    assert len(result) > 0

def test_get_users_list():
    add_user("u1")
    add_user("u2")
    result = get_users_list()

    assert isinstance(result, list)
    assert any(user["nick"] == "u1" for user in result)

#Update
def test_update_user_data():
    add_user("toupdate", score=15)
    update_user_data("toupdate", score=100, map_size="15x15")
    updated_user = get_user("toupdate")

    assert updated_user["score"] == 100
    assert updated_user["map_size"] == "15x15"

#Delete
def test_delete_user():
    add_user("todelete", score=25)
    delete_user("todelete")
    deleted_user = get_user("todelete")

    assert deleted_user is None