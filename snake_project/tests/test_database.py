from snake_project.database.db import get_db
from snake_project.database.models import users

def connection_test():
    db = get_db()
    
    assert db is not None

def add_user_test():
    users.insert_one({"nickname":"test_user","score":10})
    found = users.find_one({"nickname":"test_user"})

    assert found is not None
    assert found["score"] == 10