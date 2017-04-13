import json
from numpy import std, mean

path = 'data/yelp_funny_b.json'
with open(path) as json_data:
    d = json.load(json_data)[:10]
    for x in d:
        print x['text']
        print '*'
