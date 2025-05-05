from .db import get_db
import json

db = get_db()

users = db["users"]     ##gracze
games = db["games"]     ##dane o rozegranych grach

         #CRUD( Create, Read, Update, Delete)
#Create
#MongoDB ma swoj wlasny unikalny _id tworzony automatycznie
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

def get_users_list():
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
    update_fields = {}          #pusty slownik jest traktowany jako False

    if score is not None:
        update_fields["score"] = score

    if map_size is not None:
        update_fields["map_size"] = map_size

    if update_fields:
        return users.update_one(
            {"nick": nick},
            {"$set": update_fields}
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

#Zapisywanie danych do CSV/JSON po zamknięciu aplikacji
def save_data(filename="data_backup.json"):
    data = get_games_list()
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 4, default = str)

#wczytanie danych
def load_data_from_file(filename="data_backup.json"):
    try:
        #{} - wszystkie dokumenty w kolekcji games
        if games.count_documents({}) > 0:
            print(f"Baza danych nie jest pusta")
            return
        with open(filename, "r", encoding = "utf-8") as file:
            data = json.loads(file)
            #czy data to lista
            if isinstance(data, list):
                if data:
                    games.insert_many(data)
                    print(f"Wczytano {len(data)} rekordow z pliku {filename}")
                else:
                    print(f"Nie znaleziono listy rekordow w pliku {filename}")
            elif isinstance(data, dict):
                games.insert_one(data)
                print(f"Wczytano 1 rekord z pliku {filename}")
            else:
                print(f"Nieprawidlowy format danych w pliku {filename}")
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje")
    except Exception as e:
        print(f"Blad podczas wczytywania danych z pliku {filename}: {e}")
