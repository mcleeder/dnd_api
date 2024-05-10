from fastapi import Body, FastAPI, HTTPException
from pymongo import MongoClient
from models.monster import Monster
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("mongo_uri")

client = MongoClient(mongo_uri)
db = client['dungeons_dragons']
collection = db['monsters']

app = FastAPI()


@app.get('/monsters', response_model=List[Monster])
def get_all_monsters():
    return list(collection.find({}, {'_id': False}))

@app.get("/monsters/search", response_model=List[Monster])
def search_monsters(**filters: dict):
    query = {}
    for k, v in filters.items():
        if k in Monster.__annotations__:
            query[k] = v
    return list(collection.find(query, {'_id': False}))

@app.get('/monsters/{name}', response_model=Monster)
def get_monster_by_name(name: str):
    if document := collection.find_one({'name': name}, {'_id': False}):
        return document
    raise HTTPException(status_code=404, detail="Data not found")

