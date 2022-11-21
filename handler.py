from pymongo import MongoClient
import configfile as config
from datetime import datetime


class MongoHandler:

    def __init__(self):
        self.db = None
        self.client = None

        self.post_buffer = []
        self.delete_buffer = []

        if config.DBCONFIG["address"] is None:
            raise Exception("MongoLoader: Configuration file has 'None' value for server IP address.")
        if config.DBCONFIG["port"] is None:
            raise Exception("MongoLoader: Configuration file has 'None' value for server port number.")
        if config.DBCONFIG["db"] is None:
            raise Exception("MongoLoader: Configuration file has 'None' value for server database name.")
        self.__get_parsed_data()


    def __get_parsed_data(self):
        self.__connect_to_db_()
        self.idsDB = set()

        for item in self.db['update'].find({}, {"_id": 0, "id": 1}, no_cursor_timeout=True):
            self.idsDB.add(int(item['id']))

        self.deletDB = set()
        for item in self.db['deletions'].find({}, {"_id": 0, "id": 1}, no_cursor_timeout=True):
            self.deletDB.add(int(item['id']))
        self.__disconnect_from_db_()


    def handler_post(self, data):
        post_id = data["id"]
        if post_id not in self.idsDB:
            self.idsDB.add(post_id)
            data["probe_at"] = datetime.now()
            self.post_buffer.append(data)
            if len(self.post_buffer) >= 200:
                print(f'{datetime.now()}-->Handler insert to mongo new:{len(self.post_buffer)} posts')
                self.__store_posts()


    def handler_deletion(self, delete_id):
        if delete_id not in self.deletDB:
            self.deletDB.add(delete_id)
            self.delete_buffer.append({"id": delete_id, "created_at": datetime.now()})
            if len(self.delete_buffer) >= 50:
                print(f'{datetime.now()}-->Handler insert to mongo new:{len(self.delete_buffer)} deletions')
                self.__store_deletions()

    def __store_posts(self):
        self.__connect_to_db_()
        self.db['update'].insert_many(self.post_buffer)
        self.__disconnect_from_db_()
        self.post_buffer = []

    def __store_deletions(self):
        self.__connect_to_db_()
        self.db['deletions'].insert_many(self.delete_buffer)
        self.__disconnect_from_db_()
        self.delete_buffer = []

    ##############################
    # Connect to MongoDB
    ##############################
    def __connect_to_db_(self):
        # connect to mongo db collection
        self.__disconnect_from_db_()
        self.client = MongoClient(config.DBCONFIG["address"], config.DBCONFIG["port"])
        self.db = self.client[config.DBCONFIG["db"]]
        self.collection = self.db['tweets']

    ##############################
    # Disconnect from mongo DB
    ##############################
    def __disconnect_from_db_(self):
        if not (self.client is None):
            self.client.close()
            self.client = None
