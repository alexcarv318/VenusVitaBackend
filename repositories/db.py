from pymongo import MongoClient
import config

mongo_client = MongoClient(config.MONGO_CONN_URI)
db = mongo_client[config.MONGO_DB_NAME]