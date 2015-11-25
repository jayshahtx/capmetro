import os
import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime

collection_ref = None

def get_mongo_collection():
    """Returns mongo collection where our auth tokens are stored"""
    
    global collection_ref

    # check if we have established a connection before
    if collection_ref == None:
        MONGO_URL = os.environ.get('MONGOHQ_URL')
        DB_NAME = os.environ.get('MONGO_DB_NAME')
        DB_COLLECTION = os.environ.get('MONGO_COLLECTION_NAME')
        collection_ref = MongoClient(MONGO_URL)[DB_NAME][DB_COLLECTION]
        return collection_ref
    else:
        return collection_ref