import googlemaps
from math import sin, cos, sqrt, atan2, radians

#Define google maps
gmaps = googlemaps.Client(key="AIzaSyCme-XTBo-DfwIW6J7qY76MTVWIvsBJ7HU")

def get_coords(address):
    response = gmaps.geocode(address)
    coordinates = response[0]['geometry']['location']
    return coordinates

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 0.621371
    return distance

#Get current location
city = input("What city are you located in?")
state = input("What state are you in?")
address = city + ' , ' + state
location_coords = get_coords(address)

# Get desination coordinates
destination = input("Where would you like to go?")
destination_coords = get_coords(destination)

# Split latitude and longitudes
lat1 = radians(location_coords['lat'])
lon1 = radians(location_coords['lng'])
lat2 = radians(destination_coords['lat'])
lon2 = radians(destination_coords['lng'])
distance = calculate_distance(lat1, lon1, lat2, lon2)
print("You have to travel", distance, "  miles!")




