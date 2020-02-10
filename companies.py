import pandas as pd
from pymongo import MongoClient
import common

def clean_companies():
    client = MongoClient("mongodb://localhost/companies")
    db = client.get_database()
    query = {
        "$and": [
            {"founded_year": {"$gte": 2005}},
            {"offices": {"$elemMatch": {"latitude": {"$ne": None}, "longitude": {"$ne": None}}}}
        ]
    }
    projection = {"name": 1, "offices.city": 1, "offices.latitude": 1, "offices.longitude": 1, "_id": 0}
    result = db["companies"].find(query, projection)
    companies = pd.DataFrame(list(result))
    companies = companies.explode("offices")
    companiesCleaned = companies[["offices"]].apply(lambda x: x.offices, result_type="expand", axis=1)
    cleanCompanies = pd.concat([companies, companiesCleaned], axis=1)
    cleanCompanies.drop(columns=["offices"], inplace=True)
    cleanCompanies = cleanCompanies.dropna(subset=["city", "latitude", "longitude"])
    cleanCompanies["location"] = cleanCompanies[["longitude", "latitude"]].apply(lambda x: common.geoCode(x.longitude, x.latitude), axis=1)
    cleanCompanies.to_json("cleaned_companies.json", orient="records")
    cleanCompanies = cleanCompanies[(cleanCompanies.city == "New York") | (cleanCompanies.city == "New York City")]
    return cleanCompanies
