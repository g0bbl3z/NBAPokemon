import json


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
    deffense = weight*defs + spe
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


def playerStats(givenName):
    with open('players.json') as f:
        players = json.load(f)['players']
        for x in players:
            if('firstName' in x):
                playerName = x['firstName'] + x['lastName']
            else:
                playerName = str(x['name'])
            if(playerName == givenName):

                playerWeight = x['weight']
                playerHeight = x['hgt']
                playerRatings = x['ratings']
                return makePokemon(playerRatings, playerHeight, playerWeight)


def adjStats(givenPlayerStats):
    aStats = {"hp" : 0,
        "atk": 0,
        "def": 0,
        "spa": 0,
        "spd": 0,
        "spe": 0,
        "tot": 0,
    }

    nbaHp = 7984 - 1200
    nbaAtk = 6835 - 2520
    nbaDef = 17514 - 5320
    nbaSpa = 7217 - 2500
    nbaSpd = 8075 - 2420
    nbaSpe = 567567 - 267267
    hpLow = 1200
    atkLow = 2520
    defLow = 5320
    spaLow = 2500
    spdLow = 2420
    speLow = 267267
    pokeHp = 254
    pokeAtk = 185
    pokeDef = 230
    pokeSpa = 188
    pokeSpd = 224
    pokeSpe = 175

    lows = {"hp": hpLow,
            "atk": atkLow,
            "def": defLow,
            "spa": spaLow,
            "spd": spdLow,
            "spe": speLow,
            }

    slopes = {"hp": nbaHp / pokeHp,
              "atk": nbaAtk / pokeAtk,
              "def": nbaDef / pokeDef,
              "spa": nbaSpa / pokeSpa,
              "spd": nbaSpd / pokeSpd,
              "spe": nbaSpe / pokeSpe,
              }

    for i in givenPlayerStats:
        adj = int((givenPlayerStats[i] - lows[i]) / slopes[i])
        aStats[i] = adj
    total = 0
    for j in aStats:
        total += aStats[j]
    aStats["tot"] = total
    return aStats


def topThree(givenPlayerName):
    with open('pokemon.json') as f:
        pokedex = json.load(f)

    nbaHp = 7984-1200
    nbaAtk = 6835-2520
    nbaDef = 17514 - 5320
    nbaSpa = 7217-2500
    nbaSpd = 8075-2420
    nbaSpe = 567567 - 267267
    hpLow = 1200
    atkLow = 2520
    defLow = 5320
    spaLow = 2500
    spdLow = 2420
    speLow = 267267
    pokeHp = 254
    pokeAtk = 185
    pokeDef = 230
    pokeSpa = 188
    pokeSpd = 224
    pokeSpe = 175

    stats = ["hp", "atk", "def", "spa", "spd", "spa"]

    lows = {"hp" : hpLow,
            "atk": atkLow,
            "def": defLow,
            "spa": spaLow,
            "spd": spdLow,
            "spe": speLow,
    }

    slopes = {"hp" : nbaHp/pokeHp,
            "atk": nbaAtk/pokeAtk,
            "def": nbaDef/pokeDef,
            "spa": nbaSpa/pokeSpa,
            "spd": nbaSpd/pokeSpd,
            "spe": nbaSpe/pokeSpe,
    }

    count = 0
    minDif = [9999999999, "name"]
    minList = [minDif,minDif,minDif]
    playerStatsats = playerStats(givenPlayerName)

    for pokemon in pokedex:
        if count <= 1008:
            squaredDiff = 0
            for stat in stats:
                adj = (playerStatsats[stat] - lows[stat]) / slopes[stat]
                squaredDiff += (adj - pokedex[pokemon]['baseStats'][stat])**2
                #if best
            if squaredDiff < minList[0][0]:
                minList[2] = minList[1]
                minList[1] = minList[0]
                minList[0] = [squaredDiff, pokemon]
                #if 2nd
            elif squaredDiff < minList[1][0]:
                minList[2] = minList[1]
                minList[1] = [squaredDiff, pokemon]
                #if 3rd
            elif squaredDiff < minList[2][0]:
                minList[2] = [squaredDiff, pokemon]
        count += 1
    return minList

givenName = "Nikola Jokic"
print(topThree(givenName))
print(adjStats(playerStats(givenName)))
