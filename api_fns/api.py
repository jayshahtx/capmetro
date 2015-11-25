import urllib, json


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

    return vehicles