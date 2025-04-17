from pymongo import MongoClient
from dotenv import load_dotenv 
import os                           ##wbudowany modul pythona do odczytu zmiennej srodowiskowej

#wczytywanie zmiennych srodowiskowych
load_dotenv()

#connection string z .env
connection_string = os.getenv("MONGO_URI")

def get_db():
    try:
        client = MongoClient(connection_string)
        db = client.get_database("snake-db")
        collections = db.list_collection_names()

        #return client["snake-db"]   #nazwa db

        print("Połączenie z bazą danych działa, kolekcje: ", collections)
        return db
    except Exception as e:
        print("Błąd podczas łączenia z bazą MongoDB Atlas", e)
        return None