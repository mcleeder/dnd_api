import csv, os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("mongo_uri")

client = MongoClient(mongo_uri)

db = client['dungeons_dragons']
collection = db['monsters']

csv_file_path = "./_csv_data/dnd_monsters.csv"

with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        collection.insert_one(row)

client.close()

print("Data has been uploaded to MongoDB.")
