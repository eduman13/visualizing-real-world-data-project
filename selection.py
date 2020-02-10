import pandas as pd

def airportsSelect(airport):
    airportSum = 0
    if airport == None:
        return airportSum
    for i in airport:
        if 0 <= i["distance"] <= 5000:
            airportSum += 3
        if 5000 < i["distance"] <= 10000:
            airportSum += 2
        if 10000 < i["distance"] <= 15000:
            airportSum += 1
    return airportSum / len(airport)

def starbuckSelect(starbuck):
    starbuckSum = 0
    if starbuck == None:
        return starbuckSum
    for i in starbuck:
        if 0 <= i["distance"] <= 83.33:
            starbuckSum += 3
        if 83.34 <= i["distance"] <= 166.67:
            starbuckSum += 2
        if 166.68 <= i["distance"] <= 250:
            starbuckSum += 1
    return starbuckSum / len(starbuck)

def nightClubSelect(nightClub):
    nightClubSum = 0
    if nightClub == None:
        return nightClubSum
    for i in nightClub:
        if 0 <= i["distance"] <= 166.66:
            nightClubSum += 3
        if 166.67 <= i["distance"] <= 333.33:
            nightClubSum += 2
        if 333.34 <= i["distance"] <= 500:
            nightClubSum += 1
    return nightClubSum / len(nightClub)

def selection(companies):
    airports = [airportsSelect(i) for i in companies.airport.values.tolist()]
    satrbucks = [starbuckSelect(i) for i in companies.starBuck.values.tolist()]
    nightClub = [nightClubSelect(i) for i in companies.nightClub.values.tolist()]
    companies["airportRaiting"] = airports
    companies["starBucksRaiting"] = satrbucks
    companies["nightClubRaiting"] = nightClub
    companies["sumTotal"] = companies["airportRaiting"].rank() * 0.5 + companies["starBucksRaiting"].rank() * 0.25 + companies["nightClubRaiting"].rank() * 0.25
    return companies

