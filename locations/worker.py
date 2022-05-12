import string
import random
import json
from .country import Country


def get_ran_country():
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c1 = random.choice(alph)
    c2 = random.choice(alph)
    cCode = "AU"

    rawJson = open('locations/countries-position.json','r')
    # print(rawJson.read())
    jsonObjs = json.loads(rawJson.read())

    for x in jsonObjs['values']:
        if cCode == x['code']:
            selected_country = Country(x['name'], x['code'], ((x['longitude'], x['latitude'])))

            print(str(selected_country.location))
            print("(get_country) Task Finished")

            return selected_country

    get_ran_country()