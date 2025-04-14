from .db import get_db

db = get_db()

users = db["users"]     ##gracze
games = db["games"]     ##dane o rozegranych grach