from pymongo import MongoClient
from dotenv import load_dotenv 
import os                           ##wbudowany modul pythona do odczytu zmiennej srodowiskowej

load_dotenv()
CONNECTION_STRING = os.getenv("MONGO_URI")
client = MongoClient(CONNECTION_STRING)

def get_db():
    return client["snake_db"]   #nazwa db