import urllib, json, datetime
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

    # update the MongoDB collection, key is timestamp and value is 
    # vehicle locations
    now = datetime.datetime.now()
    collection = get_mongo_collection()
    return collection.insert_one(
        {
            str(now.strftime("%Y-%m-%d %H:%M:%S")):vehicles
        }
    )

    