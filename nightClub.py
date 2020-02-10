from dotenv import load_dotenv
import os
import requests as r
import common
load_dotenv()

def findNightClub(lat, log, dist):
    token = os.getenv("API_PLACES")
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={token}&location={lat},{log}&radius={dist}&type=night_club"
    information = r.get(url).json()
    return [(i["name"], i["geometry"]["location"]) for i in information["results"]]

def distanceNightClub(nightsClubs, point):
        lista = [{"name": i[0],
                 "distance": common.distacePoints(point[0], point[1], i[1]["lat"], i[1]["lng"]),
                 "latitude": i[1]["lat"],
                 "longitude": i[1]["lng"]
                 } for i in nightsClubs]
        return lista

def addNightClub(lat, log,  dist):
    listaNightClub = findNightClub(lat, log, dist)
    return distanceNightClub(listaNightClub, (lat, log))

def location(lista):
    listaCoordenadas = []
    for i in lista:
        if i == None:
            continue
        for e in i:
            listaCoordenadas.append((e["latitude"], e["longitude"]))
    return listaCoordenadas






