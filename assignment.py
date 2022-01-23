# import needed libraries
import requests
import math

# api endpoint
URL_PATH = "https://nominatim.openstreetmap.org/search.php"


def get_lat_lon(location):
    # q for query. format is json as specified from examples in documentation
    PARAMS = {"q": location, "format": "jsonv2"}

    # send a GET request and save response object to variable
    r = requests.get(url=URL_PATH, params=PARAMS)

    # extract data from response object in and  parse json data
    data = r.json()

    # print data for investigative purposes
    # print(location, data)

    # access desired values
    latitude = float(data[0]["lat"])
    longitude = float(data[0]["lon"])
    return [latitude, longitude]


# end of get_lat_lon(location):


def distance_calculation(orig, dest):
    # longitude is the second part of our returned coord array
    dlon = dest[1] - orig[1]  # dlon = lon2 - lon1
    # latitude is the first part at index 0
    dlat = dest[0] - orig[0]  # dlat = lat2 - lat1
    # a = (sin(dlat / 2)) ^ 2 + cos(lat1) * cos(lat2) *(sin(dlon / 2)) ^ 2
    a = (math.sin(math.radians(dlat / 2))) ** 2 + (math.cos(math.radians(orig[0]))) * (
        math.cos(math.radians(dest[0]))
    ) * (math.sin(math.radians(dlon / 2))) ** 2
    # c = 2 * atan2(sqrt(a), sqrt(1 - a))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961  # gives miles. switch to 6373 for kilometers
    d = R * c

    return d
