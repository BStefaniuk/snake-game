from .db import get_db

db = get_db()

users = db["users"]     ##gracze
games = db["games"]     ##dane o rozegranych grach

        #CRUD( Create, Read, Update, Delete)
#Create
def add_user(nick: str, score: int = 0, map_size: str = "10x10"):
    return users.insert_one({
        "nick": nick, 
        "score": score,
        "map_size": map_size
    })

def add_game(nick: str, date: str, playing_time: float, score: int):
    return games.insert_one({
        "nick": nick,
        "date": date,
        "playing_time": playing_time,
        "score": score
    })

#Read
def get_user(nick: str):
    return users.find_one({
        "nick": nick
    })

def get_user_games(nick: str):
    return list(
        games.find({"nick": nick})      #lista gier uzytkownika
    )

def get_useres_list():
    return list(
        users.find()            #list graczy
    )

def get_games_list():
    return list(
        games.find()        #historia gier
    )

def get_top_score():
    return games.find_one(      #zwraca jeden wynik
        sort=[("score", -1)]    #sortuje malejaco, najlepszy wynik jako pierwszy
    )