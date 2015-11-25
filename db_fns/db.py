import os
import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime

def get_mongo_collection():
    """Returns mongo collection where our auth tokens are stored"""

    MONGO_URL = os.environ.get('MONGOHQ_URL')
    DB_NAME = os.environ.get('MONGO_DB_NAME')
    DB_COLLECTION = os.environ.get('MONGO_COLLECTION_NAME')
    print MONGO_URL
    print DB_NAME
    print DB_COLLECTION
    return MongoClient(MONGO_URL)[DB_NAME][DB_COLLECTION]