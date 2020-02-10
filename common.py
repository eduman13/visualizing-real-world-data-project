from math import sin, cos, sqrt, atan2, radians

def geoCode(latitude, longitude):
    lat = float(latitude)
    lng = float(longitude)
    return {
        "type": "Point",
        "coordinates": [lat, lng]
    }

def distacePoints(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return round(distance * 1000, 2)

def prettyPrint(lista):
    if lista == None:
        pass
    else:
        return [{
            "name": i["name"],
            "distance": round(i["dist"]["calculated"], 2)
        } for i in lista]
