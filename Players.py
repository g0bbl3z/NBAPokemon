import json
import random
from pprint import pprint


weight = 77
height = 1.88
aWeight = (weight-60.3278)/.275
aHeight = (height-1.7)/.06713


#print(aWeight)
#print(aHeight)
with open('pokemon.json') as f:
    pokemon = json.load(f)
    count = 0
    approvedPokemon = []
    for i in pokemon:
        if count <= 1008:
            if abs(pokemon[i]['heightm']-aHeight) < 1:
                if abs(pokemon[i]['weightkg']-aWeight) < 1:
                    approvedPokemon.append(i)
        count += 1
    #pprint(approvedPokemon)
    #print(len(approvedPokemon))

with open('players.json') as f:
    players = json.load(f)['players']
    for x in players:
        try:
            pprint("Name: " + x['name'] + " Weight: " + str(x['weight']) + " Height: " + str(x['hgt']))
        except:
            pass



