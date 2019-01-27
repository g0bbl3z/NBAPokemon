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

def findPokemon(pokedex, rating,height,weight):
    reb = rating[0]
    end = rating[0]
    str = rating[0]
    ft = rating[0]
    off = rating[0]
    fg = rating[0]
    defs = rating[0]
    tp = rating[0]
    dnk = rating[0]
    drb = rating[0]
    spe = rating[0]
    jmp = rating[0]
    healthPoints = int((str+end +reb)/3)
    attack = int(off+fg + ft)/3
    deffense = int((weight+defs)/2)
    specialAttack = int((tp+height+dnk)/3)
    speed = int((spe+end+drb)/3)
    specialDefense = int((str+jmp)/2)
