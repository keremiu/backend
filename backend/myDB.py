import os
import glob
import pymongo
import json

class myDB:
    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        # Check if data is a list, if not, put it in a list
        if not isinstance(data, list):
            data = [data]
        return data
    @staticmethod
    def update_to_mongo(db_name, collection_name, data, connection_string='mongodb+srv://kerem:ztwk3iTKlL8RuQyE@cluster0.0pubafo.mongodb.net/'):
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]
        collection.delete_many({})  # Delete all documents in the collection
        result = collection.insert_many(data)  # Insert new data
        return result
    @staticmethod
    def insert_to_mongo(db_name, collection_name, data, connection_string='mongodb+srv://kerem:ztwk3iTKlL8RuQyE@cluster0.0pubafo.mongodb.net/'):
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]
        result = collection.insert_many(data)
        return result

    @staticmethod
    def get_data_from_mongo(db_name, collection_name, connection_string='mongodb+srv://kerem:ztwk3iTKlL8RuQyE@cluster0.0pubafo.mongodb.net/'):
        client = pymongo.MongoClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]
        data = list(collection.find())
        return data

    @staticmethod
    def insert_to_mongo_from_directory(db_name, dir_path, files=None, connection_string='mongodb+srv://kerem:ztwk3iTKlL8RuQyE@cluster0.0pubafo.mongodb.net/'):
        # Get list of all JSON files in the directory
        json_files = glob.glob(os.path.join(dir_path, '*.json'))
        print(json_files)
        for file_path in json_files:
            # Get the name of the file without extension (to be used as collection name)
            collection_name = os.path.splitext(os.path.basename(file_path))[0]

            # If a list of files is specified, only load these files
            if files is not None and collection_name not in files:
                continue

            # Load JSON data from file
            data = myDB.load_json(file_path)

            # Insert data into MongoDB
            myDB.insert_to_mongo(db_name, collection_name, data, connection_string)