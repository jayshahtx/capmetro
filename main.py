## Hit the URL to get JSON of bus locations
import pdb
import urllib, json
import time

def get_raw_bus_locs():
    """Hits the cap metro API and retrieves bus locations"""

    url = "https://data.texas.gov/download/gyui-3zdd/text/plain"
    response = urllib.urlopen(url)
    return json.loads(response.read())

def parse_data(data):
    """extract the vehicle locations from JSON data"""

    vehicles = data['soap:Envelope']\
        ['soap:Body']\
        ['FleetlocationResponse']\
        ['Vehicles']\
        ['Vehicle']

    return vehicles

def main():


    import time
    while True:
        d = get_raw_bus_locs()
        loc = parse_data(d)
        pdb.set_trace()
        time.sleep(1)

if __name__ == "__main__":
    main()

