import pytest
pytestmark = pytest.mark.skip(reason="Pominieto testy zalezne od MongoDB w CI")

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
    add_game("user1", "2025-04-14", 50.0, 100)
    games_for_user = get_user_games("user1")

    assert any(game["score"] == 100 for game in games_for_user)

#Read

def test_get_user():
    add_user("toread", score=10)
    user = get_user("toread")

    assert user is not None
    assert user["nick"] == "toread"

def test_get_user_games():
    add_user("user1", score = 0)
    add_game("user1", "2025-04-16", 30, 100)
    result = get_user_games("user1")

    assert isinstance(result, list)
    assert len(result) > 0

def test_get_users_list():
    add_user("user1")
    add_user("user2")
    result = get_users_list()

    assert isinstance(result, list)
    assert any(user["nick"] == "user1" for user in result)

def test_get_games_list():
    add_game("user1", "2025-04-16", 10, 100)
    result = get_games_list()

    assert isinstance(result, list)
    assert any(user["nick"] == "user1" for user in result)

def test_get_top_score():
    add_game("top_player", "2025-04-16", 10, 100)
    top = get_top_score()

    assert top is not None
    assert "score" in top


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
    add_game("todelete", "2025-04-16", 20, 100)
    delete_user("todelete")

    assert get_user("todelete") is None

def test_delete_all_users():
    add_user("todelete1")
    add_user("todelete2")
    delete_all_users()
    all_users = list(users.find())

    assert len(all_users) == 0

def test_delete_all_games():
    add_game("deletegame", "2025-04-16", 10, 20)
    delete_all_games()
    all_games = list(games.find())

    assert len(all_games) == 0