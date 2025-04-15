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

#Update
def update_user_data(nick: str, score: int = None, map_size: str = None):
    update_fileds = {}          #pusty slownik jest traktowany jako False

    if score is not None:
        update_fileds["score"] = score

    if map_size is not None:
        update_fileds["map_size"] = map_size

    if update_fileds:
        return users.update_one(
            {"nick": nick},
            {"$set": update_fileds}
        )
    
    return None #jak nic do aktualizacji to nic nie zwraca

#Delete
def delete_user(nick: str):
    users.delete_one({
        "nick": nick        #usuwa danego uzytkownika
    })
    games.delete_many({
        "nick": nick        #usuwa cala historie gier uzytkownika
    })

def delete_all_users():
    users.delete_many({})

def delete_all_games():
    games.delete_many({})