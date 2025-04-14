from snake_project.database.db import get_db
from snake_project.database.models import users

def test_connection():
    db = get_db()
    print("test polaczenia")
    
    assert db is not None

def test_add_user():
    users.insert_one({"nickname":"test_user","score":10})
    found = users.find_one({"nickname":"test_user"})

    assert found is not None
    assert found["score"] == 10