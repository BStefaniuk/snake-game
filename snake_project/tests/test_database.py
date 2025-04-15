from snake_project.database.db import get_db
from snake_project.database.models import users
from snake_project.database.models import (add_game, add_user, update_user_data, delete_user, get_user, get_user_games, get_users_list, get_games_list, get_top_score, delete_all_users, delete_all_games)

def test_connection():
    db = get_db()
    print("test polaczenia")
    
    assert db is not None

#Create

def test_add_user():
    add_user("test_user", score=50, map_size="20x20")
    found_user = get_user("test_user")

    assert found_user is not None
    assert found_user["score"] == 50
    assert found_user["map_size"] == "20x20"

#Read

def test_get_user():
    add_user("toread", score=10)
    user = get_user("toread")

    assert user is not None
    assert user["nick"] == "toread"

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