import json
import urllib.request

key = ""

def request(url):
    """general function for pulling down url requests
    input: url
    output: dictionary containing json contents
    """
    RESPONSE = urllib.request.urlopen(url)
    READ_RESPONSE = RESPONSE.read().decode('utf-8')
    RESPONSE_DICT = json.loads(READ_RESPONSE)
    return RESPONSE_DICT

def get_bus_time(key = key):
    """gets official cta time"""
    URL = ("http://www.ctabustracker.com/bustime/api/v2/gettime?key="
    +key+"&format=json")
    RESPONSE = request(URL)
    return RESPONSE["bustime-response"]

def get_vehicles(vid, key = key, tmres = "s"):
    """gets list of CTA vehicles
    takes list of ID numbers of length less than 11
    outputs list of dictionaries"""
    if len(vid) > 9:
        vid = vid[:10]
        print("More than ten Vids entered. Using first ten")
    vids = ""
    for i in vid:
        vids = vids + "," + i
    vids = vids[1:]
    URL = ("http://ctabustracker.com/bustime/api/v2/getvehicles?key="
    + key +"&vid=" + vids + "&tmres=" + tmres + "&format=json")
    print(URL)
    return request(URL)["bustime-response"]

def get_routes(key = key):
    """gets list of routes
    outputs list of dictionaries
    """
    URL = "http://www.ctabustracker.com/bustime/api/v2/getroutes?key=" + key + "&format=json"
    ROUTES_LIST = request(URL)["bustime-response"]["routes"]
    return ROUTES_LIST

def get_directions(rt, key = key):
    """takes route number and gets list of directions for route"""
    URL = "http://www.ctabustracker.com/bustime/api/v2/getdirections?key="+ key + "&rt=" + rt + "&format=json"
    print(URL)
    return request(URL)["bustime-response"]

def get_stops(rt, direction, key = key):
    """get's list of directional stops from route number and direction
    direction must be in the form 'Northbound', 'Southbound', 'Eastbound', or 'Westbound'
    """
    DIRECTIONS = ["Northbound","Southbound","Eastbound", "Westbound"]
    if direction not in DIRECTIONS:
        print("Error, please use 'Northbound', 'Southbound', 'Eastbound', or 'Westbound' for direction argument")
        return None
    URL =  "http://www.ctabustracker.com/bustime/api/v2/getstops?key=" + key + "&rt=" + rt + "&dir=" + direction + "&format=json"
    print(URL)
    return request(URL)["bustime-response"]["stops"]
def get_predictions(stpid, rt, key = key):
    STPID = ""
    for i in stpid:
        STPID = STPID+ "," + i
    STPID = STPID[1:]
    URL = "http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=" + key + "&rt=" + rt + "&stpid=" + STPID + "&format=json"
    print(URL)
    return request(URL)["bustime-response"]
print(get_stops("55", "Eastbound")[15])
print(get_predictions(["10500"],"55"))
