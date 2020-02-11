import pandas as pd
from pymongo import MongoClient
import common

client = MongoClient("mongodb://localhost/geoProject")
db = client.get_database()

def createAirports():
    air = pd.read_csv("./data/airports.csv")
    air = air.dropna(subset=["wikipedia_link"])
    air = air.drop(air[(air.type == "small_airport") | (air.type == "heliport") | (air.type == "closed") | (
                air.type == "seaplane_base") | (air.type == "medium_airport")].index)
    air = air.drop(columns=["scheduled_service", "local_code", "home_link", "wikipedia_link", "keywords"])
    air["location"] = air[["longitude_deg", "latitude_deg"]].apply(lambda x: common.geoCode(x.longitude_deg, x.latitude_deg), axis=1)
    air.to_json("cleaned_airports.json", orient="records")
    return air

def findAirport(lat, log, dist):
    result = db["airports"].aggregate([
        {
        "$geoNear": {
            "near": {"type": "Point", "coordinates": [lat, log]},
            "distanceField": "dist.calculated",
            "maxDistance": dist,
            "query": {"municipality": "New York"},
            "spherical": "true"
            }
        },
        {"$project": {"_id": 0, "name": 1, "dist.calculated": 1}}
    ])
    return list(result)

def location(lista):
    listaCoordenadas = []
    for i in lista:
        for e in i:
            query = {"name": f"{e['name']}"}
            projection = {"_id": 0, "name": 1, "latitude_deg": 1, "longitude_deg": 1}
            result = db["airports"].find(query, projection)
            listaCoordenadas.append(list(result))
    return listaCoordenadas


