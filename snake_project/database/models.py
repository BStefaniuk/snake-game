from .db import get_db

db = get_db()

users = db["users"]     ##gracze
games = db["games"]     ##dane o rozegranych grach

        #CRUD( Create, Read, Update, Delete)
#Create
def add_user(nick: str, score: int):
    return users.insert_one({
        "nick": nick, 
        "score": score
    })

def add_game(nick: str, date: str, playing_time: int, score: int):
    return games.insert_one({
        "nick": nick,
        "date": date,
        "playing_time": playing_time,
        "score": score
    })

