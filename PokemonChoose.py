import json
from pprint import pprint

def getPokemonAdjusted(inWeight, inHeight):
    weight = inWeight
    height = inHeight
    aWeight = (weight-60.3278)/.275
    aHeight = (height-1.7)/.06713

    with open('pokemon.json') as f:
        pokemon = json.load(f)
        count = 0
        approvedPokemon = []
        for i in pokemon:
            try:
                pokemon[i]["baseSpecies"]
            except:
                if count <= 1008:
                    if abs(pokemon[i]['heightm']-aHeight) < .2:
                        if abs(pokemon[i]['weightkg']-aWeight) < 7:
                            approvedPokemon.append(i)
                count += 1
        return approvedPokemon

def getPokemon(inWeight, inHeight):
    weight = inWeight
    height = inHeight
    with open('pokemon.json') as f:
        pokemon = json.load(f)
        count = 0
        approvedPokemon = []
        for i in pokemon:
            try:
                pokemon[i]["baseSpecies"]
            except:
                if count <= 1008:
                    if abs(pokemon[i]['heightm']-height) < .2:
                        if abs(pokemon[i]['weightkg']-weight) < 7:
                            approvedPokemon.append(i)
                count += 1
        return approvedPokemon
