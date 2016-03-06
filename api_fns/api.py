import urllib, json, datetime
import pymongo
from db_fns.db import get_mongo_collection
import xmltodict

def get_bus_data():
    """Hits cap metro API and returns bus data in JSON form"""

    # all the routes we want bus data for
    routes = [
        "1",
        "2",
        "3",
        "4",
        "N5",
        "6",
        "7",
        "8",
        "8A",
        "9",
        "X9",
        "10",
        "11",
        "12",
        "J14",
        "15",
        "18",
        "19",
        "20",
        "21",
        "22",
        "24",
        "26",
        "28",
        "29",
        "30",
        "34",
        "35",
        "36",
        "37",
        "39",
        "43",
        "44",
        "47",
        "48",
        "49",
        "X49",
        "49B",
        "50",
        "51",
        "52",
        "52A",
        "53",
        "53A",
        "54",
        "54A",
        "54B",
        "55",
        "55A",
        "55N",
        "56",
        "57",
        "59",
        "60",
        "62",
        "62H",
        "63",
        "63W",
        "65",
        "66",
        "67",
        "68",
        "70",
        "71",
        "72",
        "73",
        "74",
        "75",
        "76",
        "77",
        "78",
        "79",
        "80",
        "81",
        "81W",
        "82",
        "84",
        "85",
        "85A",
        "86",
        "87",
        "88",
        "90",
        "91",
        "92",
        "93",
        "94",
        "95W",
        "95E",
        "96",
        "97",
        "X98",
        "100",
        "103",
        "106",
        "108",
        "111",
        "111A",
        "112",
        "115",
        "119",
        "120",
        "121",
        "124",
        "125",
        "126",
        "128",
        "130",
        "132",
        "134",
        "135",
        "136",
        "143",
        "146",
        "147",
        "148",
        "151",
        "152",
        "155",
        "156",
        "157",
        "165",
        "169",
        "170",
        "171",
        "172",
        "192",
        "201",
        "205",
        "206"
        ]

    
    # time at which we are making this request
    time = str(datetime.datetime.now())

    # make 13 API calls, each requesting data for vehicles in 10 routes
    for x in range(0,13):
        min_list = x*10
        max_list = x*10+10
        subset = routes[min_list:max_list]
        
        # construct the URL
        url = "http://www.ctabustracker.com/bustime/api/v1/getvehicles?key=gHWUtXmL57trkQcf2NTpqPWzC&rt="
        for route in subset:
            url += route + ","
        
        # remove extra comma from URL
        url = url[0:-1]

        # hit the API
        response = urllib.urlopen(url)    
        data = response.read()
        dic = xmltodict.parse(data)

        # save this response in mongo database
        key = time + " !" + str(x)
        collection = get_mongo_collection()

        try:
            collection.insert_one(
                {
                    "_id":key,
                    "value":dic
                }
            )
        except e:
            print "Some error occured"