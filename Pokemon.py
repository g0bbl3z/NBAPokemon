import json
import random
from pprint import pprint

#POKEMON
#hp 1, 255
#atk 5, 190
#def 0, 230
#spa 6, 194
#spd 6, 230
#spe 5, 180

stats = ["hp", "atk", "def", "spa", "spd", "spa"]

def makePokemon(rating,height,weight):
    reb = rating[0]["reb"]
    end = rating[0]["endu"]
    str = rating[0]["stre"]
    ft = rating[0]["ft"]
    off = rating[0]["oiq"]
    fg = rating[0]["fg"]
    defs = rating[0]["diq"]
    tp = rating[0]["tp"]
    dnk = rating[0]["dnk"]
    drb = rating[0]["drb"]
    spe = rating[0]["spd"]
    jmp = rating[0]["jmp"]
    healthPoints = str*end + reb
    attack = off*fg + ft
    deffense = weight*defs
    specialAttack = tp*height + dnk
    speed = spe*end*drb
    specialDefense = str*jmp
    return {"hp" : healthPoints,
            "atk" : attack,
            "def" : deffense,
            "spa" : specialAttack,
            "spe" : speed,
            "spd" : specialDefense
            }

#PLAYERS
#hp 1200 7984
#atk 2520 6835
#def 5320 17514
#spa 2500 7217
#spd 2420 8075
#spe 267267 567567

with open('players.json') as f:
    players = json.load(f)['players']
    for x in players:
        try:
            playerName = x['name']
            playerWeight = x['weight']
            playerHeight = x['hgt']
            playerRatings = x['ratings']
            # pprint("Name: " + x['name'] + " Weight: " + str(x['weight']) + " Height: " + str(x['hgt']))
            # pprint("Ratings: " + str(x['ratings']))
            poke = makePokemon(playerRatings, playerHeight, playerWeight)
            if poke > maxValue:
                maxValue = poke
                maxPlayer = playerName
            if poke < minValue:
                minValue = poke
                minPlayer = playerName
        except:
            pass

def playerStats(givenName):
    with open('players.json') as f:
        players = json.load(f)['players']
        for x in players:
            # if(x['name'] ==)
            try:
                playerName = x['name']
                playerWeight = x['weight']
                playerHeight = x['hgt']
                playerRatings = x['ratings']
                # pprint("Name: " + x['name'] + " Weight: " + str(x['weight']) + " Height: " + str(x['hgt']))
                # pprint("Ratings: " + str(x['ratings']))
                poke = makePokemon(playerRatings, playerHeight, playerWeight)
                if poke > maxValue:
                    maxValue = poke
                    maxPlayer = playerName
                if poke < minValue:
                    minValue = poke
                    minPlayer = playerName
            except:
                pass

nbaHp = 7984-1200
nbaAtk = 6835-2520
nbaDef = 17514 - 5320
nbaSpa = 7217-2500
nbaSpd = 8075-2420
nbaSpe = 567567 - 267267
pokeHp = 254
pokeAtk = 185
pokeDef = 230
pokeSpa = 188
pokeSpd = 224
pokeSpe = 175
slopes = {"hp" : nbaHp/pokeHp,
        "atk": nbaAtk/pokeAtk,
        "def": nbaDef/pokeDef,
        "spa": nbaSpa/pokeSpa,
        "spd": nbaSpd/pokeSpd,
        "spe": nbaSpe/pokeSpe,
}

possiblePokemon = []
percent = 100
while len(possiblePokemon) > 5 and len(possiblePokemon) != 0:
    with open('pokemon.json') as f:
        pokedex = json.load(f)
        count = 0
        for pokemon in pokedex:
            if count <= 1008:
                for stat in stats:
                    a
            count += 1