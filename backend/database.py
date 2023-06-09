import motor.motor_asyncio
from model import Odds
from model import Match
from model import Matches
from typing import List
import pymongo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://kerem:ztwk3iTKlL8RuQyE@cluster0.0pubafo.mongodb.net/')
database = client.BahisSiteleriCur2


async def fetch_all_teams(collection_name: str) -> List[str]:
    collection = database[collection_name]
    cursor = collection.find({})
    teams = []
    async for document in cursor:
        if "Teams" in document:
            teams.append(document["Teams"])
    return teams


async def fetch_all_odds(collection_name: str) -> List[Odds]:
    collection = database[collection_name]
    cursor = collection.find({})
    odds = []
    async for document in cursor:
        if "1x2" in document:
            odds.append(document["1x2"])
    return odds