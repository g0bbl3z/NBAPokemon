import json
import random
from pprint import pprint


weight = 77
height = 1.88
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
            if abs(pokemon[i]['heightm']-aHeight) < 1:
                if abs(pokemon[i]['weightkg']-aWeight) < 1:
                    approvedPokemon.append(i)
        count += 1
    pprint(approvedPokemon)
    print(len(approvedPokemon))

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
    healthPoints = str*end + reb
    attack = off*fg + ft
    deffense = weight*defs
    specialAttack = tp*height + dnk
    speed = spe*end*drb
    specialDefense = str*jmp



