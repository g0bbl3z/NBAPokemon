import json
from pprint import pprint

with open('pokemon.json') as f:
    data = json.load(f)

pprint(data)