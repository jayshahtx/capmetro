import urllib, json, datetime
import pymongo
from db_fns.db import get_mongo_collection

def get_bus_data():
    """Hits cap metro API and returns bus data in JSON form"""

    # hit the API
    url = "https://data.texas.gov/download/gyui-3zdd/text/plain"
    response = urllib.urlopen(url)
    j_response = json.loads(response.read())

    # parse JSON
    vehicles = j_response['soap:Envelope']\
        ['soap:Body']\
        ['FleetlocationResponse']\
        ['Vehicles']\
        ['Vehicle']


    # use the first vehicle's id and its position as the key
    key = str(vehicles[0]["Vehicleid"]) + "--" + str(vehicles[0]["Position"]).replace(".","")

    # update the MongoDB collection, key is defined above and value is all
    # vehicle locations
    collection = get_mongo_collection()

    try:
        return collection.insert_one(
            {
                "_id":key,
                "value":vehicles
            }
        )
    except pymongo.errors.DuplicateKeyError, e:
        print "Data already exists in database"
    