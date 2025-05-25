import pytest
import os

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

# Create

def test_add_user():
    delete_user("test_user1")
    add_user("test_user1", score=50, map_size="20x20")
    found_user = get_user("test_user1")
    assert found_user is not None
    assert found_user["score"] == 50
    assert found_user["map_size"] == "20x20"

def test_add_game():
    delete_user("test_user1")
    add_user("test_user1")
    add_game("test_user1", "2025-04-14", 50.0, 100)
    games_for_user = get_user_games("test_user1")
    assert any(game["score"] == 100 for game in games_for_user)

# Read

def test_get_user():
    delete_user("test_read")
    add_user("test_read", score=10)
    user = get_user("test_read")
    assert user is not None
    assert user["nick"] == "test_read"
    assert user["score"] == 10

def test_get_user_games():
    delete_user("test_games")
    add_user("test_games")
    add_game("test_games", "2025-04-16", 30, 100)
    result = get_user_games("test_games")
    assert isinstance(result, list)
    assert len(result) > 0

def test_get_users_list():
    delete_user("test_user2")
    delete_user("test_user3")
    add_user("test_user2")
    add_user("test_user3")
    result = get_users_list()
    assert isinstance(result, list)
    assert any(user["nick"] == "test_user2" for user in result)
    assert any(user["nick"] == "test_user3" for user in result)

def test_get_games_list():
    delete_user("test_gamelist")
    add_user("test_gamelist")
    add_game("test_gamelist", "2025-04-16", 10, 100)
    result = get_games_list()
    assert isinstance(result, list)
    assert any(game["nick"] == "test_gamelist" for game in result)

def test_get_top_score():
    delete_user("test_top")
    add_user("test_top")
    add_game("test_top", "2025-04-16", 10, 100)
    top = get_top_score()
    assert top is not None
    assert "score" in top

# Update

def test_update_user_data():
    delete_user("test_update")
    add_user("test_update", score=15)
    update_user_data("test_update", score=100, map_size="15x15")
    updated_user = get_user("test_update")
    assert updated_user["score"] == 100
    assert updated_user["map_size"] == "15x15"

# Delete

def test_delete_user():
    delete_user("test_delete")
    add_user("test_delete", score=25)
    add_game("test_delete", "2025-04-16", 20, 100)
    delete_user("test_delete")
    assert get_user("test_delete") is None
    assert len(get_user_games("test_delete")) == 0

def test_delete_all_users():
    add_user("test_bulk1")
    add_user("test_bulk2")
    delete_all_users()
    remaining = list(users.find({"nick": {"$regex": "^test_"}}))
    assert len(remaining) == 0

def test_delete_all_games():
    add_user("test_bulk_games")
    add_game("test_bulk_games", "2025-04-16", 10, 20)
    delete_all_games()
    remaining = list(games.find({"nick": {"$regex": "^test_"}}))
    assert len(remaining) == 0