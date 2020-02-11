import pandas as pd
from pymongo import MongoClient
import common

client = MongoClient("mongodb://localhost/geoProject")
db = client.get_database()

def cleanStarbucks():
    starbucks = pd.read_csv("./data/starbucks.csv")
    starbucks = starbucks.drop(
        columns=["Ownership Type", "Facility ID", "Features - Products", "Features - Service", "Features - Stations",
                 "Food Region", "Venue Type", "Phone Number", "Zip", "Insert Date", "Coordinates", "Street Line 1",
                 "Street Line 2", "Location", "Street Address", "Store Number"])
    starbucks = starbucks.rename(columns={i: i.lower() for i in starbucks.columns.tolist()})
    starbucks["location"] = starbucks[["longitude", "latitude"]].apply(lambda x: common.geoCode(x.longitude, x.latitude ), axis=1)
    starbucks.to_json("cleaned_starbucks.json", orient="records")
    return starbucks

def findStarbuck(lat, log, dist):
    result = db["starbucks"].aggregate([
        {
            "$geoNear": {
                "near": {"type": "Point", "coordinates": [lat, log]},
                "distanceField": "dist.calculated",
                "maxDistance": dist,
                "query": {"city": "New York"},
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
            projection = {"_id": 0, "name": 1, "latitude": 1, "longitude": 1}
            result = db["starbucks"].find(query, projection)
            listaCoordenadas.append(list(result))
    return listaCoordenadas
