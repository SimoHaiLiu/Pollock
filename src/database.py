import pymongo

class Database(object):
    DATABASE = None
    URI = "mongodb://47.244.166.253:27017"

    @staticmethod
    def initialize():
        client = pymongo.MongoClient('47.244.166.253', 27017)
        Database.DATABASE = client["dashboard"]

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)  # Return the first element

    @staticmethod
    def update(collection, document_id, data):
        Database.DATABASE[collection].update_one ({"id": document_id}, {"$set": data})

