import json
import random
from pprint import pprint

def getPokemonAdjusted(inWeight, inHeight):
    weight = inWeight
    height = inHeight
    aWeight = (weight-60.3278)/.275
    aHeight = (height-1.7)/.06713

    print(aWeight)
    print(aHeight)
    with open('pokemon.json') as f:
        pokemon = json.load(f)
        count = 0
        approvedPokemon = []
        for i in pokemon:
            if count <= 1008:
                if abs(pokemon[i]['heightm']-aHeight) < .2:
                    if abs(pokemon[i]['weightkg']-aWeight) < 7:
                        approvedPokemon.append(i)
            count += 1
        pprint(approvedPokemon)
        print(len(approvedPokemon))
        return approvedPokemon

def getPokemon(inWeight, inHeight):
    weight = inWeight
    height = inHeight
    # aWeight = (weight-60.3278)/.275
    # aHeight = (height-1.7)/.06713

    print(weight)
    print(height)
    with open('pokemon.json') as f:
        pokemon = json.load(f)
        count = 0
        approvedPokemon = []
        for i in pokemon:
            if count <= 1008:
                if abs(pokemon[i]['heightm']-height) < .2:
                    if abs(pokemon[i]['weightkg']-weight) < 7:
                        approvedPokemon.append(i)
            count += 1
        pprint(approvedPokemon)
        print(len(approvedPokemon))
        return approvedPokemon
